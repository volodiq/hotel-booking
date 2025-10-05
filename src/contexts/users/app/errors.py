from shared.app.errors import ApplicationError


class UserAlreadyExists(ApplicationError):
    @property
    def details(self) -> str:
        return "Пользователь с таким номером телефона уже существует"


class UserAlreadyHotelAdmin(ApplicationError):
    @property
    def details(self) -> str:
        return "Пользователь уже является администратором отеля"


class UserNotFound(ApplicationError):
    @property
    def details(self) -> str:
        return "Пользователь не найден"


class MakeHotelAdminForbidden(ApplicationError):
    @property
    def details(self) -> str:
        return "Не достаточно прав для назначения администраторов отелей"
