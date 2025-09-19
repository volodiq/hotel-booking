from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, HTTPException, status

from core.domain.exceptions import DomainError

from ..domain.services import CreateUserService
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
    try:
        await create_user_service(
            first_name=data.first_name,
            last_name=data.last_name,
            phone=data.phone,
        )
    except DomainError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.details,
        )
