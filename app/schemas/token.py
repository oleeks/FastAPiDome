from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    token: str
    token_type: str = "Bearer"


class TokenPayload(BaseModel):
    uid: Optional[int] = None
    uuid: str = None
    token: str = None

