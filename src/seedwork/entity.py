from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from shared.utils import utcnow


@dataclass(eq=False, frozen=True)
class Entity:
    oid: str = field(default_factory=lambda: str(uuid4()), kw_only=True)
    created_at: datetime = field(default_factory=utcnow, kw_only=True)

    def __hash__(self) -> int:
        return hash(self.oid)

    def __eq__(self, value) -> bool:
        if isinstance(value, self.__class__):
            return self.oid == value.oid
        return False
