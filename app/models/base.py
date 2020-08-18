from app.exts.mgino import db
from app.utils.tools import time2str


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ct = db.Column(db.String(19), default=time2str)
    ut = db.Column(db.String(19), onupdate=time2str,
                   default=time2str)

    @property
    def create_time(self):
        if self.ct:
            return self.ct

    @property
    def update_time(self):
        if self.ut:
            return self.ct

    @classmethod
    def count(cls):
        return db.func.count(cls.id).gino.scalar()