from datetime import datetime
from pydantic import BaseModel


class Base(BaseModel):

    class Config:
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.strftime('%Y-%m-%d %H:%M:%S')
        }
