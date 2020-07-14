from datetime import datetime

import shortuuid

from app.exts import db
from app.utils.tools import time2str
class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.String(100), primary_key=True, default=shortuuid.uuid)
    ct = db.Column(db.String(19))
    ut = db.Column(db.String(19), onupdate=time2str,
                   default=time2str)

    def __init__(self):
        self.ct = self.ut = time2str()

    @property
    def create_time(self):
        if self.ct:
            return self.ct

    @property
    def update_time(self):
        if self.ut:
            return self.ct
