from typing import Optional

from pymongo.collection import Collection


def template_match(fields: list[tuple[str, str]], collection: Collection) -> Optional[dict]:
    """
    Функция для поиска шаблонов форм с полями, входящими в запрос
    :param fields: Поля в запросе
    :param collection: Коллекция MongoDB
    :return: Объект или None, если не был найден
    """
    result = collection.aggregate(
        [
            {
                "$match": {
                    "$expr": {
                        "$setIsSubset": ["$fields", fields],
                    }
                }
            },
            {"$limit": 1},
            {
                "$project": {
                    "_id": 1,
                    "name": 1,
                }
            },
        ]
    )
    result = list(result)
    return result[0] if result else None
