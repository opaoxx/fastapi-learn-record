from fastapi import APIRouter

from ..schemas import HealthResponse


router = APIRouter(tags=["system"])


@router.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello FastAPI,and hello world"}


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status="ok", service="first-api")
