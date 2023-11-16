from pytest import mark
from bson import ObjectId


@mark.parametrize(
    'index',
    [0, 1, 2],
)
async def test_delete(data, client, index):
    response = await client.delete(f'/template/{data[index]["id"]}')
    assert response.status_code == 204
    confirm_response = await client.get(f'/template/{data[index]["id"]}')
    assert confirm_response.status_code == 404


async def test_delete_not_found(data, client):
    response = await client.delete(f'/template/{ObjectId()}')
    assert response.status_code == 204


async def test_delete_bad_id(data, client):
    response = await client.delete('/template/xxx')
    assert response.status_code == 422
