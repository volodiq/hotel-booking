from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from shared.infra.db_domains import UUID, Bool, String
from shared.infra.models import DBModel


class Hotel(DBModel):
    __tablename__ = "hotels"

    name: Mapped[String]
    hotel_admin_oid: Mapped[UUID]
    rating: Mapped[int]
    address: Mapped[String]


class Room(DBModel):
    __tablename__ = "rooms"

    name: Mapped[String]
    hotel_oid: Mapped[UUID]
    description: Mapped[String]
    room_type: Mapped[String]
    bed_type: Mapped[String]

    photos: Mapped[list["RoomPhoto"]] = relationship(back_populates="room")


class RoomPhoto(DBModel):
    __tablename__ = "room_photos"

    url: Mapped[String]
    room_oid: Mapped[UUID] = mapped_column(ForeignKey("rooms.oid"))
    caption: Mapped[String] = mapped_column(nullable=True)
    is_cover: Mapped[Bool]

    room: Mapped["Room"] = relationship(back_populates="photos")
