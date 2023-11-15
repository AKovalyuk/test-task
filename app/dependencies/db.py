from app.db import client


async def get_session():
    session = client.start_session()
    try:
        yield session
    finally:
        session.end_session()
