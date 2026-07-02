from typing import Literal

from pydantic import BaseModel, Field as PydanticField
from sqlmodel import Field, SQLModel


class HealthResponse(BaseModel):
    status: Literal["ok"]
    service: str


class PredictionRequest(BaseModel):
    text: str = PydanticField(
        min_length=3,
        max_length=500,
        examples=["FastAPI makes backend APIs pleasant."],
    )
    mode: Literal["fast", "careful"] = "fast"
    temperature: float = PydanticField(default=0.2, ge=0, le=1)


class PredictionResponse(BaseModel):
    label: Literal["positive", "neutral"]
    score: float
    source: str
    text_length: int


ItemCategory = Literal["book", "course", "tool"]


class ItemBase(SQLModel):
    name: str
    category: str = Field(index=True)
    price: float = Field(ge=0)
    in_stock: bool


class Item(ItemBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class ItemCreate(ItemBase):
    name: str = Field(min_length=2, max_length=80, schema_extra={"examples": ["FastAPI Project Notes"]})
    category: ItemCategory = "course"
    price: float = Field(ge=0, schema_extra={"examples": [29.9]})
    in_stock: bool = True


class ItemRead(ItemBase):
    id: int
