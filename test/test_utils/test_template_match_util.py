# pylint: disable=missing-function-docstring, unused-argument
from pytest import mark

from app.schemas import FieldType
from app.utils import get_field_type


@mark.parametrize(
    "value, field_type",
    [
        ('', FieldType.TEXT),
        ('+7 111 111 11 11', FieldType.PHONE),
        ('+8 111 111 11 11', FieldType.TEXT),
        ('01.01.2023', FieldType.DATE),
        ('31.02.2023', FieldType.TEXT),
        ('2023-12-12', FieldType.DATE),
        ('2023-30-30', FieldType.TEXT),
        ('example@mail.com', FieldType.EMAIL),
        ('xxx', FieldType.TEXT),
    ]
)
def test_template_match(field_type, value):
    assert field_type == get_field_type(value)
