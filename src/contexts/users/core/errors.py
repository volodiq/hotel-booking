from system.seedwork.errors import DomainError


class UserAlreadyExists(DomainError):
    @property
    def details(self) -> str:
        return "Пользователь с таким номером телефона уже существует"


class PhoneNumberEmpty(DomainError):
    @property
    def details(self) -> str:
        return "Номер телефона пользователя не может быть пустым"


class PhoneNumberInvalid(DomainError):
    @property
    def details(self) -> str:
        return "Номер телефона пользователя некорректен"


class PhoneNumberUnsupportedRegion(DomainError):
    @property
    def details(self) -> str:
        return "Данный регион не поддерживается"


class FirstNameEmpty(DomainError):
    @property
    def details(self) -> str:
        return "Имя пользователя не может быть пустым"


class FirstNameTooLong(DomainError):
    @property
    def details(self) -> str:
        return "Имя пользователя слишком длинное"


class LastNameEmpty(DomainError):
    @property
    def details(self) -> str:
        return "Фамилия пользователя не может быть пустой"


class LastNameTooLong(DomainError):
    @property
    def details(self) -> str:
        return "Фамилия пользователя слишком длинная"


class UserNotFound(DomainError):
    @property
    def details(self) -> str:
        return "Пользователь не найден"


class MakeHotelAdminForbidden(DomainError):
    @property
    def details(self) -> str:
        return "Не достаточно прав для назначения администраторов отелей"


class UserAlreadyHotelAdmin(DomainError):
    @property
    def details(self) -> str:
        return "Пользователь уже является администратором отеля"
