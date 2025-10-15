from sqlalchemy import ForeignKey, types
from sqlalchemy.orm import Mapped, mapped_column, relationship

from shared.infra.db_domains import UUID, Bool, String
from shared.infra.models import DBModel

from ..core import entities


class HotelModel(DBModel):
    __tablename__ = "hotels"

    name: Mapped[String]
    hotel_admin_oid: Mapped[UUID]
    rating: Mapped[int]
    address: Mapped[String]


class RoomModel(DBModel):
    __tablename__ = "rooms"

    name: Mapped[String]
    hotel_oid: Mapped[UUID]
    description: Mapped[String]
    room_type: Mapped[entities.RoomType] = mapped_column(
        types.Enum(entities.RoomType),
        nullable=False,
    )
    bed_type: Mapped[entities.RoomBedType] = mapped_column(
        types.Enum(entities.RoomBedType),
        nullable=False,
    )

    photos: Mapped[list["RoomPhotoModel"]] = relationship(back_populates="room")


class RoomPhotoModel(DBModel):
    __tablename__ = "room_photos"

    url: Mapped[String]
    room_oid: Mapped[UUID] = mapped_column(ForeignKey("rooms.oid"))
    caption: Mapped[String] = mapped_column(nullable=True)
    is_cover: Mapped[Bool]

    room: Mapped["RoomModel"] = relationship(back_populates="photos")
