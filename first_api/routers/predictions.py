import logging
from time import perf_counter
from typing import Annotated

import httpx
from fastapi import APIRouter, Depends, HTTPException, Response, status

from ..dependencies import get_provider_http_client
from ..schemas import ErrorResponse, PredictionRequest, PredictionResponse
from ..services.ai_clients import AIClient, AIClientConfig, AIClientError, PredictionResult, get_ai_client
from ..services.provider_http import request_provider_prediction
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
    started_at = perf_counter()
    backend = settings.ai_prediction_backend

    try:
        if backend == "provider":
            config = AIClientConfig(
                provider=settings.ai_provider,
                timeout_seconds=settings.ai_timeout_seconds,
                max_attempts=settings.ai_max_attempts,
            )
            prediction = await request_provider_prediction(
                url=settings.ai_provider_prediction_url,
                text=payload.text,
                mode=payload.mode,
                config=config,
                client=provider_http_client,
            )
        else:
            prediction = ai_client.predict_sentiment(payload.text, payload.mode)
    except AIClientError as exc:
        elapsed_ms = (perf_counter() - started_at) * 1000
        logger.warning(
            "prediction_failed",
            extra={
                "prediction_backend": backend,
                "prediction_elapsed_ms": round(elapsed_ms, 2),
                "prediction_error_code": exc.error_code,
            },
        )
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "error_code": exc.error_code,
                "message": exc.message,
            },
            headers=build_prediction_headers(
                backend=backend,
                elapsed_ms=elapsed_ms,
                error_code=exc.error_code,
            ),
        ) from exc

    elapsed_ms = (perf_counter() - started_at) * 1000
    set_prediction_headers(
        response=response,
        backend=backend,
        elapsed_ms=elapsed_ms,
        source=prediction.source,
    )
    logger.info(
        "prediction_completed",
        extra={
            "prediction_backend": backend,
            "prediction_source": prediction.source,
            "prediction_elapsed_ms": round(elapsed_ms, 2),
        },
    )

    return build_prediction_response(prediction, payload.text)


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
    provider_http_client: Annotated[httpx.AsyncClient, Depends(get_provider_http_client)],
) -> PredictionResponse:
    started_at = perf_counter()
    backend = "provider"
    config = AIClientConfig(
        provider=settings.ai_provider,
        timeout_seconds=settings.ai_timeout_seconds,
        max_attempts=settings.ai_max_attempts,
    )

    try:
        prediction = await request_provider_prediction(
            url=settings.ai_provider_prediction_url,
            text=payload.text,
            mode=payload.mode,
            config=config,
            client=provider_http_client,
        )
    except AIClientError as exc:
        elapsed_ms = (perf_counter() - started_at) * 1000
        logger.warning(
            "prediction_failed",
            extra={
                "prediction_backend": backend,
                "prediction_elapsed_ms": round(elapsed_ms, 2),
                "prediction_error_code": exc.error_code,
            },
        )
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "error_code": exc.error_code,
                "message": exc.message,
            },
            headers=build_prediction_headers(
                backend=backend,
                elapsed_ms=elapsed_ms,
                error_code=exc.error_code,
            ),
        ) from exc

    elapsed_ms = (perf_counter() - started_at) * 1000
    set_prediction_headers(
        response=response,
        backend=backend,
        elapsed_ms=elapsed_ms,
        source=prediction.source,
    )
    logger.info(
        "prediction_completed",
        extra={
            "prediction_backend": backend,
            "prediction_source": prediction.source,
            "prediction_elapsed_ms": round(elapsed_ms, 2),
        },
    )

    return build_prediction_response(prediction, payload.text)
