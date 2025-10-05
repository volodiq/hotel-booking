from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter

from ..app import use_cases
from . import schemas


router = APIRouter(
    prefix="/auth",
    tags=["Аутентификация"],
    route_class=DishkaRoute,
)


@router.post("/login/", response_model=schemas.SLoginOut)
async def login(
    data: schemas.SLoginIn,
    use_case: FromDishka[use_cases.AuthenticateUser],
):
    """
    Получение токенов для аутентификации.
    """

    return await use_case(
        phone=data.phone,
        password=data.password,
    )


@router.post("/refresh/", response_model=schemas.SRefreshTokenOut)
async def refresh(
    data: schemas.SRefreshTokenIn,
    use_case: FromDishka[use_cases.RefreshToken],
):
    """
    Обновление токена доступа.
    """

    access_token = await use_case(data.refresh_token)
    return schemas.SRefreshTokenOut(access_token=access_token)
