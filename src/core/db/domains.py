from datetime import datetime
from typing import Annotated

from sqlalchemy import types
from sqlalchemy.orm import mapped_column

from core.utils import utcnow


DateTime = Annotated[
    datetime,
    mapped_column(
        types.DateTime,
        default=utcnow,
    ),
]
