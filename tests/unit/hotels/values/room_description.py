from faker import Faker
import pytest

from contexts.hotels.app.values.room_description import (
    RoomDescription,
    RoomDescriptionInvalidError,
    RoomDescriptionInvalidReason,
)


def test_room_description(faker: Faker):
    room_description = RoomDescription(faker.text(max_nb_chars=1024))
    assert room_description.value


@pytest.mark.parametrize(
    "room_description, reason",
    [
        ("1" * 1025, RoomDescriptionInvalidReason.TOO_LONG),
    ],
)
def test_room_description_invalid(room_description, reason):
    with pytest.raises(RoomDescriptionInvalidError) as e:
        RoomDescription(room_description)

    assert e.value.reason == reason
