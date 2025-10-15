from dataclasses import dataclass, field, replace
from enum import StrEnum
from typing import Self

from shared.core.entity import Entity

from . import errors, values


class RoomType(StrEnum):
    STANDARD = "STANDARD"
    DELUXE = "DELUXE"
    SUITE = "SUITE"


class RoomBedType(StrEnum):
    SINGLE = "SINGLE"
    DOUBLE = "DOUBLE"
    TWIN = "TWIN"
    TRIPLE = "TRIPLE"
    FAMILY = "FAMILY"


@dataclass(eq=False, frozen=True)
class RoomPhoto(Entity):
    url: str
    is_cover: bool
    caption: str | None = None

    def disable_cover(self) -> Self:
        return replace(self, is_cover=False)


@dataclass(eq=False, frozen=True)
class Room(Entity):
    name: str
    hotel_oid: str
    description: values.RoomDescription
    room_type: RoomType
    bed_type: RoomBedType
    _photos: list[RoomPhoto] = field(default_factory=list, kw_only=True)

    def add_photo(self, photo: RoomPhoto):
        if len(self._photos) >= 5:
            raise errors.RoomPhotosLimitExceeded()

        photos = self._photos.copy()
        self._photos.clear()

        for p in photos:
            if photo.is_cover:
                p = p.disable_cover()
            self.photos.append(p)

        self.photos.append(photo)

    @property
    def photos(self) -> list[RoomPhoto]:
        return self._photos


@dataclass(eq=False, frozen=True)
class Hotel(Entity):
    name: str
    hotel_admin_oid: str
    rating: values.HotelRating
    address: str
