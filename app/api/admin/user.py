from typing import List, Optional
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from fastapi import APIRouter, Depends

from app.core.deps import get_current_admin
from app.models.user import AdminUser

from app.core.responses import AuthFailedResponse, ValidationErrorResponse
from app.schemas import user, common

from app.api.admin.curd.user import curd_admin
from app.utils.exceptions import CustomizeBase

router = APIRouter()


@router.get("/info", summary="获取当前用户信息", response_model=user.AdminUserInfo)
async def get_user_info(current_user: AdminUser = Depends(get_current_admin)):
    if not current_user:
        return AuthFailedResponse(msg="权限不足")
    return current_user


@router.post("/add", summary="新增用户", response_model=user.AdminUserInfo)
async def add_user(user_in: user.AdminUserCreate, current_user: AdminUser = Depends(get_current_admin)):
    if not curd_admin.is_superuser(current_user):
        return AuthFailedResponse(content="权限不足")

    check_user_in = user_in.copy()
    user_is_exist = await curd_admin.is_exist(check_user_in)

    if not user_is_exist:
        return ValidationErrorResponse(content="帐户已存在")

    await curd_admin.create_user(obj_in=user_in)

    return user_in


@router.post("/all", response_model=List[user.AdminUserInfo])
# @router.post("/all", summary="获取所有用户信息", response_model=user.AllAdminUser)
async def get_user_all(
        page: common.Page,
        # current_user: AdminUser = Depends(get_current_admin)
):
    # if not curd_admin.is_superuser(current_user):
    #     return AuthFailedResponse(content="权限不足")
    user_count = await curd_admin.count
    user_all = await curd_admin.get_multi(skip=page.page, limit=page.size)

    return {"count": user_count, "users": user_all}
