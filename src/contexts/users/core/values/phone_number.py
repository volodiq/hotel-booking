from dataclasses import dataclass
from enum import StrEnum

import phonenumbers

from shared.core.errors import ApplicationError
from shared.core.value_object import ValueObject


class PhoneNumberInvalidReason(StrEnum):
    EMPTY = "phone_number.empty"
    INVALID = "phone_number.invalid"
    UNSUPPORTED_REGION = "phone_number.unsupported_region"


PHONE_NUMBER_INVALID_REASONS_DESCRIPTION = {
    PhoneNumberInvalidReason.EMPTY: "Номер телефона пользователя не может быть пустым",
    PhoneNumberInvalidReason.INVALID: "Номер телефона пользователя некорректен",
    PhoneNumberInvalidReason.UNSUPPORTED_REGION: "Данный регион не поддерживается",
}


@dataclass
class PhoneNumberInvalidError(ApplicationError):
    reason: PhoneNumberInvalidReason

    @property
    def details(self) -> str:
        return PHONE_NUMBER_INVALID_REASONS_DESCRIPTION[self.reason]


class PhoneNumber(ValueObject[str]):
    def validate(self):
        if not self._value:
            raise PhoneNumberInvalidError(PhoneNumberInvalidReason.EMPTY)

        try:
            parsed_number = phonenumbers.parse(self._value, "RU")
        except phonenumbers.NumberParseException:
            raise PhoneNumberInvalidError(PhoneNumberInvalidReason.INVALID)
        if not phonenumbers.is_possible_number(parsed_number):
            raise PhoneNumberInvalidError(PhoneNumberInvalidReason.INVALID)
        if not phonenumbers.is_valid_number(parsed_number):
            raise PhoneNumberInvalidError(PhoneNumberInvalidReason.INVALID)
        if not phonenumbers.is_valid_number_for_region(parsed_number, "RU"):
            raise PhoneNumberInvalidError(PhoneNumberInvalidReason.UNSUPPORTED_REGION)

    @property
    def value(self):
        """
        Возвращает номер телефона в формате E164
        """

        parsed_number = phonenumbers.parse(self._value, "RU")
        return phonenumbers.format_number(
            parsed_number,
            phonenumbers.PhoneNumberFormat.E164,
        )
