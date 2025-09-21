import datetime
from functools import partial


utcnow = partial(datetime.datetime.now, datetime.UTC)
