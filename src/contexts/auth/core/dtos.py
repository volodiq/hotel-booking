from dataclasses import dataclass


@dataclass
class TokenPair:
    access_token: str
    refresh_token: str
