from fastapi import APIRouter

from .google import router as google_router

common_api = APIRouter()

common_api.include_router(google_router, prefix='/google')

