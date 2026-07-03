from typing import Annotated

import httpx
from fastapi import Query, Request

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


def get_provider_http_client(request: Request) -> httpx.AsyncClient:
    return request.app.state.provider_http_client
