from typing import Annotated, Literal

from fastapi import FastAPI, HTTPException, Path, Query, status
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


ITEMS: dict[int, Item] = {
    1: Item(id=1, name="FastAPI Beginner Course", category="course", price=0, in_stock=True),
    2: Item(id=2, name="Python Backend Handbook", category="book", price=39.9, in_stock=True),
    3: Item(id=3, name="API Debug Toolkit", category="tool", price=19.9, in_stock=False),
}


def get_item_or_404(item_id: int) -> Item:
    item = ITEMS.get(item_id)
    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item {item_id} was not found.",
        )
    return item


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello FastAPI,and hello world"}


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(status="ok", service="first-api")


@app.get("/items", response_model=list[Item])
def list_items(
    q: Annotated[str | None, Query(max_length=40)] = None,
    category: ItemCategory | None = None,
    max_price: Annotated[float | None, Query(ge=0)] = None,
    in_stock: bool | None = None,
) -> list[Item]:
    results = list(ITEMS.values())

    if q is not None:
        keyword = q.lower()
        results = [item for item in results if keyword in item.name.lower()]
    if category is not None:
        results = [item for item in results if item.category == category]
    if max_price is not None:
        results = [item for item in results if item.price <= max_price]
    if in_stock is not None:
        results = [item for item in results if item.in_stock == in_stock]

    return results


@app.get("/items/{item_id}", response_model=Item)
def read_item(
    item_id: Annotated[int, Path(ge=1, description="The numeric ID of the item.")]
) -> Item:
    return get_item_or_404(item_id)


@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate) -> Item:
    next_id = max(ITEMS) + 1
    item = Item(id=next_id, **payload.model_dump())
    ITEMS[next_id] = item
    return item


@app.post("/predict", response_model=PredictionResponse)
def predict(payload: PredictionRequest) -> PredictionResponse:
    positive_words = {"good", "great", "love", "pleasant", "nice", "happy"}
    tokens = {word.strip(".,!?;:").lower() for word in payload.text.split()}
    is_positive = bool(tokens & positive_words)
    careful_bonus = 0.04 if payload.mode == "careful" else 0.0

    score = (0.91 if is_positive else 0.55) + careful_bonus

    return PredictionResponse(
        label="positive" if is_positive else "neutral",
        score=round(score, 2),
        source="rule-based-demo",
        text_length=len(payload.text),
    )
