from typing import Optional
from aioredis import Redis
from fastapi import Header, Depends, Request

from app.setting import config
from app.utils.exceptions import AuthError
from app.models.user import AdminUser, User
from app.schemas.token import TokenPayload
from app.core.jwt import check_token
from app.core import curd_redis


async def get_redis_cli(request: Request) -> Redis:
    return request.app.redis_cli


async def get_token_data(token: Optional[str] = Header(None),
                         ) -> TokenPayload:
    """
    根据header中token 获取存储的数据
    :param redis_cli:
    :param token:
    :return:
    """
    if not token:
        raise AuthError(err_desc='headers not found token')

    token_data = check_token(config.SECRET_KEY, config.ALGORITHM, token)

    return token_data


async def get_current_admin(current_token_data: TokenPayload = Depends(get_token_data),
                            redis_cli: Redis = Depends(get_redis_cli)) -> AdminUser:
    user = await AdminUser.get(current_token_data.uid)

    rv = await curd_redis.auth_get_token(redis_cli, current_token_data.uuid)

    if rv != current_token_data.token:
        raise AuthError(err_desc='token is fail')
    if not user or not (user.user_id == current_token_data.uuid):
        raise AuthError(err_desc="user not found")

    return user


async def get_current_user(current_token_data: TokenPayload = Depends(get_token_data),
                           redis_cli: Redis = Depends(get_redis_cli)) -> User:
    user = await User.get(current_token_data.uid)

    if not user:
        raise AuthError(err_desc="user not found")
    rv = await redis_cli.get(f"user:token:{user.user_id}")

    if rv != current_token_data.token:
        raise AuthError(err_desc='token is fail')
    if not user or not (user.user_id == current_token_data.uuid):
        raise AuthError(err_desc="user not found")

    return user
