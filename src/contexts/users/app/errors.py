from shared.app.errors import DomainError


class UserAlreadyExists(DomainError):
    @property
    def details(self) -> str:
        return "Пользователь с таким номером телефона уже существует"


class UserAlreadyHotelAdmin(DomainError):
    @property
    def details(self) -> str:
        return "Пользователь уже является администратором отеля"


class UserNotFound(DomainError):
    @property
    def details(self) -> str:
        return "Пользователь не найден"


class MakeHotelAdminForbidden(DomainError):
    @property
    def details(self) -> str:
        return "Не достаточно прав для назначения администраторов отелей"
