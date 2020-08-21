import pyotp

def generate_secret_key() -> str:
    """
    generate google key
    """
    
    return pyotp.random_base32()

def verify_code(secret_key, verify_code) -> bool:
    """
    Verify that the google code is correct
    :param secret_key: google secret key
    :param verify_code: google authernticator code
    """
    t = pyotp.TOTP(secret_key)
    return t.verify(verify_code)
