from fastapi import APIRouter
from app.api.admin.auth import router as auth_router
from app.api.admin.user import router as user_router

admin_api = APIRouter()

admin_api.include_router(auth_router, prefix='/auth')
admin_api.include_router(user_router, prefix='/user')
