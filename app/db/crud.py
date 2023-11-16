from pymongo.collection import Collection
from pymongo.cursor import Cursor
from bson.objectid import ObjectId


def insert_object(obj: dict, collection: Collection):
    obj['fields'] = [(key, value) for key, value in obj['fields'].items()]
    return collection.insert_one(obj).inserted_id


def delete_object(object_id: str, collection: Collection):
    collection.delete_one({"_id": ObjectId(object_id)})


def get_object(object_id: str, collection: Collection):
    obj = collection.find_one({"_id": ObjectId(object_id)})
    if obj is not None:
        obj['fields'] = {key: value for key, value in obj['fields']}
    return obj


def get_objects(
        page_size: int,
        page_number: int,
        collection: Collection
) -> list[dict]:
    result = []
    for obj in collection.find({}).limit(page_size).skip((page_number - 1) * page_size):
        obj['fields'] = {key: value for key, value in obj['fields']}
        result.append(obj)
    return result
