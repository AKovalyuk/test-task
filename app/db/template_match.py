from typing import Optional

from pymongo.collection import Collection


def template_match(fields: list[tuple[str, str]], collection: Collection) -> Optional[dict]:
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
