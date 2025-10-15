from dataclasses import dataclass
from enum import StrEnum

from shared.core.errors import ApplicationError
from shared.core.value_object import ValueObject


class RoomDescriptionInvalidReason(StrEnum):
    TOO_LONG = "room_description.too_long"


ROOM_DESCRIPTION_INVALID_REASON_DESCRIPTIONS = {
    RoomDescriptionInvalidReason.TOO_LONG: "Описание комнаты слишком длинное",
}


@dataclass
class RoomDescriptionInvalidError(ApplicationError):
    reason: RoomDescriptionInvalidReason

    @property
    def details(self) -> str:
        return ROOM_DESCRIPTION_INVALID_REASON_DESCRIPTIONS[self.reason]


class RoomDescription(ValueObject[str]):
    def validate(self):
        if len(self.value) > 1024:
            raise RoomDescriptionInvalidError(RoomDescriptionInvalidReason.TOO_LONG)
