from system.seedwork.errors import DomainError
from system.seedwork.value_object import ValueObject


class LastNameEmpty(DomainError):
    @property
    def details(self) -> str:
        return "Фамилия пользователя не может быть пустой"


class LastNameTooLong(DomainError):
    @property
    def details(self) -> str:
        return "Фамилия пользователя слишком длинная"


class LastName(ValueObject[str]):
    def validate(self):
        if not self.value:
            raise LastNameEmpty()

        if len(self.value) > 50:
            raise LastNameTooLong()
