from pytest import fixture
from bson import ObjectId

from app.db import collection


@fixture(scope='function')
def data(db):
    objects = [
        {
            'name': 'o1',
            'fields': [('f1', 'email'), ('f2', 'text'), ('f3', 'phone')],
        },
        {
            'name': 'o2',
            'fields': [('f1', 'email'), ('f2', 'date')],
        },
        {
            'name': 'o3',
            'fields': [('f1', 'text')],
        }
    ]
    inserted_ids = collection.insert_many(objects).inserted_ids
    for obj in objects:
        del obj['_id']
    yield [obj | {'id': str(_id)} for obj, _id in zip(objects, inserted_ids)]
    collection.delete_many({'_id': {'$in': inserted_ids}})


@fixture(scope='function')
def cleaner():
    cleanup_ids = []
    yield cleanup_ids
    collection.delete_many({'_id': {'$in': list(map(ObjectId, cleanup_ids))}})
