import hashlib

from ..core.services import PasswordHashService


class SHA256PasswordHashService(PasswordHashService):
    def calculate_password_hash(self, raw_password: str) -> str:
        return hashlib.sha256(raw_password.encode()).hexdigest()
