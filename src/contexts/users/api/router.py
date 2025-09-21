from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter

from ..core.services import CreateUserService
from . import schemas


router = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
    route_class=DishkaRoute,
)


@router.post("/")
async def create_user(
    data: schemas.SCreateUser,
    create_user_service: FromDishka[CreateUserService],
):
    await create_user_service(
        first_name=data.first_name,
        last_name=data.last_name,
        phone=data.phone,
    )
