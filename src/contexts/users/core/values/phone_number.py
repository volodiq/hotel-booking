import phonenumbers

from shared.core.errors import DomainError
from shared.core.value_object import ValueObject


class PhoneNumberEmpty(DomainError):
    @property
    def details(self) -> str:
        return "Номер телефона пользователя не может быть пустым"


class PhoneNumberInvalid(DomainError):
    @property
    def details(self) -> str:
        return "Номер телефона пользователя некорректен"


class PhoneNumberUnsupportedRegion(DomainError):
    @property
    def details(self) -> str:
        return "Данный регион не поддерживается"


class PhoneNumber(ValueObject[str]):
    def validate(self):
        if not self._value:
            raise PhoneNumberEmpty()

        try:
            parsed_number = phonenumbers.parse(self._value, "RU")
        except phonenumbers.NumberParseException:
            raise PhoneNumberInvalid()
        if not phonenumbers.is_possible_number(parsed_number):
            raise PhoneNumberInvalid()
        if not phonenumbers.is_valid_number(parsed_number):
            raise PhoneNumberInvalid()
        if not phonenumbers.is_valid_number_for_region(parsed_number, "RU"):
            raise PhoneNumberUnsupportedRegion()

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
