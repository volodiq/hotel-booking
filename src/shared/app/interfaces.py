from abc import ABC, abstractmethod


class PasswordService(ABC):
    @abstractmethod
    def calculate_password_hash(self, raw_password: str) -> str: ...

    @abstractmethod
    def check_password(self, raw_password: str, password_hash: str) -> bool: ...
