from typing import Literal

from pydantic import BaseModel, Field as PydanticField
from sqlmodel import Field, SQLModel


class HealthResponse(BaseModel):
    status: Literal["ok"]
    service: str


class PublicConfigResponse(BaseModel):
    app_name: str
    environment: str
    api_key_configured: bool


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


TaskStatus = Literal["queued", "running", "completed", "failed"]


class SummaryRequest(BaseModel):
    text: str = PydanticField(
        min_length=10,
        max_length=2000,
        examples=[
            "FastAPI background tasks are useful when an API should accept work quickly and finish processing after the response."
        ],
    )


class SummaryTask(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    text: str
    text_length: int
    status: str = Field(default="queued", index=True)
    result: str | None = None
    error: str | None = None


class SummaryTaskRead(SQLModel):
    id: int
    text_length: int
    status: str
    result: str | None = None
    error: str | None = None


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


class ItemUpdate(SQLModel):
    name: str | None = Field(default=None, min_length=2, max_length=80)
    category: ItemCategory | None = None
    price: float | None = Field(default=None, ge=0)
    in_stock: bool | None = None


class ItemRead(ItemBase):
    id: int
