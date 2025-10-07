from dataclasses import dataclass
from enum import StrEnum

from shared.app.errors import ApplicationError
from shared.app.value_object import ValueObject


class LastNameInvalidReason(StrEnum):
    EMPTY = "last_name.empty"
    TOO_LONG = "last_name.too_long"


LAST_NAME_INVALID_REASONS_DETAILS = {
    LastNameInvalidReason.EMPTY: "Фамилия пользователя не может быть пустой",
    LastNameInvalidReason.TOO_LONG: "Фамилия пользователя слишком длинная",
}


@dataclass
class LastNameInvalidError(ApplicationError):
    reason: LastNameInvalidReason

    @property
    def details(self) -> str:
        return LAST_NAME_INVALID_REASONS_DETAILS[self.reason]


class LastName(ValueObject[str]):
    def validate(self):
        if not self.value:
            raise LastNameInvalidError(LastNameInvalidReason.EMPTY)

        if len(self.value) > 50:
            raise LastNameInvalidError(LastNameInvalidReason.TOO_LONG)
