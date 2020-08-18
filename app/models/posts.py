import shortuuid
from sqlalchemy import Column, String

from app.exts.mgino import db


class Posts(db.Model):
    __tablename__ = "posts"
    id = Column(String(100), primary_key=True)
    username = Column(String(50))