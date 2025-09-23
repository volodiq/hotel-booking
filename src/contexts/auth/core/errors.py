from shared.core.errors import DomainError


class InvalidCredentials(DomainError):
    @property
    def details(self) -> str:
        return "Неверный номер телефона или пароль"


class InvalidTokenFormat(DomainError):
    @property
    def details(self) -> str:
        return "Передан токен в невалидном формате"


class InvalidTokenData(DomainError):
    """
    Токен был прочитан, но содержит невалидные данные.
    """

    @property
    def details(self) -> str:
        return "Передан невалидный токен"


class InvalidTokenSignature(InvalidTokenData):
    @property
    def details(self) -> str:
        return "Сигнатура токена невалидна"


class ExpiredToken(InvalidTokenData):
    @property
    def details(self) -> str:
        return "Токен устарел"


class InvalidTokenType(InvalidTokenData):
    @property
    def details(self) -> str:
        return "Токен имеет невалидный тип"
