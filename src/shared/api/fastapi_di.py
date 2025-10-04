from typing import Annotated

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.security.utils import get_authorization_scheme_param

from ..app.dtos import Principal, TokenType
from ..app.interfaces import TokenService


class LocalizedHTTPBearer(HTTPBearer):
    """
    HTTPBearer, с локализованными ошибками.
    """

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials:
        authorization = request.headers.get("Authorization")
        scheme, credentials = get_authorization_scheme_param(authorization)

        if not (authorization and scheme and credentials):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Запрос не содержит заголовка авторизации",
            )

        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Данная схема авторизации не поддерживается",
            )

        return HTTPAuthorizationCredentials(scheme=scheme, credentials=credentials)


bearer_scheme = LocalizedHTTPBearer()
BearerDep = Annotated[HTTPAuthorizationCredentials, Depends(bearer_scheme)]


@inject
async def principal_provider(
    bearer: BearerDep,
    token_service: FromDishka[TokenService],
) -> Principal:
    return token_service.decode(bearer.credentials, TokenType.ACCESS)


PrincipalDep = Annotated[Principal, Depends(principal_provider)]
