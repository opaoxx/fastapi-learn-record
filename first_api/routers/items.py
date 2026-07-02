from typing import Annotated

from fastapi import APIRouter, Depends, Path, status

from ..dependencies import ItemFilters, Pagination
from ..schemas import Item, ItemCreate
from ..store import ITEMS, get_item_or_404


router = APIRouter(prefix="/items", tags=["items"])


@router.get("", response_model=list[Item])
def list_items(
    filters: Annotated[ItemFilters, Depends(ItemFilters)],
    pagination: Annotated[Pagination, Depends(Pagination)],
) -> list[Item]:
    results = list(ITEMS.values())

    if filters.q is not None:
        keyword = filters.q.lower()
        results = [item for item in results if keyword in item.name.lower()]
    if filters.category is not None:
        results = [item for item in results if item.category == filters.category]
    if filters.max_price is not None:
        results = [item for item in results if item.price <= filters.max_price]
    if filters.in_stock is not None:
        results = [item for item in results if item.in_stock == filters.in_stock]

    return results[pagination.skip : pagination.skip + pagination.limit]


@router.get("/{item_id}", response_model=Item)
def read_item(
    item_id: Annotated[int, Path(ge=1, description="The numeric ID of the item.")]
) -> Item:
    return get_item_or_404(item_id)


@router.post("", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate) -> Item:
    next_id = max(ITEMS) + 1
    item = Item(id=next_id, **payload.model_dump())
    ITEMS[next_id] = item
    return item
