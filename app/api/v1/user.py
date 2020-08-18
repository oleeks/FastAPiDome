from aioredis import Redis
from fastapi import APIRouter, Depends

from app.core import security
from app.core.deps import get_redis_cli, get_current_user
from app.api.v1.curd.user import curd_user
from app.models import User
from app.schemas import user
from app.schemas.token import Token
from app.utils.logging import logger

router = APIRouter()


@router.post("/register", response_model=user.User)
async def register_user(user_reg: user.UserRegister):
    await curd_user.create_user(obj_in=user_reg.copy())
    return user_reg


@router.post("/login", response_model=Token)
async def login(user_login: user.UserLogin, redis_cli: Redis = Depends(get_redis_cli)):
    user_info = await curd_user.authenticate(account=user_login.phone, password=user_login.password)
    token_data = {"uid": user_info.id, "uuid": user_info.user_id}
    access_token = security.create_access_token(
        token_data,
    )
    await redis_cli.set(f"user:token:{user_info.user_id}", access_token)
    return Token(token=access_token)


@router.get("/logout", summary="退出登录")
async def auth_logout(current_user: User = Depends(get_current_user), redis_cli: Redis = Depends(get_redis_cli)):
    await redis_cli.delete(f"user:token:{current_user.user_id}")



