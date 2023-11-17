# pylint: disable=missing-class-docstring
from typing import Dict, Literal, Any, Annotated
from enum import Enum

from pydantic import BaseModel, Field, field_validator, AfterValidator
from bson import ObjectId as _ObjectId


def validate_object_id(value: str) -> str:
    """Функция для превращения строки в ObjectId"""
    if not _ObjectId.is_valid(value):
        raise ValueError('Invalid ObjectId')
    return value


class FieldType(str, Enum):
    DATE = 'date'
    PHONE = 'phone'
    EMAIL = 'email'
    TEXT = 'text'


ObjectId = Annotated[str, AfterValidator(validate_object_id)]


class TemplateMatchSuccess(BaseModel):
    id: str = Field(validation_alias='_id')
    name: str

    @field_validator('id', mode='before')
    @classmethod
    def transform_id(cls, v: Any) -> str:
        if not isinstance(v, str):
            v = str(v)
        return v


class TemplateIn(BaseModel):
    name: str
    fields: Dict[str, FieldType]


class TemplateOut(TemplateIn):
    id: str = Field(validation_alias='_id')

    @field_validator('id', mode='before')
    @classmethod
    def transform_id(cls, v: Any) -> str:
        if not isinstance(v, str):
            v = str(v)
        return v
