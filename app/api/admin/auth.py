
from fastapi import APIRouter, Depends
from aioredis import Redis
from app.api.admin.curd.user import curd_admin
from app.core import security
from app.core import curd_redis
from app.core.deps import get_current_admin, get_redis_cli
from app.models.user import AdminUser

from app.utils.logging import logger

from app.schemas import user, token

from app.core.responses import AuthFailedResponse, ValidationErrorResponse

router = APIRouter()


@router.post("/login", summary="登录认证", response_model=token.Token)
async def auth_login(user_auth: user.UserAuth, redis_cli: Redis = Depends(get_redis_cli)):
    # 验证用户
    user_info = await curd_admin.authenticate(account=user_auth.username, password=user_auth.password)
    if not user_info:
        logger.info(f"用户登录认证错误: account: {user_auth.username} password:{user_auth.password}")
        return ValidationErrorResponse(content="用户不存在或帐户密码错误")

    if curd_admin.is_active(user_info):
        logger.info(f"用户未激活: account: {user_auth.username}")
        return AuthFailedResponse(content="用户未激活")
    token_data = {"uid": user_info.id,
                  "uuid": user_info.user_id}
    access_token = security.create_access_token(
        token_data,
    )
    logger.info(f"登录成功: account: {user_auth.username}")
    await curd_redis.auth_set_token(redis_cli, user_info.user_id, access_token)

    return token.Token(token=access_token)


@router.get("/logout", summary="退出登录")
async def auth_logout(current_user: AdminUser = Depends(get_current_admin), redis_cli: Redis = Depends(get_redis_cli)):
    await curd_redis.auth_del_token(redis_cli, current_user.user_id)


