import copy
from typing import Optional, Any
from sqlalchemy import or_

from app.core.security import verify_password, get_password_hash
from app.models.user import AdminUser
from app.schemas.user import AdminUserCreate, AdminUserUpdate
from app.core.curd_base import CRUDBase


class CRUDUser(CRUDBase[AdminUser, AdminUserCreate, AdminUserUpdate]):

    async def get_user(self, *, account: str) -> Optional[AdminUser]:
        """
        通过phone或email获取用户
        """
        user = await self.model.query.where(
            or_(AdminUser.phone == account, AdminUser.email == account)).gino.first()
        return user

    async def create_user(self, *, obj_in: AdminUserCreate) -> Any:
        db_obj = self.model(
            nickname=obj_in.nickname,
            email=obj_in.email,
            phone=obj_in.phone,
            hashed_password=get_password_hash(obj_in.password),
            role_id=obj_in.role_id,
            is_active=obj_in.is_active
        )
        await db_obj.create()
        return db_obj

    async def authenticate(self, *, account: str, password: str) -> Optional[AdminUser]:
        user = await self.get_user(account=account)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    @staticmethod
    def is_active(user: AdminUser) -> bool:
        return user.is_active

    @staticmethod
    def is_superuser(user: AdminUser) -> bool:
        return user.is_superuser

    async def is_exist(self, user_in) -> bool:
        if user_in.phone:
            user_in.phone = await self.model.query.where(AdminUser.phone == user_in.phone).gino.first()

        if user_in.email:
            user_in.email = await self.model.query.where(AdminUser.email == user_in.email).gino.first()

        if user_in.email or user_in.phone:
            return False
        return True


curd_admin = CRUDUser(AdminUser)
