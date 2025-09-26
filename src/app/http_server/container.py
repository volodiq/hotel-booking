from dishka import Provider, Scope, provide
from dishka.integrations.fastapi import FastapiProvider
from fastapi import HTTPException, Request, status

from app.container import make_container
from system.security.dtos import Principal, TokenType
from system.security.services import TokenService


class PrincipalProvider(Provider):
    @provide(scope=Scope.REQUEST)
    async def principal(self, request: Request, token_service: TokenService) -> Principal:
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Запрос не содержит заголовка авторизации",
            )
        schema, _, token = auth_header.partition(" ")
        if schema != "Bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Данная схема авторизации не поддерживается",
            )
        return token_service.decode(token, TokenType.ACCESS)


container = make_container(
    PrincipalProvider(),
    FastapiProvider(),
)
