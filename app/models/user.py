import shortuuid
from sqlalchemy import Column, String, Integer, BIGINT, BOOLEAN

from app.models.base import BaseModel


class AdminUser(BaseModel):
    """
    管理员表
    """
    __tablename__ = "admin_user"
    user_id = Column(String(32), default=shortuuid.uuid, unique=True, comment="用户id")
    email = Column(String(128), unique=True, index=True, nullable=False, comment="邮箱")
    phone = Column(String(16), unique=True, index=True, nullable=True, comment="手机号")
    nickname = Column(String(128), comment="管理员昵称")
    hashed_password = Column(String(128), nullable=False, comment="密码")
    is_active = Column(BOOLEAN, default=False, comment="0=未激活 1=激活", server_default="0")
    active = Column(BOOLEAN, default=False, comment="0=未激活 1=激活", server_default="0")
    role_id = Column(Integer, comment="角色表")
    is_superuser = Column(BOOLEAN, default=False, comment="0=普通用户 1=管理员", server_default="0")
    __table_args__ = ({'comment': '管理员表'})



class AdminRole(BaseModel):
    """
    角色表设计
    """
    __tablename__ = "admin_role"
    role_id = Column(Integer, primary_key=True, index=True, comment="角色Id")
    role_name = Column(String(64), comment="角色名字")
    permission_id = Column(BIGINT, comment="权限ID")
    re_mark = Column(String(128), comment="备注信息")
    __table_args__ = ({'comment': '管理员角色'})


class User(BaseModel):
    __tablename__ = "user"
    user_id = Column(String(32), default=shortuuid.uuid, unique=True, comment="用户id")
    nickname = Column(String(50))
    phone = Column(String(11), unique=True, index=True, nullable=False, comment="手机号")
    hashed_password = Column(String(128), nullable=False, comment="密码")