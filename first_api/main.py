from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from pathlib import Path

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .database import create_db_and_tables
from .routers import files, items, predictions, system, tasks
from .services.ai_clients import build_ai_client_config
from .settings import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    create_db_and_tables()
    ai_client_config = build_ai_client_config()
    app.state.provider_http_client = httpx.AsyncClient(
        timeout=ai_client_config.timeout_seconds,
        trust_env=False,
    )
    app.state.provider_http_client_provider = ai_client_config.provider
    app.state.provider_http_client_timeout_seconds = ai_client_config.timeout_seconds
    try:
        yield
    finally:
        await app.state.provider_http_client.aclose()


settings = get_settings()
frontend_dir = Path(__file__).parent / "frontend"

allowed_origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]

openapi_tags = [
    {
        "name": "system",
        "description": "Health checks and public runtime configuration.",
    },
    {
        "name": "items",
        "description": "Database-backed learning endpoints for CRUD and filtering.",
    },
    {
        "name": "predictions",
        "description": "Model-like synchronous endpoints for AI service practice.",
    },
    {
        "name": "tasks",
        "description": "Protected background summary tasks with status, filtering, and pagination.",
    },
    {
        "name": "files",
        "description": "Protected UTF-8 text uploads used as summary-task inputs.",
    },
]

app = FastAPI(
    title=settings.app_name,
    summary="A learning API that grows from backend basics into AI-service endpoints.",
    description="A tiny learning API for backend basics and future AI service endpoints.",
    version="0.1.0",
    openapi_tags=openapi_tags,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(system.router)
app.include_router(items.router)
app.include_router(predictions.router)
app.include_router(tasks.router)
app.include_router(files.router)

app.mount("/app", StaticFiles(directory=frontend_dir, html=True), name="frontend")
