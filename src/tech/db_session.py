from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from tech.env import Env


def get_session_pool(env: Env) -> async_sessionmaker:
    engine = create_async_engine(env.db_dsn)
    return async_sessionmaker(engine, expire_on_commit=False)
