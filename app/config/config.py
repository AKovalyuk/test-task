from os import getenv

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    # Service settings
    APP_PORT: int = int(getenv('APP_PORT', 8000))

    # Database settings
    MONGO_USERNAME: str = getenv('MONGO_INITDB_ROOT_USERNAME', 'user')
    MONGO_PASSWORD: str = getenv('MONGO_INITDB_ROOT_PASSWORD', '12345')


settings = Settings()
