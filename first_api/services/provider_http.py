import asyncio
import logging
import random
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Literal

import httpx
from pydantic import BaseModel, Field, ValidationError

from .ai_clients import AIClientConfig, AIClientError, PredictionLabel, PredictionResult


RETRYABLE_PROVIDER_STATUS_CODES = {429, 500, 502, 503, 504}
logger = logging.getLogger(__name__)
RetrySleep = Callable[[float], Awaitable[None]]
RetryRandom = Callable[[], float]
RetryDelaySource = Literal["retry_after", "local_backoff"]
RetryFailureReason = Literal["timeout", "http_status", "request_error"]


@dataclass(frozen=True)
class ProviderHealthResult:
    ok: bool
    provider: str
    status_code: int
    message: str


@dataclass(frozen=True)
class RetryDelayPlan:
    delay_seconds: float
    source: RetryDelaySource


class ProviderPredictionPayload(BaseModel):
    text: str
    mode: str


class ProviderPredictionBody(BaseModel):
    label: PredictionLabel
    score: float = Field(ge=0, le=1)


def is_retryable_provider_status(status_code: int) -> bool:
    return status_code in RETRYABLE_PROVIDER_STATUS_CODES


def parse_retry_after_delay(
    retry_after: str | None,
    now: datetime | None = None,
) -> float | None:
    if retry_after is None:
        return None

    value = retry_after.strip()
    if value.isdecimal():
        return float(value)

    try:
        retry_at = parsedate_to_datetime(value)
    except (TypeError, ValueError, IndexError, OverflowError):
        return None

    if retry_at.tzinfo is None:
        retry_at = retry_at.replace(tzinfo=timezone.utc)

    current_time = now or datetime.now(timezone.utc)
    if current_time.tzinfo is None:
        current_time = current_time.replace(tzinfo=timezone.utc)

    delay_seconds = (retry_at - current_time).total_seconds()
    return max(delay_seconds, 0.0)


def calculate_retry_jitter(
    config: AIClientConfig,
    random_fraction: RetryRandom = random.random,
) -> float:
    jitter_seconds = max(config.retry_jitter_seconds, 0.0)
    if jitter_seconds == 0:
        return 0.0

    fraction = min(max(random_fraction(), 0.0), 1.0)
    return jitter_seconds * fraction


def calculate_retry_delay(
    attempt: int,
    config: AIClientConfig,
    retry_after: str | None = None,
    now: datetime | None = None,
    random_fraction: RetryRandom = random.random,
) -> float:
    return build_retry_delay_plan(
        attempt,
        config,
        retry_after=retry_after,
        now=now,
        random_fraction=random_fraction,
    ).delay_seconds


def build_retry_delay_plan(
    attempt: int,
    config: AIClientConfig,
    retry_after: str | None = None,
    now: datetime | None = None,
    random_fraction: RetryRandom = random.random,
) -> RetryDelayPlan:
    base_delay = max(config.retry_base_delay_seconds, 0.0)
    max_delay = max(config.retry_max_delay_seconds, 0.0)
    provider_delay = parse_retry_after_delay(retry_after, now=now)
    if provider_delay is not None:
        return RetryDelayPlan(
            delay_seconds=min(provider_delay, max_delay),
            source="retry_after",
        )

    exponential_delay = base_delay * (2 ** (attempt - 1))
    jitter_delay = calculate_retry_jitter(config, random_fraction=random_fraction)
    return RetryDelayPlan(
        delay_seconds=min(exponential_delay + jitter_delay, max_delay),
        source="local_backoff",
    )


async def wait_before_retry(
    attempt: int,
    config: AIClientConfig,
    sleep: RetrySleep,
    retry_reason: RetryFailureReason,
    retry_after: str | None = None,
    status_code: int | None = None,
    random_fraction: RetryRandom = random.random,
) -> None:
    delay_plan = build_retry_delay_plan(
        attempt,
        config,
        retry_after=retry_after,
        random_fraction=random_fraction,
    )
    logger.info(
        "provider_prediction_retry_scheduled",
        extra={
            "attempt": attempt,
            "max_attempts": config.max_attempts,
            "retry_reason": retry_reason,
            "status_code": status_code,
            "retry_after": retry_after,
            "delay_seconds": delay_plan.delay_seconds,
            "delay_source": delay_plan.source,
        },
    )
    if delay_plan.delay_seconds > 0:
        await sleep(delay_plan.delay_seconds)


def log_retry_exhausted(
    attempt: int,
    config: AIClientConfig,
    retry_reason: RetryFailureReason,
    error_code: str,
    retry_after: str | None = None,
    status_code: int | None = None,
) -> None:
    logger.warning(
        "provider_prediction_retry_exhausted",
        extra={
            "attempt": attempt,
            "max_attempts": config.max_attempts,
            "retry_reason": retry_reason,
            "status_code": status_code,
            "retry_after": retry_after,
            "error_code": error_code,
        },
    )


async def check_provider_health(
    url: str,
    config: AIClientConfig,
    client: httpx.AsyncClient | None = None,
) -> ProviderHealthResult:
    owns_client = client is None
    active_client = client or httpx.AsyncClient(
        timeout=config.timeout_seconds,
        trust_env=False,
    )

    try:
        response = await active_client.get(url)
        response.raise_for_status()
    except httpx.TimeoutException as exc:
        raise AIClientError(
            message="The AI provider health check timed out.",
            error_code="ai_provider_timeout",
        ) from exc
    except httpx.HTTPStatusError as exc:
        raise AIClientError(
            message=f"The AI provider returned HTTP {exc.response.status_code}.",
            error_code="ai_provider_http_error",
        ) from exc
    except httpx.RequestError as exc:
        raise AIClientError(
            message="The AI provider could not be reached.",
            error_code="ai_provider_request_error",
        ) from exc
    finally:
        if owns_client:
            await active_client.aclose()

    return ProviderHealthResult(
        ok=True,
        provider=config.provider,
        status_code=response.status_code,
        message="The AI provider responded successfully.",
    )


async def request_provider_prediction(
    url: str,
    text: str,
    mode: str,
    config: AIClientConfig,
    client: httpx.AsyncClient | None = None,
    sleep: RetrySleep = asyncio.sleep,
    random_fraction: RetryRandom = random.random,
) -> PredictionResult:
    owns_client = client is None
    active_client = client or httpx.AsyncClient(
        timeout=config.timeout_seconds,
        trust_env=False,
    )

    try:
        for attempt in range(1, config.max_attempts + 1):
            try:
                response = await active_client.post(
                    url,
                    json=ProviderPredictionPayload(text=text, mode=mode).model_dump(),
                )
                response.raise_for_status()
                body = ProviderPredictionBody.model_validate(response.json())
                return PredictionResult(
                    label=body.label,
                    score=round(body.score, 2),
                    source=f"{config.provider}-provider",
                )
            except httpx.TimeoutException as exc:
                if attempt < config.max_attempts:
                    await wait_before_retry(
                        attempt,
                        config,
                        sleep,
                        retry_reason="timeout",
                        random_fraction=random_fraction,
                    )
                    continue
                log_retry_exhausted(
                    attempt=attempt,
                    config=config,
                    retry_reason="timeout",
                    error_code="ai_provider_timeout",
                )
                raise AIClientError(
                    message="The AI provider prediction request timed out.",
                    error_code="ai_provider_timeout",
                ) from exc
            except httpx.HTTPStatusError as exc:
                status_code = exc.response.status_code
                retryable_status = is_retryable_provider_status(status_code)
                if attempt < config.max_attempts and retryable_status:
                    await wait_before_retry(
                        attempt,
                        config,
                        sleep,
                        retry_reason="http_status",
                        retry_after=exc.response.headers.get("Retry-After"),
                        status_code=status_code,
                        random_fraction=random_fraction,
                    )
                    continue
                if retryable_status:
                    log_retry_exhausted(
                        attempt=attempt,
                        config=config,
                        retry_reason="http_status",
                        error_code="ai_provider_http_error",
                        retry_after=exc.response.headers.get("Retry-After"),
                        status_code=status_code,
                    )
                raise AIClientError(
                    message=f"The AI provider returned HTTP {status_code}.",
                    error_code="ai_provider_http_error",
                ) from exc
            except httpx.RequestError as exc:
                if attempt < config.max_attempts:
                    await wait_before_retry(
                        attempt,
                        config,
                        sleep,
                        retry_reason="request_error",
                        random_fraction=random_fraction,
                    )
                    continue
                log_retry_exhausted(
                    attempt=attempt,
                    config=config,
                    retry_reason="request_error",
                    error_code="ai_provider_request_error",
                )
                raise AIClientError(
                    message="The AI provider could not be reached.",
                    error_code="ai_provider_request_error",
                ) from exc
            except (ValueError, ValidationError) as exc:
                raise AIClientError(
                    message="The AI provider returned an invalid prediction response.",
                    error_code="ai_provider_invalid_response",
                ) from exc
    finally:
        if owns_client:
            await active_client.aclose()

    raise AIClientError(
        message="The AI provider prediction request did not run.",
        error_code="ai_provider_request_error",
    )
