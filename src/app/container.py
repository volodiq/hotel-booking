from dishka import Provider, Scope, make_async_container, provide
from dishka.integrations.fastapi import FastapiProvider
from fastapi import Request

from contexts.auth.di import auth_provider
from contexts.users.di import users_provider
from kernel.di import kernel_provider
from kernel.security.dtos import Principal, TokenType
from kernel.security.errors import NotAuthenticated
from kernel.security.services import TokenService


class PrincipalProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def principal(self, request: Request, token_service: TokenService) -> Principal:
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            raise NotAuthenticated()
        schema, _, token = auth_header.partition(" ")
        if schema != "Bearer":
            raise NotAuthenticated()
        return token_service.decode(token, TokenType.ACCESS)


container = make_async_container(
    FastapiProvider(),
    PrincipalProvider(),
    kernel_provider,
    users_provider,
    auth_provider,
)
