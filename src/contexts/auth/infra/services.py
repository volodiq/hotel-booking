from dataclasses import dataclass
from datetime import timedelta
from time import time

import jwt

from ..core import errors
from ..core.enums import TokenType
from ..core.services import TokenPair, TokenService


@dataclass
class PyJWTTokenService(TokenService):
    secret_key: str
    access_token_ttl: timedelta
    refresh_token_ttl: timedelta
    algorithm = "HS256"

    def create_token_pair(self, user_oid: str) -> TokenPair:
        access_token = self._encode_token(sub=user_oid, token_type=TokenType.ACCESS)
        refresh_token = self._encode_token(sub=user_oid, token_type=TokenType.REFRESH)

        return TokenPair(
            access_token=access_token,
            refresh_token=refresh_token,
        )

    def _encode_token(self, sub: str, token_type: TokenType) -> str:
        current_stamp = int(time())
        ttl = {
            TokenType.ACCESS: self.access_token_ttl,
            TokenType.REFRESH: self.refresh_token_ttl,
        }[token_type]
        ttl_secs = int(ttl.total_seconds())

        return jwt.encode(
            payload={
                "sub": sub,
                "exp": current_stamp + ttl_secs,
                "token_type": token_type.value,
            },
            key=self.secret_key,
            algorithm=self.algorithm,
        )

    def refresh_access_token(self, refresh_token: str) -> str:
        payload = self._decode_token(token=refresh_token)
        try:
            token_type = payload["token_type"]
            sub = payload["sub"]
            exp = payload["exp"]
        except KeyError:
            raise errors.InvalidTokenData()

        if token_type != TokenType.REFRESH:
            raise errors.InvalidTokenType()

        current_stamp = int(time())
        if current_stamp > exp:
            raise errors.ExpiredToken()

        return self._encode_token(sub=sub, token_type=TokenType.ACCESS)

    def _decode_token(self, token: str) -> dict:
        try:
            return jwt.decode(jwt=token, key=self.secret_key, algorithms=[self.algorithm])
        except jwt.exceptions.DecodeError:
            raise errors.InvalidTokenFormat()
        except jwt.InvalidSignatureError:
            raise errors.InvalidTokenSignature()
