from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, HTTPException, status

from ..core import errors
from ..core.services import AuthenticateUserService, RefreshTokenService
from . import http_schemas


router = APIRouter(
    prefix="/auth",
    tags=["Аутентификация"],
    route_class=DishkaRoute,
)


@router.post("/login/", response_model=http_schemas.SLoginOut)
async def login(
    data: http_schemas.SLoginIn,
    authenticate_user_service: FromDishka[AuthenticateUserService],
):
    return await authenticate_user_service(
        phone=data.phone,
        password=data.password,
    )


@router.post("/refresh/", response_model=http_schemas.SRefreshTokenOut)
async def refresh(
    data: http_schemas.SRefreshTokenIn,
    refresh_token_service: FromDishka[RefreshTokenService],
):
    try:
        access_token = await refresh_token_service(data.refresh_token)
    except errors.InvalidTokenData as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=e.details,
        )

    return http_schemas.SRefreshTokenOut(access_token=access_token)
