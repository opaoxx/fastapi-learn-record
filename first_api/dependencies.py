from typing import Annotated

from fastapi import Query

from .schemas import ItemCategory


class ItemFilters:
    def __init__(
        self,
        q: Annotated[str | None, Query(max_length=40)] = None,
        category: ItemCategory | None = None,
        max_price: Annotated[float | None, Query(ge=0)] = None,
        in_stock: bool | None = None,
    ) -> None:
        self.q = q
        self.category = category
        self.max_price = max_price
        self.in_stock = in_stock


class Pagination:
    def __init__(
        self,
        skip: Annotated[int, Query(ge=0)] = 0,
        limit: Annotated[int, Query(ge=1, le=50)] = 10,
    ) -> None:
        self.skip = skip
        self.limit = limit
