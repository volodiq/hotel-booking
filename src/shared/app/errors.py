from abc import ABC, abstractmethod


class ApplicationError(Exception, ABC):
    """
    Базовое исключение для ошибок уровня бизнес-логики.
    Определяет геттер details, возвращающий подробное описание для клиента.
    Перехватывается на уровне презентационного слоя.
    """

    @property
    @abstractmethod
    def details(self) -> str: ...


class SecurityException(Exception):
    """
    Ошибка безопасности.
    Должны перехватываться на уровне презентационного слоя
    """

    @property
    def details(self) -> str:
        return "Токен не валиден"


class InvalidTokenFormat(SecurityException):
    @property
    def details(self) -> str:
        return "Передан токен в невалидном формате"


class InvalidTokenSignature(SecurityException):
    @property
    def details(self) -> str:
        return "Сигнатура токена невалидна"


class ExpiredToken(SecurityException):
    @property
    def details(self) -> str:
        return "Токен устарел"


class InvalidTokenType(SecurityException):
    @property
    def details(self) -> str:
        return "Токен имеет невалидный тип"
