from functools import partial
from http import HTTPStatus

from fastapi import FastAPI, HTTPException, Request

from system.security.errors import SecurityException
from system.seedwork.errors import DomainError


def setup_exceptions_handlers(app: FastAPI):
    app.add_exception_handler(DomainError, partial(error_handler, HTTPStatus.BAD_REQUEST))
    app.add_exception_handler(SecurityException, partial(error_handler, HTTPStatus.UNAUTHORIZED))


async def error_handler(
    status_code: HTTPStatus,
    request: Request,
    exc: DomainError | SecurityException,
) -> None:
    raise HTTPException(
        status_code=status_code,
        detail=exc.details,
    )
