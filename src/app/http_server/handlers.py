from typing import Any, Callable, Coroutine

from fastapi import HTTPException, Request, status
from starlette.responses import Response

from kernel.security.errors import InvalidTokenData, SecurityException
from kernel.seedwork.errors import DomainError


async def domain_error_handler(request: Request, exc: DomainError):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=exc.details,
    )


async def security_error_handler(request: Request, exc: SecurityException):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=exc.details,
    )


async def invalid_token_error_handler(request: Request, exc: InvalidTokenData):
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=exc.details,
    )


exceptions_handlers: dict[
    int | type[Exception],
    Callable[[Request, Any], Coroutine[Any, Any, Response]],
] = {
    DomainError: domain_error_handler,
    SecurityException: security_error_handler,
    InvalidTokenData: invalid_token_error_handler,
}
