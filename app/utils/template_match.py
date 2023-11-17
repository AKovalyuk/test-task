from re import fullmatch
from datetime import datetime

from pydantic import validate_email
from pydantic_core import PydanticCustomError

from app.schemas import FieldType


def check_date(value: str) -> bool:
    """
    Функция проверки даты
    (сделал так, чтобы не пропускать неправильные даты например 31 февраля)
    """
    try:
        datetime.strptime(value, '%d.%m.%Y')
        return True
    except ValueError:
        ...
    try:
        datetime.strptime(value, '%Y-%m-%d')
        return True
    except ValueError:
        ...
    return False


def check_phone(value: str) -> bool:
    return fullmatch(r'\+7 \d{3} \d{3} \d{2} \d{2}', value) is not None


def check_email(value: str) -> bool:
    try:
        _ = validate_email(value)
        return True
    except PydanticCustomError:
        ...
    return False


FIELD_TYPE_PATTERN_PRIORITY = [
    (FieldType.DATE,  check_date),
    (FieldType.PHONE, check_phone),
    (FieldType.EMAIL, check_email),
    (FieldType.TEXT,  lambda value: True),
]


def get_field_type(value: str) -> FieldType:
    for field_type, checker_function in FIELD_TYPE_PATTERN_PRIORITY:
        if checker_function(value):
            return field_type
