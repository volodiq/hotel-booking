from shared.core.errors import DomainError


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


class PasswordIsEmpty(DomainError):
    @property
    def details(self) -> str:
        return "Пароль пользователя не может быть пустым"


class PasswordTooShort(DomainError):
    @property
    def details(self) -> str:
        return "Пароль пользователя слишком короткий"


class PasswordTooLong(DomainError):
    @property
    def details(self) -> str:
        return "Пароль пользователя слишком длинный"


class PasswordDontContainsUppercase(DomainError):
    @property
    def details(self) -> str:
        return "Пароль пользователя должен содержать хотя бы одну заглавную букву"


class PasswordDontContainsDigit(DomainError):
    @property
    def details(self) -> str:
        return "Пароль пользователя должен содержать хотя бы одну цифру"


class PasswordDontContainsSpecialSymbol(DomainError):
    @property
    def details(self) -> str:
        return "Пароль пользователя должен содержать хотя бы один специальный символ"
