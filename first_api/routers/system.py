import asyncio
from typing import Annotated

import httpx
from fastapi import APIRouter, HTTPException
from fastapi import Depends, Query, Request

from ..dependencies import get_provider_http_client
from ..schemas import (
    AsyncWaitResponse,
    ErrorDetail,
    ErrorResponse,
    HealthResponse,
    ProviderHealthResponse,
    ProviderHttpClientStateResponse,
    PublicConfigResponse,
)
from ..services.ai_clients import AIClientConfig, AIClientError
from ..services.provider_http import check_provider_health
from ..settings import Settings, get_settings


router = APIRouter(tags=["system"])


@router.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello FastAPI,and hello world"}


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status="ok", service="first-api")


@router.get(
    "/async/wait",
    response_model=AsyncWaitResponse,
    summary="Demonstrate non-blocking async waiting",
    description=(
        "Waits with asyncio.sleep to demonstrate an async path operation. "
        "This models waiting for external I/O without blocking the event loop."
    ),
)
async def async_wait(
    delay: Annotated[
        float,
        Query(
            ge=0,
            le=1,
            description="Seconds to await. Kept small so the learning endpoint stays safe.",
        ),
    ] = 0.05,
) -> AsyncWaitResponse:
    await asyncio.sleep(delay)
    return AsyncWaitResponse(
        status="ok",
        delay_seconds=delay,
        message="The endpoint awaited without doing CPU work.",
    )


@router.get(
    "/provider/http-client",
    response_model=ProviderHttpClientStateResponse,
    summary="Inspect the lifespan-managed provider HTTP client",
    description=(
        "Shows whether the application-level HTTP client for provider calls was created "
        "during FastAPI lifespan startup."
    ),
)
def read_provider_http_client_state(
    request: Request,
    provider_http_client: Annotated[httpx.AsyncClient, Depends(get_provider_http_client)],
) -> ProviderHttpClientStateResponse:
    return ProviderHttpClientStateResponse(
        provider=request.app.state.provider_http_client_provider,
        timeout_seconds=request.app.state.provider_http_client_timeout_seconds,
        client_ready=not provider_http_client.is_closed,
    )


@router.get(
    "/provider/health",
    response_model=ProviderHealthResponse,
    responses={503: {"model": ErrorResponse}},
    summary="Check the configured AI provider health URL",
    description=(
        "Calls the configured provider health URL with the lifespan-managed HTTP client. "
        "Provider timeouts, HTTP errors, and request errors are mapped to a stable 503 response."
    ),
)
async def read_provider_health(
    settings: Annotated[Settings, Depends(get_settings)],
    provider_http_client: Annotated[httpx.AsyncClient, Depends(get_provider_http_client)],
) -> ProviderHealthResponse:
    config = AIClientConfig(
        provider=settings.ai_provider,
        timeout_seconds=settings.ai_timeout_seconds,
        max_attempts=settings.ai_max_attempts,
    )

    try:
        result = await check_provider_health(
            url=settings.ai_provider_health_url,
            config=config,
            client=provider_http_client,
        )
    except AIClientError as exc:
        raise HTTPException(
            status_code=503,
            detail=ErrorDetail(error_code=exc.error_code, message=exc.message).model_dump(),
        ) from exc

    return ProviderHealthResponse(
        ok=result.ok,
        provider=result.provider,
        status_code=result.status_code,
        message=result.message,
    )


@router.get("/config/public", response_model=PublicConfigResponse)
def read_public_config(
    settings: Annotated[Settings, Depends(get_settings)],
) -> PublicConfigResponse:
    return PublicConfigResponse(
        app_name=settings.app_name,
        environment=settings.environment,
        api_key_configured=bool(settings.api_key),
    )
