from pytest import mark


@mark.parametrize(
    "query, excepted_status_code, found_in_db",
    [
        ([('f1', 'email'), ('f2', 'date')], 200, True),
        ([('f1', 'email'), ('f2', 'date'), ('f3', 'text')], 200, True),
        ([('f1', 'text'), ('f2', 'email')], 200, True),
    ]
)
async def test_template_match(data, client, query, excepted_status_code, found_in_db):
    response = await client.post('/get_form', params=query)
    assert response.status_code == excepted_status_code
    if found_in_db:
        found_id = response.json()['id']
        found_object = next(filter(lambda o: o['id'] == found_id, data))
        assert set(query) >= set(found_object['fields'])
    else:
        ...
