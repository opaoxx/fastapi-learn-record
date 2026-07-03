from dataclasses import dataclass

import httpx
from pydantic import BaseModel, Field, ValidationError

from .ai_clients import AIClientConfig, AIClientError, PredictionLabel, PredictionResult


@dataclass(frozen=True)
class ProviderHealthResult:
    ok: bool
    provider: str
    status_code: int
    message: str


class ProviderPredictionPayload(BaseModel):
    text: str
    mode: str


class ProviderPredictionBody(BaseModel):
    label: PredictionLabel
    score: float = Field(ge=0, le=1)


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
) -> PredictionResult:
    owns_client = client is None
    active_client = client or httpx.AsyncClient(
        timeout=config.timeout_seconds,
        trust_env=False,
    )

    try:
        response = await active_client.post(
            url,
            json=ProviderPredictionPayload(text=text, mode=mode).model_dump(),
        )
        response.raise_for_status()
        body = ProviderPredictionBody.model_validate(response.json())
    except httpx.TimeoutException as exc:
        raise AIClientError(
            message="The AI provider prediction request timed out.",
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
    except (ValueError, ValidationError) as exc:
        raise AIClientError(
            message="The AI provider returned an invalid prediction response.",
            error_code="ai_provider_invalid_response",
        ) from exc
    finally:
        if owns_client:
            await active_client.aclose()

    return PredictionResult(
        label=body.label,
        score=round(body.score, 2),
        source=f"{config.provider}-provider",
    )
