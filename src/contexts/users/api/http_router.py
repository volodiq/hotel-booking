from uuid import UUID

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, HTTPException, status

from system.security.tokens.fastapi import PrincipalDep

from ..app import errors, use_cases
from . import http_schemas


router = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
    route_class=DishkaRoute,
)


@router.post("/")
async def create_user(
    data: http_schemas.SCreateUser,
    use_case: FromDishka[use_cases.CreateUser],
):
    """
    Создание пользователя.
    """

    await use_case(
        first_name=data.first_name,
        last_name=data.last_name,
        phone=data.phone,
        password=data.password,
    )


@router.post("/{user_oid}/make-hotel-admin/")
async def make_hotel_admin(
    user_oid: UUID,
    principal: PrincipalDep,
    use_case: FromDishka[use_cases.MakeHotelAdmin],
):
    """
    Сделать пользователя администратором отеля.
    (только для администраторов).
    """

    try:
        await use_case(principal, user_oid.hex)
    except errors.MakeHotelAdminForbidden as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=e.details,
        )
