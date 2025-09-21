import datetime
from functools import partial
import hashlib


def calculate_password_hash(raw_password):
    return hashlib.sha256(raw_password.encode()).hexdigest()


utcnow = partial(datetime.datetime.now, datetime.UTC)
