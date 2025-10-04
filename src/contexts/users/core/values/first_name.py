from shared.core.errors import DomainError
from shared.core.value_object import ValueObject


class FirstNameEmpty(DomainError):
    @property
    def details(self) -> str:
        return "Имя пользователя не может быть пустым"


class FirstNameTooLong(DomainError):
    @property
    def details(self) -> str:
        return "Имя пользователя слишком длинное"


class FirstName(ValueObject[str]):
    def validate(self):
        if not self.value:
            raise FirstNameEmpty()

        if len(self.value) > 50:
            raise FirstNameTooLong()
