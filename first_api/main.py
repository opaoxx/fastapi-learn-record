from fastapi import FastAPI

from .routers import items, predictions, system


app = FastAPI(
    title="First FastAPI API",
    description="A tiny learning API for backend basics and future AI service endpoints.",
    version="0.1.0",
)

app.include_router(system.router)
app.include_router(items.router)
app.include_router(predictions.router)
