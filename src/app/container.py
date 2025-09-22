from dishka import make_async_container
from dishka.integrations.fastapi import FastapiProvider

from contexts.auth.di import AuthProvider
from contexts.users.di import UsersProvider
from shared.providers.db import DBProvider
from shared.providers.env import EnvProvider


container = make_async_container(
    FastapiProvider(),
    EnvProvider(),
    DBProvider(),
    UsersProvider(),
    AuthProvider(),
)
