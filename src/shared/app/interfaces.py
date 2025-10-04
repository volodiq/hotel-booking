from abc import ABC, abstractmethod

from . import dtos


class PasswordService(ABC):
    @abstractmethod
    def calculate_password_hash(self, raw_password: str) -> str: ...

    @abstractmethod
    def check_password(self, raw_password: str, password_hash: str) -> bool: ...


class TokenService(ABC):
    @abstractmethod
    def encode(self, principal: dtos.Principal, token_type: dtos.TokenType) -> str: ...

    @abstractmethod
    def decode(self, token: str, token_type: dtos.TokenType) -> dtos.Principal: ...
