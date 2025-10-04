from shared.core.errors import DomainError


class UserAlreadyHotelAdmin(DomainError):
    @property
    def details(self) -> str:
        return "Пользователь уже является администратором отеля"
