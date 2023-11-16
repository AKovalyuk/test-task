from pytest import mark


@mark.parametrize(
    'new_template, excepted_status_code',
    [
        ({
            'name': '1',
            'fields': {'a': 'email', 'b': 'phone'}
        }, 201),
        ({
             'name': '2',
             'fields': {'a': 'not_email', 'b': 'phone'}
         }, 422),
        ({
             'name': '3',
             'fields': {'a': 'text', 'b': 'date'}
         }, 201),
        ({
             'name': '4',
             'fields': {}
         }, 201),
        ({
            'name': '5',
            'fields': {'a': 'email'}
        }, 201)
    ]
)
async def test_create(new_template, excepted_status_code, client, cleaner):
    response = await client.post('/template', json=new_template)
    assert response.status_code == excepted_status_code
    if response.status_code == 201:
        cleaner.append(response.json()['id'])
