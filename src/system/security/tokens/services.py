from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import timedelta
from time import time

import jwt

from . import dtos, errors


class TokenService(ABC):
    @abstractmethod
    def encode(self, principal: dtos.Principal, token_type: dtos.TokenType) -> str: ...

    @abstractmethod
    def decode(self, token: str, token_type: dtos.TokenType) -> dtos.Principal: ...


@dataclass
class PyJWTTokenService(TokenService):
    secret_key: str
    access_token_ttl: timedelta
    refresh_token_ttl: timedelta
    algorithm = "HS256"

    def encode(self, principal: dtos.Principal, token_type: dtos.TokenType) -> str:
        current_stamp = int(time())
        ttl = {
            dtos.TokenType.ACCESS: self.access_token_ttl,
            dtos.TokenType.REFRESH: self.refresh_token_ttl,
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

    def decode(self, token: str, token_type: dtos.TokenType) -> dtos.Principal:
        try:
            payload = jwt.decode(jwt=token, key=self.secret_key, algorithms=[self.algorithm])
        except jwt.exceptions.DecodeError:
            raise errors.InvalidTokenFormat()
        except jwt.InvalidSignatureError:
            raise errors.InvalidTokenSignature()
        except jwt.ExpiredSignatureError:
            raise errors.ExpiredToken()

        if payload["token_type"] != token_type:
            raise errors.InvalidTokenType()

        return dtos.Principal(
            sub=payload["sub"],
            roles=payload.get("roles", []),
        )
