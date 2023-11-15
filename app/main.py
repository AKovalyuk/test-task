from fastapi import FastAPI

from app.endpoints import router, get_form


def create_app():
    app = FastAPI()
    app.include_router(router)
    return app


app = create_app()
