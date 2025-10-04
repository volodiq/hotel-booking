from dataclasses import dataclass
from datetime import timedelta
from typing import AsyncIterable

import environs
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from shared.infra.services import PyJWTTokenService, TokenService


@dataclass(frozen=True, slots=True)
class Env:
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


def get_session_pool(env: Env) -> async_sessionmaker:
    engine = create_async_engine(env.db_dsn)
    return async_sessionmaker(engine, expire_on_commit=False)


def get_env() -> Env:
    env = environs.Env()
    env.read_env()

    is_run_as_service = env.bool("APP_RUN_AS_SERVICE", default=False)

    secret_key = env.str("SECRET_KEY")

    db_name = env.str("DB_NAME")
    db_user = env.str("DB_USER")
    db_password = env.str("DB_PASSWORD")
    dbms_host = env.str("DBMS_HOST") if is_run_as_service else "localhost"
    dbms_port = env.int("DBMS_PORT")

    return Env(
        SECRET_KEY=secret_key,
        DB_NAME=db_name,
        DB_USER=db_user,
        DB_PASSWORD=db_password,
        DBMS_HOST=dbms_host,
        DBMS_PORT=dbms_port,
    )


def get_token_service(env: Env) -> TokenService:
    return PyJWTTokenService(
        secret_key=env.SECRET_KEY,
        access_token_ttl=timedelta(hours=1),
        refresh_token_ttl=timedelta(weeks=1),
    )


async def get_sa_session(session_pool: async_sessionmaker) -> AsyncIterable[AsyncSession]:
    async with session_pool.begin() as session:
        yield session
