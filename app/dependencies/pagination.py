from dataclasses import dataclass
from typing import Annotated

from fastapi import Query


@dataclass
class Pagination:
    """
    Класс, представляющий позицию пагинации
    """
    page: int
    size: int


async def pagination_dependency(
        page: Annotated[int, Query(ge=1)] = 1,
        size: Annotated[int, Query(ge=1)] = 50,
):
    """
    Зависимость для извлечения пагинации из Query-параметров
    """
    return Pagination(page=page, size=size)
