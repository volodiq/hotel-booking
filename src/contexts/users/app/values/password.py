from dataclasses import dataclass
from enum import StrEnum
from string import punctuation

from shared.app.errors import ApplicationError
from shared.app.value_object import ValueObject


class PasswordInvalidReason(StrEnum):
    EMPTY = "password.empty"
    TOO_LONG = "password.too_long"
    TOO_SHORT = "password.too_short"
    NOT_CONTAINS_DIGIT = "password.not_contains_digit"
    NOT_CONTAINS_UPPERCASE = "password.not_contains_uppercase"
    NOT_CONTAINS_LOWERCASE = "password.not_contains_lowercase"
    NOT_CONTAINS_SPECIAL_SYMBOL = "password.not_contains_special_symbol"


PASSWORD_INVALID_REASONS_DETAILS = {
    PasswordInvalidReason.EMPTY: "Пароль не может быть пустой",
    PasswordInvalidReason.TOO_LONG: "Пароль не может быть длиннее 30 символов",
    PasswordInvalidReason.TOO_SHORT: "Пароль не может быть короче 8 символов",
    PasswordInvalidReason.NOT_CONTAINS_DIGIT: "Пароль должен содержать хотя бы одну цифру",
    PasswordInvalidReason.NOT_CONTAINS_UPPERCASE: "Пароль должен содержать хотя бы одну заглавную букву",
    PasswordInvalidReason.NOT_CONTAINS_LOWERCASE: "Пароль должен содержать хотя бы одну строчную букву",
    PasswordInvalidReason.NOT_CONTAINS_SPECIAL_SYMBOL: "Пароль должен содержать хотя бы один специальный символ",
}


@dataclass
class PasswordInvalidError(ApplicationError):
    reason: PasswordInvalidReason

    @property
    def details(self) -> str:
        return PASSWORD_INVALID_REASONS_DETAILS[self.reason]


class Password(ValueObject[str]):
    """
    Сырой пароль, проверяет пароль на стойкость.
    """

    def validate(self):
        if not self.value:
            raise PasswordInvalidError(PasswordInvalidReason.EMPTY)

        if len(self.value) > 30:
            raise PasswordInvalidError(PasswordInvalidReason.TOO_LONG)

        if len(self.value) < 8:
            raise PasswordInvalidError(PasswordInvalidReason.TOO_SHORT)

        if not any(char.isdigit() for char in self.value):
            raise PasswordInvalidError(PasswordInvalidReason.NOT_CONTAINS_DIGIT)

        if not any(char.isupper() for char in self.value):
            raise PasswordInvalidError(PasswordInvalidReason.NOT_CONTAINS_UPPERCASE)

        if not any(char.islower() for char in self.value):
            raise PasswordInvalidError(PasswordInvalidReason.NOT_CONTAINS_LOWERCASE)

        if not any(char in punctuation for char in self.value):
            raise PasswordInvalidError(PasswordInvalidReason.NOT_CONTAINS_SPECIAL_SYMBOL)
