from shared.app.errors import ApplicationError
from shared.app.value_object import ValueObject


class LastNameEmpty(ApplicationError):
    @property
    def details(self) -> str:
        return "Фамилия пользователя не может быть пустой"


class LastNameTooLong(ApplicationError):
    @property
    def details(self) -> str:
        return "Фамилия пользователя слишком длинная"


class LastName(ValueObject[str]):
    def validate(self):
        if not self.value:
            raise LastNameEmpty()

        if len(self.value) > 50:
            raise LastNameTooLong()
