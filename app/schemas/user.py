from typing import Optional, List, Any
from pydantic import EmailStr, Field, validator
from datetime import datetime
from app.schemas import Base

class UserBase(Base):
    email: Optional[EmailStr] = None
    phone: str = None
    is_active: Optional[bool] = True

class AdminUserInfo(UserBase):
    nickname: str
    role_id: bool = None
    ct: datetime = Field(default_factory=datetime.utcnow)

class AllAdminUser(Base):
    count: int = 0
    users: List[AdminUserInfo]


class AdminUserCreate(UserBase):
    nickname: str
    password: str
    role_id: int

class AdminUserUpdate(UserBase):
    pass


class UserAuth(Base):
    username: str
    password: str


class User(Base):
    user_id: str = Field(...)
    nickname: Optional[str] = None
    phone: str = Field(..., min_length=8, max_length=11)

class UserRegister(User):
    password: str = Field(...)
    password2: str = Field(...)

    @validator('password2')
    def passwords_match(cls, v, values):
        if v != values['password']:
            raise ValueError('passwords do not match')

        return v

class UserLogin(Base):
    phone: str = Field(..., min_length=8, max_length=11)
    password: str = Field(...)

class UserUpdate(User):
    pass
