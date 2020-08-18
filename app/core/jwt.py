from pydantic import ValidationError
from typing import Optional
from jose import jwt
from fastapi import Header

from app.schemas.token import TokenPayload
from app.utils.exceptions import AuthError


def check_token(secrets_key, algorithm,
                token: Optional[str] = Header(None)
                ) -> TokenPayload:
    """
    只解析验证token
    :param algorithm:
    :param secrets_key:
    :param token:
    :return:
    """

    try:
        payload = jwt.decode(
            token,
            secrets_key, algorithms=algorithm
        )
        return TokenPayload(**payload, token=token)
    except (jwt.JWTError, ValidationError, AttributeError) as e:
        raise AuthError(err_desc=f"access token fail, de {e}")


def create_token(to_encode, secrets_key, algorithm):
    return jwt.encode(to_encode, secrets_key, algorithm=algorithm)
