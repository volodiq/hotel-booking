from dataclasses import dataclass

from shared.app.dtos import Principal

from . import entities, errors, interfaces, values


def validate_principal(principal: Principal):
    if "hotel_admin" not in principal.roles:
        raise errors.ActionForbidden()


@dataclass
class CreateHotel:
    hotel_repository: interfaces.HotelRepository

    async def __call__(
        self,
        principal: Principal,
        rating: int,
        name: str,
        address: str,
    ):
        validate_principal(principal)

        hotel = entities.Hotel(
            rating=values.HotelRating(rating),
            name=name,
            address=address,
            hotel_admin_oid=principal.sub,
        )
        await self.hotel_repository.save(hotel)


@dataclass
class CreateRoom:
    room_repository: interfaces.RoomRepository
    hotel_repository: interfaces.HotelRepository

    async def _verify_access(self, principal: Principal, hotel_oid: str):
        hotel = await self.hotel_repository.get_by_oid(hotel_oid)
        if hotel is None or hotel.hotel_admin_oid != principal.sub:
            raise errors.HotelNotFound()

    async def __call__(
        self,
        principal: Principal,
        hotel_oid: str,
        name: str,
        description: str,
        room_type: entities.RoomType,
        bed_type: entities.RoomBedType,
    ):
        validate_principal(principal)
        await self._verify_access(principal=principal, hotel_oid=hotel_oid)

        room = entities.Room(
            name=name,
            description=values.RoomDescription(description),
            room_type=entities.RoomType(room_type),
            bed_type=entities.RoomBedType(bed_type),
            hotel_oid=hotel_oid,
        )
        await self.room_repository.save(room)


@dataclass
class AddRoomPhoto:
    room_repository: interfaces.RoomRepository
    hotel_repository: interfaces.HotelRepository
    photo_storage: interfaces.PhotoStorage

    async def _verify_access(self, principal: Principal, hotel_oid: str):
        hotel = await self.hotel_repository.get_by_oid(hotel_oid)
        if hotel is None or hotel.hotel_admin_oid != principal.sub:
            raise errors.HotelNotFound()

    async def __call__(
        self,
        principal: Principal,
        hotel_oid: str,
        room_oid: str,
        photo_as_bytes: bytes,
        caption: str | None = None,
        is_cover: bool = False,
    ):
        validate_principal(principal=principal)
        await self._verify_access(principal=principal, hotel_oid=hotel_oid)

        room = await self.room_repository.get_by_oid(room_oid)
        if room is None:
            raise errors.RoomNotFound()

        url = await self.photo_storage.upload(photo_as_bytes)
        room.add_photo(entities.RoomPhoto(url=url, caption=caption, is_cover=is_cover))
        return await self.room_repository.save(room)
