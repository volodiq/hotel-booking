from dishka import Provider, Scope, make_async_container, provide
from dishka.integrations.fastapi import FastapiProvider
from fastapi import Request

from contexts.auth.di import AuthProvider
from contexts.hotel_admins.di import HotelAdminProvider
from contexts.users.di import UsersProvider
from shared.providers.db import DBProvider
from tech.di import TechProvider
from tech.security.dtos import Principal, TokenType
from tech.security.errors import NotAuthenticated
from tech.security.services import TokenService


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
    TechProvider(),
    DBProvider(),
    UsersProvider(),
    AuthProvider(),
    PrincipalProvider(),
    HotelAdminProvider(),
)
