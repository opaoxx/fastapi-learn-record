from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title="First FastAPI API",
    description="A tiny learning API for backend basics and future AI service endpoints.",
    version="0.1.0",
)


class HealthResponse(BaseModel):
    status: Literal["ok"]
    service: str


class PredictionRequest(BaseModel):
    text: str = Field(min_length=1, examples=["FastAPI makes backend APIs pleasant."])


class PredictionResponse(BaseModel):
    label: Literal["positive", "neutral"]
    score: float
    source: str


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello FastAPI,and hello world"}


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status="ok", service="first-api")


@app.post("/predict", response_model=PredictionResponse)
def predict(payload: PredictionRequest) -> PredictionResponse:
    positive_words = {"good", "great", "love", "pleasant", "nice", "happy"}
    tokens = {word.strip(".,!?;:").lower() for word in payload.text.split()}
    is_positive = bool(tokens & positive_words)

    return PredictionResponse(
        label="positive" if is_positive else "neutral",
        score=0.91 if is_positive else 0.55,
        source="rule-based-demo",
    )
