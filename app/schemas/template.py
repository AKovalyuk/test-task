from typing import Dict, Literal

from pydantic import BaseModel


FieldType = Literal["email", "phone", "date", "text"]


class TemplateMatchSuccess(BaseModel):
    id: str
    name: str


class TemplateIn(BaseModel):
    name: str
    fields: Dict[str, FieldType]


class TemplateOut(TemplateIn):
    id: str
