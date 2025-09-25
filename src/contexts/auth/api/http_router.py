from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter

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
    """
    Получение токенов для аутентификации.
    """

    return await authenticate_user_service(
        phone=data.phone,
        password=data.password,
    )


@router.post("/refresh/", response_model=http_schemas.SRefreshTokenOut)
async def refresh(
    data: http_schemas.SRefreshTokenIn,
    refresh_token_service: FromDishka[RefreshTokenService],
):
    """
    Обновление токена доступа.
    """

    access_token = await refresh_token_service(data.refresh_token)
    return http_schemas.SRefreshTokenOut(access_token=access_token)
