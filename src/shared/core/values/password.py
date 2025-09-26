from string import punctuation

from system.seedwork.value_object import ValueObject

from ..errors import password_errors


class Password(ValueObject[str]):
    """
    Сырой пароль, проверяет пароль на стойкость.
    """

    def validate(self):
        if not self.value:
            raise password_errors.PasswordEmpty()

        if len(self.value) > 30:
            raise password_errors.PasswordTooLong()

        if len(self.value) < 8:
            raise password_errors.PasswordTooShort()

        if not any(char.isdigit() for char in self.value):
            raise password_errors.PasswordNotContainsDigit()

        if not any(char.isupper() for char in self.value):
            raise password_errors.PasswordNotContainsUppercase()

        if not any(char.islower() for char in self.value):
            raise password_errors.PasswordNotContainsLowercase()

        if not any(char in punctuation for char in self.value):
            raise password_errors.PasswordNotContainsSpecialSymbol()
