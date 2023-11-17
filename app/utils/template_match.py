"""
Модуль с бизнес-логикой получения типа поля
"""

from re import fullmatch
from datetime import datetime

from pydantic import validate_email
from pydantic_core import PydanticCustomError

from app.schemas import FieldType


def check_date(value: str) -> bool:
    """
    Функция проверки даты
    (сделал с datetime чтобы не пропускать неправильные даты например 31 февраля)
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
    """Проверка телефона через re"""
    return fullmatch(r'\+7 \d{3} \d{3} \d{2} \d{2}', value) is not None


def check_email(value: str) -> bool:
    """Проверка email с помощью Pydantic"""
    try:
        _ = validate_email(value)
        return True
    except PydanticCustomError:
        ...
    return False


# Список с типами полей и функциями проверки
# Порядок в списке задает порядок проверки
FIELD_TYPE_PATTERN_PRIORITY = [
    (FieldType.DATE,  check_date),
    (FieldType.PHONE, check_phone),
    (FieldType.EMAIL, check_email),
    (FieldType.TEXT,  lambda value: True),  # Если другие не подходят - будет выбран тип TEXT
]


def get_field_type(value: str) -> FieldType:
    """
    Функция определения типа поля
    Проходит по FIELD_TYPE_PATTERN_PRIORITY, возвращает первое подходящее поле

    :param value: Значение поля
    :return: Тип поля (Enum)
    """
    for field_type, checker_function in FIELD_TYPE_PATTERN_PRIORITY:
        if checker_function(value):
            return field_type
