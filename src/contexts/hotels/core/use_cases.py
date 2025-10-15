from dataclasses import dataclass

from shared.core.dtos import Principal

from . import entities, errors, interfaces, services, values


@dataclass
class CreateHotel:
    hotel_repository: interfaces.HotelRepository
    access_service: services.HotelAccessService

    async def __call__(
        self,
        principal: Principal,
        rating: int,
        name: str,
        address: str,
    ):
        self.access_service.verify_module_access(principal)

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
    access_service: services.HotelAccessService

    async def __call__(
        self,
        principal: Principal,
        hotel_oid: str,
        name: str,
        description: str,
        room_type: entities.RoomType,
        bed_type: entities.RoomBedType,
    ):
        await self.access_service.verify_hotel_access(principal=principal, hotel_oid=hotel_oid)

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
    photo_storage: interfaces.PhotoStorage
    access_service: services.HotelAccessService

    async def __call__(
        self,
        principal: Principal,
        hotel_oid: str,
        room_oid: str,
        photo_as_bytes: bytes,
        caption: str | None = None,
        is_cover: bool = False,
    ):
        await self.access_service.verify_hotel_access(principal=principal, hotel_oid=hotel_oid)

        room = await self.room_repository.get_by_oid(room_oid)
        if room is None:
            raise errors.RoomNotFound()

        url = await self.photo_storage.upload(photo_as_bytes)
        room.add_photo(entities.RoomPhoto(url=url, caption=caption, is_cover=is_cover))
        return await self.room_repository.save(room)
