from typing import Dict, Literal, Any, Annotated

from pydantic import BaseModel, Field, field_validator, AfterValidator
from bson import ObjectId as _ObjectId


def validate_object_id(value: str) -> str:
    if not _ObjectId.is_valid(value):
        raise ValueError('Invalid ObjectId')
    return value


FieldType = Literal["email", "phone", "date", "text"]
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
