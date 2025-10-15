from dataclasses import dataclass


@dataclass
class TokenPair:
    access_token: str
    refresh_token: str


@dataclass
class VerifyUserPasswordOut:
    is_valid: bool
    user_oid: str | None
    is_superuser: bool | None
    is_hotel_admin: bool | None
