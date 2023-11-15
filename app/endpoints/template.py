from typing import Annotated

from fastapi import APIRouter, Path, Query, Request, Depends, Body
from starlette import status

from app.dependencies import Pagination, pagination_dependency
from app.schemas import TemplateOut, TemplateIn, TemplateMatchSuccess, FieldType


router = APIRouter(
    prefix='',
    tags=['Template']
)


@router.post(
    path='/get_form',
    status_code=status.HTTP_200_OK,
    response_model=TemplateMatchSuccess | dict[str, FieldType],
)
async def get_form(request: Request):
    ...


@router.get(
    path='/template',
    status_code=status.HTTP_200_OK,
)
async def get_templates(
        pagination: Annotated[Pagination, Depends(pagination_dependency)],
) -> list[TemplateOut]:
    ...


@router.get(
    path='/template/{template_id}',
    status_code=status.HTTP_200_OK,
)
async def get_template(
        template_id: Annotated[str, Path()],  # ObjectId
) -> TemplateOut:
    ...


@router.post(
    path='/template',
    status_code=status.HTTP_201_CREATED,
)
async def create_template(
        template_data: Annotated[TemplateIn, Body()],
) -> TemplateOut:
    ...


@router.delete(
    path='/{template_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_template(
        template_id: Annotated[str, Path()],
):
    ...
