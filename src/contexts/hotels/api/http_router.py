from typing import Annotated

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, File, Form, HTTPException, status

from shared.api.fastapi_di import PrincipalDep

from ..core import errors, use_cases
from . import schemas


router = APIRouter(
    prefix="/hotels",
    tags=["Отели"],
    route_class=DishkaRoute,
)


@router.post("/")
async def create_hotel(
    data: schemas.SCreateHotel,
    use_case: FromDishka[use_cases.CreateHotel],
    principal: PrincipalDep,
):
    try:
        await use_case(
            principal=principal,
            rating=data.rating,
            name=data.name,
            address=data.address,
        )
    except errors.ActionForbidden as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=e.details,
        )


@router.post("/{hotel_oid}/rooms/")
async def create_room(
    hotel_oid: str,
    data: schemas.SCreateRoom,
    use_case: FromDishka[use_cases.CreateRoom],
    principal: PrincipalDep,
):
    try:
        await use_case(
            principal=principal,
            hotel_oid=hotel_oid,
            name=data.name,
            description=data.description,
            room_type=data.room_type,
            bed_type=data.bed_type,
        )
    except errors.ActionForbidden as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=e.details,
        )


@router.post("/{hotel_oid}/rooms/{room_oid}/photos/")
async def add_room_photo(
    hotel_oid: str,
    room_oid: str,
    principal: PrincipalDep,
    photo: Annotated[bytes, File()],
    use_case: FromDishka[use_cases.AddRoomPhoto],
    is_cover: Annotated[bool, Form()],
    caption: Annotated[str | None, Form()] = None,
):
    try:
        await use_case(
            principal=principal,
            hotel_oid=hotel_oid,
            room_oid=room_oid,
            photo_as_bytes=photo,
            caption=caption,
            is_cover=is_cover,
        )
    except errors.ActionForbidden as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=e.details,
        )
