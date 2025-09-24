from os import getenv

from dishka import Provider, Scope, provide

from .env import Env


class TechProvider(Provider):
    @provide(scope=Scope.APP)
    def env(self) -> Env:
        app_run_as_service = getenv("APP_RUN_AS_SERVICE")
        if app_run_as_service:
            return Env()  # type: ignore
        return Env(DBMS_HOST="localhost")  # type: ignore
