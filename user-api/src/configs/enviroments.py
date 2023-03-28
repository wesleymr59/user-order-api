from functools import lru_cache
import os
from pydantic import BaseSettings


@lru_cache
def get_env_filename():
    runtime_env = os.getenv("ENV")
    return f".env" if runtime_env else ".env"


class EnvironmentSettings(BaseSettings):
    API_VERSION: str
    APP_NAME: str
    MYSQL_HOST:str
    MYSQL_PORT:str
    MYSQL_USER:str
    MYSQL_PASSWORD:str
    MYSQL_ROOT_PASSWORD:str
    MYSQL_DATABASE:str
    REDIS_HOST:str
    ENV_TOKEN:str


    class Config:
        env_file = get_env_filename()
        env_file_encoding = "utf-8"


@lru_cache
def get_environment_variables():
    return EnvironmentSettings()
