from shared.app.errors import ApplicationError
from shared.app.value_object import ValueObject


class FirstNameEmpty(ApplicationError):
    @property
    def details(self) -> str:
        return "Имя пользователя не может быть пустым"


class FirstNameTooLong(ApplicationError):
    @property
    def details(self) -> str:
        return "Имя пользователя слишком длинное"


class FirstName(ValueObject[str]):
    def validate(self):
        if not self.value:
            raise FirstNameEmpty()

        if len(self.value) > 50:
            raise FirstNameTooLong()
