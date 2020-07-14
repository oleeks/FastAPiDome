from app.exts import db
from .base import BaseModel


class User(BaseModel):
    __tablename__ = "user"
    nickname = db.Column(db.String(50))