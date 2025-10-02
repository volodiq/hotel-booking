from abc import ABC, abstractmethod
import hashlib
import secrets


class PasswordService(ABC):
    @abstractmethod
    def calculate_password_hash(self, raw_password: str) -> str: ...

    @abstractmethod
    def check_password(self, raw_password: str, password_hash: str) -> bool: ...


class SHA256PasswordService(PasswordService):
    def calculate_password_hash(self, raw_password: str) -> str:
        return hashlib.sha256(raw_password.encode()).hexdigest()

    def check_password(self, raw_password: str, password_hash: str) -> bool:
        return secrets.compare_digest(
            password_hash,
            self.calculate_password_hash(raw_password),
        )
