from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import timedelta
from enum import StrEnum, auto
from time import time

from dishka import Provider, Scope, provide
import jwt

from tech.env import Env


@dataclass
class SecurityException(Exception):
    """
    Ошибка безопасности.
    Должны перехватываться на уровне фреймворка презентационного слоя
    """

    @property
    def details(self) -> str:
        return "Токен не валиден"


class NotAuthenticated(SecurityException):
    @property
    def details(self) -> str:
        return "Пользователь не авторизован"


class InvalidTokenFormat(SecurityException):
    @property
    def details(self) -> str:
        return "Передан токен в невалидном формате"


class InvalidTokenData(SecurityException):
    """
    Токен был прочитан, но содержит невалидные данные.
    """

    @property
    def details(self) -> str:
        return "Передан невалидный токен"


class InvalidTokenSignature(InvalidTokenData):
    @property
    def details(self) -> str:
        return "Сигнатура токена невалидна"


class ExpiredToken(InvalidTokenData):
    @property
    def details(self) -> str:
        return "Токен устарел"


class InvalidTokenType(InvalidTokenData):
    @property
    def details(self) -> str:
        return "Токен имеет невалидный тип"


class TokenType(StrEnum):
    ACCESS = auto()
    REFRESH = auto()


@dataclass
class Principal:
    sub: str
    roles: list[str] = field(default_factory=list)


class TokenService(ABC):
    @abstractmethod
    def encode(self, principal: Principal, token_type: TokenType) -> str: ...

    @abstractmethod
    def decode(self, token: str, token_type: TokenType) -> Principal: ...


@dataclass
class PyJWTTokenService(TokenService):
    secret_key: str
    access_token_ttl: timedelta
    refresh_token_ttl: timedelta
    algorithm = "HS256"

    def encode(self, principal: Principal, token_type: TokenType) -> str:
        current_stamp = int(time())
        ttl = {
            TokenType.ACCESS: self.access_token_ttl,
            TokenType.REFRESH: self.refresh_token_ttl,
        }[token_type]
        ttl_secs = int(ttl.total_seconds())

        return jwt.encode(
            payload={
                "sub": principal.sub,
                "roles": principal.roles,
                "exp": current_stamp + ttl_secs,
                "token_type": token_type.value,
            },
            key=self.secret_key,
            algorithm=self.algorithm,
        )

    def decode(self, token: str, token_type: TokenType) -> Principal:
        try:
            payload = jwt.decode(jwt=token, key=self.secret_key, algorithms=[self.algorithm])
        except jwt.exceptions.DecodeError:
            raise InvalidTokenFormat()
        except jwt.InvalidSignatureError:
            raise InvalidTokenSignature()

        if payload["token_type"] != token_type:
            raise InvalidTokenType()
        if payload["exp"] < int(time()):
            raise ExpiredToken()

        return Principal(
            sub=payload["sub"],
            roles=payload.get("roles", []),
        )


class SecurityProvider(Provider):
    @provide(scope=Scope.APP)
    def token_service(self, env: Env) -> TokenService:
        return PyJWTTokenService(
            secret_key=env.SECRET_KEY,
            access_token_ttl=timedelta(hours=1),
            refresh_token_ttl=timedelta(weeks=1),
        )
