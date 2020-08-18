import shortuuid
from fastapi import APIRouter

from app.models import Posts

router = APIRouter()

@router.post('/add')
async def add_posts():
    p = await Posts.create(id=shortuuid.uuid(),username='fantix')