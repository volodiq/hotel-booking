from datetime import timedelta
from os import getenv

from dishka import Provider, Scope, provide

from .env import Env
from .security.services import PyJWTTokenService, TokenService


class TechProvider(Provider):
    @provide(scope=Scope.APP)
    def env(self) -> Env:
        app_run_as_service = getenv("APP_RUN_AS_SERVICE")
        if app_run_as_service:
            return Env()  # type: ignore
        return Env(DBMS_HOST="localhost")  # type: ignore

    @provide(scope=Scope.APP)
    def token_service(self, env: Env) -> TokenService:
        return PyJWTTokenService(
            secret_key=env.SECRET_KEY,
            access_token_ttl=timedelta(hours=1),
            refresh_token_ttl=timedelta(weeks=1),
        )
