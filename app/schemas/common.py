from pydantic import Field

from app.schemas import Base


class Page(Base):
    size: int = Field(..., example=10)
    page: int = Field(..., example=1)