from typing import Annotated

from fastapi import Depends
from fastapi import APIRouter

from ..schemas import HealthResponse, PublicConfigResponse
from ..settings import Settings, get_settings


router = APIRouter(tags=["system"])


@router.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello FastAPI,and hello world"}


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status="ok", service="first-api")


@router.get("/config/public", response_model=PublicConfigResponse)
def read_public_config(
    settings: Annotated[Settings, Depends(get_settings)],
) -> PublicConfigResponse:
    return PublicConfigResponse(
        app_name=settings.app_name,
        environment=settings.environment,
        api_key_configured=bool(settings.api_key),
    )
