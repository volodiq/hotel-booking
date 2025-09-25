from pydantic_settings import BaseSettings, SettingsConfigDict


class Env(BaseSettings):
    SECRET_KEY: str

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
