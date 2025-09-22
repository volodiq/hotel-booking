from dataclasses import dataclass
from datetime import timedelta
from time import time

import jwt

from ..core.enums import TokenType
from ..core.services import TokenPair, TokenService


@dataclass
class PyJWTTokenService(TokenService):
    secret_key: str
    access_token_ttl: timedelta
    refresh_token_ttl: timedelta

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
        )
