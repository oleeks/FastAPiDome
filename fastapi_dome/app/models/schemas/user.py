from pydantic import BaseModel


class UserInModel(BaseModel):
    name: str


class UserOutModel(UserInModel):
    id = str
