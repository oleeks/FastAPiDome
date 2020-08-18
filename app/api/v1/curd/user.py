from typing import Optional, Any

from app.core.security import verify_password, get_password_hash
from app.models.user import User
from app.schemas.user import UserRegister,UserUpdate
from app.core.curd_base import CRUDBase
from app.utils.exceptions import CustomizeBase


class CRUDUser(CRUDBase[User, UserRegister, UserUpdate]):

    async def get_user(self, *, account: str) -> Optional[User]:
        """
        通过phone或email获取用户
        """
        user = await self.model.query.where(User.phone == account).gino.first()
        return user

    async def create_user(self, *, obj_in: UserRegister) -> Any:
        user = await self.get_user(account=obj_in.phone)

        if user:
            raise CustomizeBase(err_desc="帐户已存在")

        db_obj = self.model(
            nickname=obj_in.nickname,
            phone=obj_in.phone,
            hashed_password=get_password_hash(obj_in.password),
        )
        await db_obj.create()
        return db_obj

    async def authenticate(self, *, account: str, password: str) -> Optional[User]:
        user = await self.get_user(account=account)
        if not user:
            raise CustomizeBase(err_desc="帐户或密码错误")
        if not verify_password(password, user.hashed_password):
            raise CustomizeBase(err_desc="帐户或密码错误")
        return user


curd_user = CRUDUser(User)
