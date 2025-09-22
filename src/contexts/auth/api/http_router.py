from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter

from ..core.services import AuthenticateUserService
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
