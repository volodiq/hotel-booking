from uuid import UUID

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, HTTPException, status

from system.security.fastapi import PrincipalDep

from ..core import errors
from ..core.services import CreateUserService, MakeHotelAdminService
from . import http_schemas


router = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
    route_class=DishkaRoute,
)


@router.post("/")
async def create_user(
    data: http_schemas.SCreateUser,
    create_user_service: FromDishka[CreateUserService],
):
    """
    Создание пользователя.
    """

    await create_user_service(
        first_name=data.first_name,
        last_name=data.last_name,
        phone=data.phone,
        password=data.password,
    )


@router.post("/{user_oid}/make-hotel-admin/")
async def make_hotel_admin(
    user_oid: UUID,
    principal: PrincipalDep,
    make_hotel_admin_service: FromDishka[MakeHotelAdminService],
):
    """
    Сделать пользователя администратором отеля.
    (только для администраторов).
    """

    try:
        await make_hotel_admin_service(principal, user_oid.hex)
    except errors.MakeHotelAdminForbidden as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=e.details,
        )
