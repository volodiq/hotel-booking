from shared.app.errors import ApplicationError


class InvalidCredentials(ApplicationError):
    @property
    def details(self) -> str:
        return "Неверный номер телефона или пароль"
