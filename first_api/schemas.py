from typing import Literal

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: Literal["ok"]
    service: str


class PredictionRequest(BaseModel):
    text: str = Field(
        min_length=3,
        max_length=500,
        examples=["FastAPI makes backend APIs pleasant."],
    )
    mode: Literal["fast", "careful"] = "fast"
    temperature: float = Field(default=0.2, ge=0, le=1)


class PredictionResponse(BaseModel):
    label: Literal["positive", "neutral"]
    score: float
    source: str
    text_length: int


ItemCategory = Literal["book", "course", "tool"]


class Item(BaseModel):
    id: int
    name: str
    category: ItemCategory
    price: float
    in_stock: bool


class ItemCreate(BaseModel):
    name: str = Field(min_length=2, max_length=80, examples=["FastAPI Project Notes"])
    category: ItemCategory = "course"
    price: float = Field(ge=0, examples=[29.9])
    in_stock: bool = True
