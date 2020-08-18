from fastapi import APIRouter
from app.api.admin.auth import router as auth_router
from app.api.admin.user import router as user_router

api_admin = APIRouter()

api_admin.include_router(auth_router, prefix='/auth')
api_admin.include_router(user_router, prefix='/user')
