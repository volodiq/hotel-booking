from shared.core.errors import DomainError


class FirstNameEmpty(DomainError):
    @property
    def details(self) -> str:
        return "Имя администратора отелей не может быть пустым"


class FirstNameTooLong(DomainError):
    @property
    def details(self) -> str:
        return "Имя администратора отелей не может быть длиннее 50 символов"


class LastNameTooLong(DomainError):
    @property
    def details(self) -> str:
        return "Фамилия администратора отелей не может быть длиннее 50 символов"


class LastNameEmpty(DomainError):
    @property
    def details(self) -> str:
        return "Фамилия администратора отелей не может быть пустой"


class MiddleNameTooLong(DomainError):
    @property
    def details(self) -> str:
        return "Отчество администратора отелей не может быть длиннее 50 символов"


class PhoneNumberEmpty(DomainError):
    @property
    def details(self) -> str:
        return "Номер телефона администратора отелей не может быть пустым"


class PhoneNumberUnsupportedRegion(DomainError):
    @property
    def details(self) -> str:
        return "Данный регион номера телефона не поддерживается"


class PhoneNumberInvalid(DomainError):
    @property
    def details(self) -> str:
        return "Номер телефона администратора отелей некорректен"


class EmailEmpty(DomainError):
    @property
    def details(self) -> str:
        return "Email администратора отелей не может быть пустой"


class EmailInvalid(DomainError):
    @property
    def details(self) -> str:
        return "Email администратора отелей некорректен"


class EmailUnsupportedDomain(DomainError):
    @property
    def details(self) -> str:
        return "Данный домен email не поддерживается"


class PasswordTooLong(DomainError):
    @property
    def details(self) -> str:
        return "Пароль администратора отелей не может быть длиннее 30 символов"


class PasswordEmpty(DomainError):
    @property
    def details(self) -> str:
        return "Пароль администратора отелей не может быть пустой"


class PasswordTooShort(DomainError):
    @property
    def details(self) -> str:
        return "Пароль администратора отелей не может быть короче 8 символов"


class PasswordNotContainsDigit(DomainError):
    @property
    def details(self) -> str:
        return "Пароль администратора отелей должен содержать хотя бы одну цифру"


class PasswordNotContainsUppercase(DomainError):
    @property
    def details(self) -> str:
        return "Пароль администратора отелей должен содержать хотя бы одну заглавную букву"


class PasswordNotContainsLowercase(DomainError):
    @property
    def details(self) -> str:
        return "Пароль администратора отелей должен содержать хотя бы одну строчную букву"


class PasswordNotContainsSpecialSymbol(DomainError):
    @property
    def details(self) -> str:
        return "Пароль администратора отелей должен содержать хотя бы один специальный символ"


class HotelAdminAlreadyExists(DomainError):
    @property
    def details(self) -> str:
        return "Администратор с таким номером телефона уже существует"


class HotelAdminAlreadyBanned(DomainError):
    @property
    def details(self) -> str:
        return "Данный администратор уже заблокирован"
