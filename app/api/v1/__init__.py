from fastapi import APIRouter

from app.api.v1.user import router as user_router
from app.api.v1.posts import router as posts_router
from app.api.v1.ws import router as ws_router
api_v1 = APIRouter()

api_v1.include_router(user_router)
api_v1.include_router(posts_router)
# api_v1.include_router(ws_router, prefix='/ws')
api_v1.add_api_websocket_route('/ws', endpoint=ws_router)
