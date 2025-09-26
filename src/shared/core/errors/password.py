from kernel.seedwork.errors import DomainError


class PasswordEmpty(DomainError):
    @property
    def details(self) -> str:
        return "Пароль не может быть пустой"


class PasswordTooLong(DomainError):
    @property
    def details(self) -> str:
        return "Пароль не может быть длиннее 30 символов"


class PasswordTooShort(DomainError):
    @property
    def details(self) -> str:
        return "Пароль не может быть короче 8 символов"


class PasswordNotContainsDigit(DomainError):
    @property
    def details(self) -> str:
        return "Пароль должен содержать хотя бы одну цифру"


class PasswordNotContainsUppercase(DomainError):
    @property
    def details(self) -> str:
        return "Пароль должен содержать хотя бы одну заглавную букву"


class PasswordNotContainsLowercase(DomainError):
    @property
    def details(self) -> str:
        return "Пароль должен содержать хотя бы одну строчную букву"


class PasswordNotContainsSpecialSymbol(DomainError):
    @property
    def details(self) -> str:
        return "Пароль должен содержать хотя бы один специальный символ"
