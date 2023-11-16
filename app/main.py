from fastapi import FastAPI

from app.endpoints import router


def create_app():
    """
    Создает приложение и настраивает его
    Тут могут быть настройки генерации Openapi
    """
    new_app = FastAPI()
    new_app.include_router(router)
    return new_app


app = create_app()
