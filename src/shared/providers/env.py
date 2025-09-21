from os import getenv

from dishka import Provider, Scope, provide
from pydantic_settings import BaseSettings, SettingsConfigDict


class Env(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DBMS_HOST: str
    DBMS_PORT: int

    @property
    def db_dsn(self) -> str:
        dbms = "postgresql"
        driver = "asyncpg"
        return (
            f"{dbms}+{driver}://"
            f"{self.DB_USER}:{self.DB_PASSWORD}@"
            f"{self.DBMS_HOST}:{self.DBMS_PORT}/{self.DB_NAME}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="allow",
    )


class EnvProvider(Provider):
    @provide(scope=Scope.APP)
    def env(self) -> Env:
        app_run_as_service = getenv("APP_RUN_AS_SERVICE")
        if app_run_as_service:
            return Env()  # type: ignore
        return Env(DB_NAME="localhost")  # type: ignore
