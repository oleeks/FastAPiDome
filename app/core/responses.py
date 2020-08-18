from typing import Any
import typing
import orjson
from fastapi.responses import JSONResponse

from starlette.background import BackgroundTask


class CORJSONResponse(JSONResponse):
    msg = "OK"
    msg_code = 0

    def __init__(
            self,
            content: typing.Any = None,
            status_code: int = 200,
            headers: dict = None,
            media_type: str = None,
            background: BackgroundTask = None,
            msg: str = None,
            msg_code: int = 200
    ) -> None:
        self.msg = msg if msg else self.msg
        self.msg_code = msg_code if msg_code else self.msg_code
        # if msg:
        #     self.msg = msg
        # if msg_code:
        #
        #     self.msg_code = msg_code

        super().__init__(content, status_code, headers, media_type, background)

    def render(self, content: Any) -> bytes:
        reps_data = {
            "msg_code": self.msg_code,
            "msg": self.msg,
            "data": content
        }

        assert orjson is not None, "orjson must be installed to use ORJSONResponse"
        return orjson.dumps(reps_data)


class AuthFailedResponse(CORJSONResponse):
    msg_code = 400
    msg = "FAIL"


class NotFoundResponse(CORJSONResponse):
    msg_code = 404
    msg = "FAIL"


class ValidationErrorResponse(CORJSONResponse):
    msg_code = 406
    msg = "FAIL"


class ServerErrorResponse(CORJSONResponse):
    pass
