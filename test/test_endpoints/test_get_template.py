# pylint: disable=missing-function-docstring, unused-argument
from pytest import mark
from bson import ObjectId


@mark.parametrize(
    "page, size, excepted_count",
    [
        (None, None, 3),
        (1, 10, 3),
        (2, 10, 0),
        (1, 1, 1),
        (1, 2, 2),
        (2, 2, 1),
        (-1, 2, None),
        (3, -5, None),
    ]
)
async def test_get_multiple(data, client, page, size, excepted_count):
    params = {}
    if page:
        params['page'] = page
    if size:
        params['size'] = size
    response = await client.get('/template', params=params)
    if (page and page < 1) or (size and size < 1):
        assert response.status_code == 422
    else:
        assert len(response.json()) == excepted_count


async def test_bad_id(data, client):
    response = await client.get('/template/fake_id')
    assert response.status_code == 422


async def test_not_found(data, client):
    response = await client.get(f'/template/{ObjectId()}')
    assert response.status_code == 404


@mark.parametrize(
    "index",
    [0, 1, 2]
)
async def test_get_one(data, client, index):
    response = await client.get(f'/template/{data[index]["id"]}')
    assert response.json()['id'] == data[index]['id']
    assert response.json()['fields'] == dict(data[index]['fields'])
