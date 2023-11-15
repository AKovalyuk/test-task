from asyncio import get_event_loop_policy

from pytest import fixture
from httpx import AsyncClient

from app.config import settings
from app.db import collection
from app.main import app


pytest_plugins = [
    'fixtures.data',
]


@fixture(scope='session')
def event_loop():
    policy = get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@fixture(scope='session')
def db():
    settings.MONGO_DATABASE = 'test_db'
    try:
        yield
    finally:
        collection.delete_many({})


@fixture(scope='session')
async def client(db) -> AsyncClient:
    yield AsyncClient(app=app, base_url="http://test")
