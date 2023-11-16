from typing import Optional

from pymongo.collection import Collection


def template_match(fields: dict[str, str], collection: Collection) -> Optional[dict]:
    ...