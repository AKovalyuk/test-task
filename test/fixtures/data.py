from pytest import fixture

from app.db import collection


@fixture(scope='session')
def data(db):
    objects = [
        {
            'name': 'o1',
            'fields': {'f1': 'email', 'f2': 'text', 'f3': 'phone'},
        },
        {
            'name': 'o2',
            'fields': {'f4': 'email', 'f5': 'date'},
        },
        {
            'name': 'o3',
            'fields': {'f6': 'text'},
        }
    ]
    inserted_ids = collection.insert_many(objects).inserted_ids
    return [obj | {'id': _id} for obj, _id in zip(objects, inserted_ids)]
