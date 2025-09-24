from datetime import datetime
from typing import Annotated

from sqlalchemy import types
from sqlalchemy.orm import mapped_column

from utils.utcnow import utcnow


DateTime = Annotated[
    datetime,
    mapped_column(
        types.DateTime,
        default=utcnow,
    ),
]

String = Annotated[
    str,
    mapped_column(
        types.String,
        nullable=False,
    ),
]

Bool = Annotated[
    bool,
    mapped_column(
        types.Boolean,
        nullable=False,
    ),
]
