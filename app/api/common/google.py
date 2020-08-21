from fastapi import APIRouter
from app.utils import google
from app.schemas.common  import  GoogleCode, Google
router = APIRouter()


@router.get('/get-secret-key', response_model=Google)
async def generate_secret_key():
    secret_key = google.generate_secret_key()
    print(secret_key)
    return {"secret_key":secret_key}

@router.post('/verify-code')
async def google_verify_code(code: GoogleCode):
    print(code)
    verify_result = google.verify_code('3YN4R46CPLQ3ONCQ', code)
    return verify_result

# TODO:待完善关联用户
