from sqlalchemy import Column, String
from .base import BaseModel


class User(BaseModel):
    __tablename__ = "user"
    nickname = Column(String(50))
