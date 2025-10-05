from dataclasses import dataclass

import environs


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
