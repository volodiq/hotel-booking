from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Generic, TypeVar


VT = TypeVar("VT")


@dataclass(frozen=True)
class ValueObject(ABC, Generic[VT]):
    value: VT

    def __post_init__(self):
        self.validate()

    @abstractmethod
    def validate(self):
        """
        Проверяет значение, если оно не валидно, то генерирует
        core.domain.errors.DomainError
        """

        ...
