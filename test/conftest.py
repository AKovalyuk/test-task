from pytest import fixture
from httpx import AsyncClient

from app.config import settings
from app.db import client as db_client
from app.main import app


pytest_plugins = [
    'fixtures.data',
]


@fixture(scope='session')
def db():
    settings.MONGO_DATABASE = 'test_db'
    yield
    db_client.drop_database(settings.MONGO_DATABASE)


@fixture(scope='session')
async def client(db) -> AsyncClient:
    yield AsyncClient(app=app, base_url="http://test")
