import bcrypt

from ..app.interfaces import PasswordService


class BcryptPasswordService(PasswordService):
    def calculate_password_hash(self, raw_password: str) -> str:
        return bcrypt.hashpw(raw_password.encode(), bcrypt.gensalt()).decode()

    def check_password(self, raw_password: str, password_hash: str) -> bool:
        return bcrypt.checkpw(raw_password.encode(), password_hash.encode())
