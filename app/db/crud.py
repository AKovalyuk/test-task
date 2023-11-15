from pymongo.client_session import ClientSession
from pymongo.collection import Collection


def insert_object(obj: dict, session: ClientSession, collection: Collection):
    with session.start_transaction():
        return collection.insert_one(obj, session=session).inserted_id


def delete_object(object_id: str, session: ClientSession, collection: Collection):
    with session.start_transaction():
        collection.delete_one({"_id": object_id}, session=session)


def get_object(object_id: str, session: ClientSession, collection: Collection):
    with session.start_transaction():
        return collection.find_one({"_id": object_id})


def get_objects(page_size: int, page_number: int, session: ClientSession, collection: Collection):
    with session.start_transaction():
        return collection.find({}).limit(page_size).limit((page_number - 1) * page_size)
