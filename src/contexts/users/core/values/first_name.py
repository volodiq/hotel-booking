from dataclasses import dataclass
from enum import StrEnum

from shared.core.errors import ApplicationError
from shared.core.value_object import ValueObject


class FirstNameInvalidReason(StrEnum):
    EMPTY = "first_name.empty"
    TOO_LONG = "first_name.too_long"


INVALID_NAME_REASONS_DETAILS = {
    FirstNameInvalidReason.EMPTY: "Имя пользователя не может быть пустым",
    FirstNameInvalidReason.TOO_LONG: "Имя пользователя слишком длинное",
}


@dataclass
class FirstNameInvalidError(ApplicationError):
    reason: FirstNameInvalidReason

    @property
    def details(self) -> str:
        return INVALID_NAME_REASONS_DETAILS[self.reason]


class FirstName(ValueObject[str]):
    def validate(self):
        if not self.value:
            raise FirstNameInvalidError(FirstNameInvalidReason.EMPTY)

        if len(self.value) > 50:
            raise FirstNameInvalidError(FirstNameInvalidReason.TOO_LONG)
