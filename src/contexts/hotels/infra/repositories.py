from dataclasses import dataclass

from sqlalchemy import sql
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from ..core import entities, values
from ..core.interfaces import HotelRepository, RoomRepository
from . import models


@dataclass
class SAHotelRepository(HotelRepository):
    session: AsyncSession

    @staticmethod
    def to_entity(model: models.Hotel) -> entities.Hotel:
        return entities.Hotel(
            oid=model.oid,
            name=model.name,
            address=model.address,
            rating=values.HotelRating(model.rating),
            hotel_admin_oid=model.hotel_admin_oid,
            created_at=model.created_at,
        )

    async def save(self, hotel: entities.Hotel) -> None:
        insert_stmt = insert(models.Hotel).values(
            oid=hotel.oid,
            name=hotel.name,
            address=hotel.address,
            rating=hotel.rating.value,
            hotel_admin_oid=hotel.hotel_admin_oid,
            created_at=hotel.created_at.replace(tzinfo=None),
        )
        upsert_stmt = insert_stmt.on_conflict_do_update(
            index_elements=[models.Hotel.oid],
            set_={
                "name": insert_stmt.excluded.name,
                "address": insert_stmt.excluded.address,
                "rating": insert_stmt.excluded.rating,
                "hotel_admin_oid": insert_stmt.excluded.hotel_admin_oid,
            },
        )
        await self.session.execute(upsert_stmt)

    async def get_by_oid(self, oid: str) -> entities.Hotel | None:
        stmt = sql.select(models.Hotel).where(models.Hotel.oid == oid)
        res = await self.session.scalars(stmt)
        model = res.one_or_none()
        if not model:
            return None

        return self.to_entity(model)


@dataclass
class SARoomRepository(RoomRepository):
    session: AsyncSession

    @staticmethod
    def to_entity(model: models.Room) -> entities.Room:
        return entities.Room(
            oid=model.oid,
            name=model.name,
            hotel_oid=model.hotel_oid,
            description=values.RoomDescription(model.description),
            room_type=model.room_type,
            bed_type=model.bed_type,
            created_at=model.created_at,
            _photos=[
                entities.RoomPhoto(
                    oid=p.oid,
                    url=p.url,
                    is_cover=p.is_cover,
                    caption=p.caption,
                    created_at=p.created_at,
                )
                for p in model.photos
            ],
        )

    @staticmethod
    def to_model(room: entities.Room) -> models.Room:
        return models.Room(
            oid=room.oid,
            name=room.name,
            hotel_oid=room.hotel_oid,
            description=room.description.value,
            room_type=room.room_type,
            bed_type=room.bed_type,
            created_at=room.created_at.replace(tzinfo=None),
            photos=[
                models.RoomPhoto(
                    oid=p.oid,
                    url=p.url,
                    is_cover=p.is_cover,
                    caption=p.caption,
                    created_at=p.created_at.replace(tzinfo=None),
                )
                for p in room.photos
            ],
        )

    async def _upsert_room(self, room: models.Room) -> None:
        insert_stmt = insert(models.Room).values(
            oid=room.oid,
            hotel_oid=room.hotel_oid,
            name=room.name,
            description=room.description,
            room_type=room.room_type,
            bed_type=room.bed_type,
            created_at=room.created_at.replace(tzinfo=None),
        )
        upsert_stmt = insert_stmt.on_conflict_do_update(
            index_elements=[models.Room.oid],
            set_={
                "name": insert_stmt.excluded.name,
                "description": insert_stmt.excluded.description,
                "room_type": insert_stmt.excluded.room_type,
                "bed_type": insert_stmt.excluded.bed_type,
            },
        )
        await self.session.execute(upsert_stmt)

    async def _upsert_photos(self, room: models.Room):
        delete_stmt = sql.delete(models.RoomPhoto).where(models.RoomPhoto.room_oid == room.oid)
        await self.session.execute(delete_stmt)
        if not room.photos:
            return
        insert_stmt = insert(models.RoomPhoto).values(
            [
                {
                    "oid": p.oid,
                    "room_oid": room.oid,
                    "url": p.url,
                    "is_cover": p.is_cover,
                    "caption": p.caption,
                    "created_at": p.created_at,
                }
                for p in room.photos
            ]
        )
        await self.session.execute(insert_stmt)

    async def save(self, room: entities.Room) -> None:
        model = self.to_model(room)
        await self._upsert_room(model)
        await self._upsert_photos(model)

    async def get_by_oid(self, oid: str) -> entities.Room | None:
        stmt = (
            sql.select(models.Room)
            .where(models.Room.oid == oid)
            .options(selectinload(models.Room.photos))
        )
        res = await self.session.scalars(stmt)
        model = res.one_or_none()
        if not model:
            return None

        return self.to_entity(model)
