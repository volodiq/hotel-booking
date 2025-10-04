from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter

from ..app import use_cases
from . import http_schemas


router = APIRouter(
    prefix="/auth",
    tags=["Аутентификация"],
    route_class=DishkaRoute,
)


@router.post("/login/", response_model=http_schemas.SLoginOut)
async def login(
    data: http_schemas.SLoginIn,
    use_case: FromDishka[use_cases.AuthenticateUser],
):
    """
    Получение токенов для аутентификации.
    """

    return await use_case(
        phone=data.phone,
        password=data.password,
    )


@router.post("/refresh/", response_model=http_schemas.SRefreshTokenOut)
async def refresh(
    data: http_schemas.SRefreshTokenIn,
    use_case: FromDishka[use_cases.RefreshToken],
):
    """
    Обновление токена доступа.
    """

    access_token = await use_case(data.refresh_token)
    return http_schemas.SRefreshTokenOut(access_token=access_token)
