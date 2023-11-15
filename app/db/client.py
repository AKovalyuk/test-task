from pymongo import MongoClient

from app.config import settings


client = MongoClient(
    host=settings.MONGO_HOST,
    port=settings.MONGO_PORT,
    username=settings.MONGO_INITDB_ROOT_USERNAME,
    password=settings.MONGO_INITDB_ROOT_PASSWORD,
)
db = client[settings.MONGO_DATABASE]
collection = db[settings.MONGO_COLLECTION]
