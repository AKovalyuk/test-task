from pytest import mark


@mark.parametrize(
    "page, size, excepted_count",
    [
        (None, None, 3),
        (1, 10, 3),
        (2, 10, 0),
        (1, 1, 1),
        (1, 2, 2),
        (2, 2, 1),
    ]
)
async def test_get_multiple(data, client, page, size, excepted_count):
    params = {}
    if page:
        params['page'] = page
    if size:
        params['size'] = size
    response = await client.get('/template', params=params)
    assert len(response.json()) == excepted_count
