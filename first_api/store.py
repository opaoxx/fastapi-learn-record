from fastapi import HTTPException, status

from .schemas import Item


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
