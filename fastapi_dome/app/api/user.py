from fastapi import APIRouter
from typing import List

from app.models.db.user import User
from app.models.schemas.user import UserInModel, UserOutModel

user_router = APIRouter()


@user_router.get("/user/all/", response_model=List[UserOutModel])
async def get_users():
    users = await User.query.gino.all()
    # print(users)
    # users: List[UserOutModel] = await User.query.gino.all()
    return users


@user_router.post("/user")
async def add_user(user: UserInModel):
    rv = await User.create(nickname=user.name)
    return rv.to_dict()


@user_router.get("/user/{uid}")
async def get_user(uid: str):
    user = await User.get_or_404(uid)
    return user.to_dict()


@user_router.delete("/user/{uid}")
async def delete_user(uid: str):
    user = await User.get_or_404(uid)
    await user.delete()
    return dict(id=uid)


def init_app(app):
    app.include_router(user_router)
