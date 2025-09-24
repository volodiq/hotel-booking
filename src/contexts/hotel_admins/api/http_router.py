from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, HTTPException, status

from ..core import errors
from ..core.services import CreateHotelAdminService
from . import http_schemas


router = APIRouter(
    prefix="/hotel_admins",
    tags=["Администраторы отелей"],
    route_class=DishkaRoute,
)


@router.post("/", openapi_extra={"security": [{"HTTPBearer": []}]})
async def create_hotel_admin(
    data: http_schemas.SCreateHotelAdmin,
    create_hotel_admin_service: FromDishka[CreateHotelAdminService],
):
    try:
        await create_hotel_admin_service(
            first_name=data.first_name,
            last_name=data.last_name,
            middle_name=data.middle_name,
            phone=data.phone,
            email=data.email,
            raw_password=data.raw_password,
        )
    except errors.HotelAdminCreateForbidden as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=e.details,
        )
