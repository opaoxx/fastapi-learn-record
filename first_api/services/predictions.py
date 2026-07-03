from dataclasses import dataclass
from time import perf_counter
from typing import Literal

import httpx

from ..settings import Settings
from .ai_clients import AIClient, AIClientConfig, AIClientError, PredictionResult
from .provider_http import request_provider_prediction


PredictionBackend = Literal["demo", "provider"]


@dataclass(frozen=True)
class PredictionServiceResult:
    prediction: PredictionResult
    backend: PredictionBackend
    elapsed_ms: float


class PredictionServiceError(Exception):
    def __init__(
        self,
        message: str,
        error_code: str,
        backend: PredictionBackend,
        elapsed_ms: float,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.backend = backend
        self.elapsed_ms = elapsed_ms


async def run_prediction(
    text: str,
    mode: str,
    settings: Settings,
    ai_client: AIClient,
    provider_http_client: httpx.AsyncClient,
    backend: PredictionBackend | None = None,
) -> PredictionServiceResult:
    active_backend = backend or settings.ai_prediction_backend
    started_at = perf_counter()

    try:
        if active_backend == "provider":
            config = AIClientConfig(
                provider=settings.ai_provider,
                timeout_seconds=settings.ai_timeout_seconds,
                max_attempts=settings.ai_max_attempts,
                retry_base_delay_seconds=settings.ai_retry_base_delay_seconds,
                retry_max_delay_seconds=settings.ai_retry_max_delay_seconds,
                retry_jitter_seconds=settings.ai_retry_jitter_seconds,
            )
            prediction = await request_provider_prediction(
                url=settings.ai_provider_prediction_url,
                text=text,
                mode=mode,
                config=config,
                client=provider_http_client,
            )
        else:
            prediction = ai_client.predict_sentiment(text, mode)
    except AIClientError as exc:
        elapsed_ms = (perf_counter() - started_at) * 1000
        raise PredictionServiceError(
            message=exc.message,
            error_code=exc.error_code,
            backend=active_backend,
            elapsed_ms=elapsed_ms,
        ) from exc

    elapsed_ms = (perf_counter() - started_at) * 1000
    return PredictionServiceResult(
        prediction=prediction,
        backend=active_backend,
        elapsed_ms=elapsed_ms,
    )
