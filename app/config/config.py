from os import getenv

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Загружает конфигурацию из .env файла
    """

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    # Настройки сервиса
    APP_PORT: int = int(getenv('APP_PORT', '8000'))

    # Настройки соединения с БД
    MONGO_INITDB_ROOT_USERNAME: str = getenv('MONGO_INITDB_ROOT_USERNAME', 'user')
    MONGO_INITDB_ROOT_PASSWORD: str = getenv('MONGO_INITDB_ROOT_PASSWORD', '12345')
    MONGO_DATABASE: str = getenv('MONGO_DATABASE', 'templates')
    MONGO_HOST: str = getenv('MONGO_HOST', 'db')
    MONGO_PORT: int = int(getenv('MONGO_PORT', '27017'))
    MONGO_COLLECTION: str = getenv('MONGO_COLLECTION', 'templates')


settings = Settings()
