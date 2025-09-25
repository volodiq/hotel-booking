from kernel.seedwork.errors import DomainError


class InvalidCredentials(DomainError):
    @property
    def details(self) -> str:
        return "Неверный номер телефона или пароль"
