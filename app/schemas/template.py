from typing import Dict, Literal, Any

from pydantic import BaseModel, Field, field_validator

FieldType = Literal["email", "phone", "date", "text"]


class TemplateMatchSuccess(BaseModel):
    id: str
    name: str


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
