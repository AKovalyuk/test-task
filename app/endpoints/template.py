# pylint: disable=missing-function-docstring
from typing import Annotated

from fastapi import APIRouter, Path, Request, Depends, Body, HTTPException
from starlette import status

from app.dependencies import Pagination, pagination_dependency
from app.schemas import TemplateOut, TemplateIn, TemplateMatchSuccess, FieldType, ObjectId
from app.db import insert_object, get_object, get_objects, delete_object, collection, template_match
from app.utils import get_field_type


router = APIRouter(
    prefix='',
    tags=['Template']
)


@router.post(
    path='/get_form',
    status_code=status.HTTP_200_OK,
)
async def get_form(
        data: Annotated[dict[str, str], Body()]
) -> TemplateMatchSuccess | dict[str, FieldType]:
    """Endpoint для поиска подходящего шаблона"""
    # Получение типов полей
    field_types = {
        field_name: get_field_type(field_value)
        for field_name, field_value in data.items()
    }

    # Поиск подходящего шаблона в БД
    matched_template = template_match(list(field_types.items()), collection)

    if matched_template:
        return TemplateMatchSuccess(**matched_template)
    return field_types


@router.get(
    path='/template',
    status_code=status.HTTP_200_OK,
)
async def get_templates(
        pagination: Annotated[Pagination, Depends(pagination_dependency)],
) -> list[TemplateOut]:
    return [
        TemplateOut(**obj) for obj in
        get_objects(pagination.size, pagination.page, collection)
    ]


@router.get(
    path='/template/{template_id}',
    status_code=status.HTTP_200_OK,
)
async def get_template(
        template_id: Annotated[ObjectId, Path()],  # ObjectId
) -> TemplateOut:
    found_object = get_object(template_id, collection)
    if not found_object:
        raise HTTPException(status_code=404)
    return TemplateOut(**found_object)


@router.post(
    path='/template',
    status_code=status.HTTP_201_CREATED,
)
async def create_template(
        template_data: Annotated[TemplateIn, Body()],
) -> TemplateOut:
    inserted_id = insert_object(template_data.model_dump(), collection)
    return TemplateOut(_id=str(inserted_id), **template_data.model_dump())


@router.delete(
    path='/template/{template_id}',
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_template(
        template_id: Annotated[ObjectId, Path()],
):
    delete_object(template_id, collection)
