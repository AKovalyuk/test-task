from pymongo.collection import Collection
from bson.objectid import ObjectId


def insert_object(obj: dict, collection: Collection):
    """Вставка объекта в коллекцию"""
    obj['fields'] = list(obj['fields'].items())
    return collection.insert_one(obj).inserted_id


def delete_object(object_id: str, collection: Collection):
    """Удаление объекта из коллекции"""
    collection.delete_one({"_id": ObjectId(object_id)})


def get_object(object_id: str, collection: Collection):
    """Получение объекта из коллекции по id"""
    obj = collection.find_one({"_id": ObjectId(object_id)})
    if obj is not None:
        obj['fields'] = dict(obj['fields'])
    return obj


def get_objects(
        page_size: int,
        page_number: int,
        collection: Collection
) -> list[dict]:
    """
    Получение объектов из коллекции
    :param page_size: Размер страницы
    :param page_number: Номер страницы
    :param collection: Коллекция MongoDB
    :return: Список объектов
    """
    result = []
    for obj in collection.find({}).limit(page_size).skip((page_number - 1) * page_size):
        obj['fields'] = dict(obj['fields'])
        result.append(obj)
    return result
