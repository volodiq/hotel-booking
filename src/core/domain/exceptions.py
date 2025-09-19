from abc import ABC, abstractmethod


class DomainError(Exception, ABC):
    """
    Базовое исключение для доменных ошибок.
    Определяет геттер details, возвращающий подробное описание для клиента.
    """

    @property
    @abstractmethod
    def details(self) -> str: ...
