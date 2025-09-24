from dataclasses import dataclass


@dataclass
class SecurityException(Exception):
    """
    Ошибка безопасности.
    Должны перехватываться на уровне фреймворка презентационного слоя
    """

    @property
    def details(self) -> str:
        return "Токен не валиден"


class NotAuthenticated(SecurityException):
    @property
    def details(self) -> str:
        return "Пользователь не авторизован"


class InvalidTokenFormat(SecurityException):
    @property
    def details(self) -> str:
        return "Передан токен в невалидном формате"


class InvalidTokenData(SecurityException):
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
