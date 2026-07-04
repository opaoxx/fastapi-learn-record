import logging
from typing import Annotated

import httpx
from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.responses import PlainTextResponse

from ..dependencies import get_provider_http_client
from ..schemas import (
    ErrorResponse,
    PredictionRequest,
    PredictionResponse,
    ProviderMetricSampleResponse,
)
from ..services.ai_clients import AIClient, PredictionResult, get_ai_client
from ..services.predictions import PredictionServiceError, PredictionServiceResult, run_prediction
from ..services.provider_http import (
    get_provider_metrics_prometheus_text,
    get_provider_metrics_snapshot,
)
from ..settings import Settings, get_settings


router = APIRouter(tags=["predictions"])
logger = logging.getLogger(__name__)


def build_prediction_response(prediction: PredictionResult, text: str) -> PredictionResponse:
    return PredictionResponse(
        label=prediction.label,
        score=prediction.score,
        source=prediction.source,
        text_length=len(text),
    )


def build_prediction_headers(
    backend: str,
    elapsed_ms: float,
    source: str | None = None,
    error_code: str | None = None,
) -> dict[str, str]:
    headers = {
        "X-Prediction-Backend": backend,
        "X-Prediction-Elapsed-Ms": f"{elapsed_ms:.2f}",
    }
    if source is not None:
        headers["X-Prediction-Source"] = source
    if error_code is not None:
        headers["X-Prediction-Error-Code"] = error_code
    return headers


def set_prediction_headers(
    response: Response,
    backend: str,
    elapsed_ms: float,
    source: str | None = None,
) -> None:
    for name, value in build_prediction_headers(
        backend=backend,
        elapsed_ms=elapsed_ms,
        source=source,
    ).items():
        response.headers[name] = value


def log_prediction_completed(result: PredictionServiceResult) -> None:
    logger.info(
        "prediction_completed",
        extra={
            "prediction_backend": result.backend,
            "prediction_source": result.prediction.source,
            "prediction_elapsed_ms": round(result.elapsed_ms, 2),
        },
    )


def log_prediction_failed(error: PredictionServiceError) -> None:
    logger.warning(
        "prediction_failed",
        extra={
            "prediction_backend": error.backend,
            "prediction_elapsed_ms": round(error.elapsed_ms, 2),
            "prediction_error_code": error.error_code,
        },
    )


@router.post(
    "/predict",
    response_model=PredictionResponse,
    responses={status.HTTP_503_SERVICE_UNAVAILABLE: {"model": ErrorResponse}},
)
async def predict(
    payload: PredictionRequest,
    response: Response,
    settings: Annotated[Settings, Depends(get_settings)],
    ai_client: Annotated[AIClient, Depends(get_ai_client)],
    provider_http_client: Annotated[httpx.AsyncClient, Depends(get_provider_http_client)],
) -> PredictionResponse:
    try:
        result = await run_prediction(
            text=payload.text,
            mode=payload.mode,
            settings=settings,
            ai_client=ai_client,
            provider_http_client=provider_http_client,
        )
    except PredictionServiceError as exc:
        log_prediction_failed(exc)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "error_code": exc.error_code,
                "message": exc.message,
            },
            headers=build_prediction_headers(
                backend=exc.backend,
                elapsed_ms=exc.elapsed_ms,
                error_code=exc.error_code,
            ),
        ) from exc

    set_prediction_headers(
        response=response,
        backend=result.backend,
        elapsed_ms=result.elapsed_ms,
        source=result.prediction.source,
    )
    log_prediction_completed(result)

    return build_prediction_response(result.prediction, payload.text)


@router.post(
    "/provider/predict",
    response_model=PredictionResponse,
    responses={status.HTTP_503_SERVICE_UNAVAILABLE: {"model": ErrorResponse}},
    summary="Call the configured AI provider prediction endpoint",
    description=(
        "Sends the prediction request to the configured provider prediction URL with the "
        "lifespan-managed HTTP client, then maps the provider result back to the stable "
        "PredictionResponse contract."
    ),
)
async def predict_with_provider(
    payload: PredictionRequest,
    response: Response,
    settings: Annotated[Settings, Depends(get_settings)],
    ai_client: Annotated[AIClient, Depends(get_ai_client)],
    provider_http_client: Annotated[httpx.AsyncClient, Depends(get_provider_http_client)],
) -> PredictionResponse:
    try:
        result = await run_prediction(
            text=payload.text,
            mode=payload.mode,
            settings=settings,
            ai_client=ai_client,
            provider_http_client=provider_http_client,
            backend="provider",
        )
    except PredictionServiceError as exc:
        log_prediction_failed(exc)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "error_code": exc.error_code,
                "message": exc.message,
            },
            headers=build_prediction_headers(
                backend=exc.backend,
                elapsed_ms=exc.elapsed_ms,
                error_code=exc.error_code,
            ),
        ) from exc

    set_prediction_headers(
        response=response,
        backend=result.backend,
        elapsed_ms=result.elapsed_ms,
        source=result.prediction.source,
    )
    log_prediction_completed(result)

    return build_prediction_response(result.prediction, payload.text)


@router.get(
    "/provider/metrics",
    response_model=list[ProviderMetricSampleResponse],
    summary="Read teaching provider prediction metrics",
    description=(
        "Returns the current in-process provider prediction metric counter snapshot. "
        "This endpoint is for teaching metric shape and FastAPI response modeling, not "
        "for production multi-instance aggregation."
    ),
)
async def get_provider_metrics() -> list[dict[str, object]]:
    return get_provider_metrics_snapshot()


@router.get(
    "/provider/metrics/prometheus",
    response_class=PlainTextResponse,
    summary="Read teaching provider prediction metrics as text",
    description=(
        "Returns a Prometheus text-style rendering of the current in-process provider "
        "prediction metric counter. This is an educational export shape, not a "
        "production multi-instance metrics pipeline."
    ),
)
async def get_provider_metrics_prometheus() -> str:
    return get_provider_metrics_prometheus_text()
