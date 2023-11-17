# pylint: disable=missing-function-docstring, unused-argument
from pytest import mark


@mark.parametrize(
    "query, excepted_status_code, excepted_name",
    [
        ({'f1': 'a@mail.ru', 'f2': 'text', 'f3': '+7 111 111 11 11'}, 200, 'o1'),
        ({'f1': 'b@gmail.com', 'f2': '29.02.2004', 'f3': 'text'}, 200, 'o2'),
        ({'f1': 'text', 'f2': 'a@mail.ru'}, 200, 'o3'),
    ]
)
async def test_template_match_endpoint_db(data, client, query, excepted_status_code, excepted_name):
    response = await client.post('/get_form', json=query)
    assert response.status_code == excepted_status_code
    assert excepted_name == response.json()['name']


@mark.parametrize(
    "query, excepted_types, excepted_status_code",
    [
        ({'f1': '+7 111 111 11 11', 'f2': 'xxx', 'f3': '2000-10-10'},
         {'f1': 'phone', 'f2': 'text', 'f3': 'date'}, 200),
        ({'x1': 'textex', 'x2': '20.10.2010', 'x3': '+7 000 000 00 00', 'x4': 'a.x@gx.com'},
         {'x1': 'text', 'x2': 'date', 'x3': 'phone', 'x4': 'email'}, 200),
        ({}, {}, 200),

    ]
)
async def test_template_match(data, client, query, excepted_status_code, excepted_types):
    response = await client.post('/get_form', json=query)
    # assert response.json() == {}
    assert response.status_code == excepted_status_code
    assert response.json() == excepted_types
