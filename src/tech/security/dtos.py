from dataclasses import dataclass, field
from enum import StrEnum, auto


class TokenType(StrEnum):
    ACCESS = auto()
    REFRESH = auto()


@dataclass
class Principal:
    sub: str
    roles: list[str] = field(default_factory=list)
