from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlmodel import Session, select

from ..database import get_session
from ..dependencies import ItemFilters, Pagination
from ..schemas import Item, ItemCreate, ItemRead


router = APIRouter(prefix="/items", tags=["items"])


@router.get("", response_model=list[ItemRead])
def list_items(
    filters: Annotated[ItemFilters, Depends(ItemFilters)],
    pagination: Annotated[Pagination, Depends(Pagination)],
    session: Annotated[Session, Depends(get_session)],
) -> list[Item]:
    statement = select(Item)
    items = list(session.exec(statement))

    if filters.q is not None:
        keyword = filters.q.lower()
        items = [item for item in items if keyword in item.name.lower()]
    if filters.category is not None:
        items = [item for item in items if item.category == filters.category]
    if filters.max_price is not None:
        items = [item for item in items if item.price <= filters.max_price]
    if filters.in_stock is not None:
        items = [item for item in items if item.in_stock == filters.in_stock]

    return items[pagination.skip : pagination.skip + pagination.limit]


@router.get("/{item_id}", response_model=ItemRead)
def read_item(
    item_id: Annotated[int, Path(ge=1, description="The numeric ID of the item.")],
    session: Annotated[Session, Depends(get_session)],
) -> Item:
    item = session.get(Item, item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item {item_id} was not found.")
    return item


@router.post("", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create_item(
    payload: ItemCreate,
    session: Annotated[Session, Depends(get_session)],
) -> Item:
    item = Item.model_validate(payload)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item
