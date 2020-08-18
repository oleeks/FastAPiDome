
class CustomizeBase(Exception):
    def __init__(self, err_desc: str = "用户认证异常"):
        self.err_desc = err_desc

class AuthError(CustomizeBase):
    pass




