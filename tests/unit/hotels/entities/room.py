from faker import Faker
import pytest

from contexts.hotels.app.entities import Room, RoomBedType, RoomPhoto, RoomType
from contexts.hotels.app.errors import RoomPhotosLimitExceeded
from contexts.hotels.app.values import RoomDescription


def test_room(faker: Faker):
    room = Room(
        name=faker.text(max_nb_chars=50),
        hotel_oid=faker.uuid4(),
        description=RoomDescription(faker.text(max_nb_chars=1024)),
        room_type=RoomType.STANDARD,
        bed_type=RoomBedType.SINGLE,
    )

    room.add_photo(RoomPhoto(faker.url(), is_cover=True))
    room.add_photo(RoomPhoto(faker.url(), is_cover=True))
    room.add_photo(RoomPhoto(faker.url(), is_cover=False))
    room.add_photo(RoomPhoto(faker.url(), is_cover=False))
    room.add_photo(RoomPhoto(faker.url(), is_cover=False))

    assert len(room.photos) == 5
    assert len([p for p in room.photos if p.is_cover]) == 1

    with pytest.raises(RoomPhotosLimitExceeded):
        room.add_photo(RoomPhoto(faker.url(), is_cover=False))
