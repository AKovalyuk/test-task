from pymongo.collection import Collection
from pymongo.cursor import Cursor
from bson.objectid import ObjectId


def insert_object(obj: dict, collection: Collection):
    return collection.insert_one(obj).inserted_id


def delete_object(object_id: str, collection: Collection):
    collection.delete_one({"_id": ObjectId(object_id)})


def get_object(object_id: str, collection: Collection):
    return collection.find_one({"_id": ObjectId(object_id)})


def get_objects(
        page_size: int,
        page_number: int,
        collection: Collection
) -> Cursor:
    return collection.find({}).limit(page_size).limit((page_number - 1) * page_size)
