from dishka import make_async_container
from dishka.integrations.fastapi import FastapiProvider

from contexts.users.di import UsersProvider
from providers.db import DBSessionPoolProvider, DBSessionProvider
from providers.env import EnvProvider


container = make_async_container(
    FastapiProvider(),
    EnvProvider(),
    DBSessionPoolProvider(),
    DBSessionProvider(),
    UsersProvider(),
)
