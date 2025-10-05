from string import punctuation

from shared.app.errors import DomainError
from shared.app.value_object import ValueObject


class PasswordEmpty(DomainError):
    @property
    def details(self) -> str:
        return "Пароль не может быть пустой"


class PasswordTooLong(DomainError):
    @property
    def details(self) -> str:
        return "Пароль не может быть длиннее 30 символов"


class PasswordTooShort(DomainError):
    @property
    def details(self) -> str:
        return "Пароль не может быть короче 8 символов"


class PasswordNotContainsDigit(DomainError):
    @property
    def details(self) -> str:
        return "Пароль должен содержать хотя бы одну цифру"


class PasswordNotContainsUppercase(DomainError):
    @property
    def details(self) -> str:
        return "Пароль должен содержать хотя бы одну заглавную букву"


class PasswordNotContainsLowercase(DomainError):
    @property
    def details(self) -> str:
        return "Пароль должен содержать хотя бы одну строчную букву"


class PasswordNotContainsSpecialSymbol(DomainError):
    @property
    def details(self) -> str:
        return "Пароль должен содержать хотя бы один специальный символ"


class Password(ValueObject[str]):
    """
    Сырой пароль, проверяет пароль на стойкость.
    """

    def validate(self):
        if not self.value:
            raise PasswordEmpty()

        if len(self.value) > 30:
            raise PasswordTooLong()

        if len(self.value) < 8:
            raise PasswordTooShort()

        if not any(char.isdigit() for char in self.value):
            raise PasswordNotContainsDigit()

        if not any(char.isupper() for char in self.value):
            raise PasswordNotContainsUppercase()

        if not any(char.islower() for char in self.value):
            raise PasswordNotContainsLowercase()

        if not any(char in punctuation for char in self.value):
            raise PasswordNotContainsSpecialSymbol()
