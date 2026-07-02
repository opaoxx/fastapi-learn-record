from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator

from fastapi import FastAPI

from .database import create_db_and_tables
from .routers import items, predictions, system, tasks
from .settings import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    create_db_and_tables()
    yield


settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description="A tiny learning API for backend basics and future AI service endpoints.",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(system.router)
app.include_router(items.router)
app.include_router(predictions.router)
app.include_router(tasks.router)
