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
    response_model=TemplateMatchSuccess | dict[str, FieldType],
)
async def get_form(request: Request):
    for _, param_value in request.query_params.items():
        if not FieldType.contains(param_value):
            raise HTTPException(status_code=422)
    obj = template_match(list(request.query_params.items()), collection)
    if obj:
        return TemplateMatchSuccess(**obj)
    return {
        field_name: get_field_type(field_value)
        for field_name, field_value in request.query_params.items()
    }


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
