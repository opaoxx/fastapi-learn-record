from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .database import create_db_and_tables
from .routers import files, items, predictions, system, tasks
from .settings import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    create_db_and_tables()
    yield


settings = get_settings()
frontend_dir = Path(__file__).parent / "frontend"

allowed_origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]

app = FastAPI(
    title=settings.app_name,
    description="A tiny learning API for backend basics and future AI service endpoints.",
    version="0.1.0",
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
