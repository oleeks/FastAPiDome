import traceback

from fastapi import FastAPI, Request, status
from fastapi.responses import ORJSONResponse
from fastapi.exceptions import RequestValidationError, StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import api_v1
from app.api.admin import api_admin
from app.exts import mredis, mgino

from app.setting import config
from app.utils.logging import logger
from app.utils.exceptions import AuthError, CustomizeBase

from app.core.responses import (
    NotFoundResponse,
    ValidationErrorResponse,
    ServerErrorResponse, CORJSONResponse,
)


def create_app():
    app = FastAPI(
        title="FastDome",
        description="",
        version="0.1.1",
        docs_url=config.DOCS_URL,
        openapi_url=config.OPENAPI_URL,
        # redoc_url=config.REDOC_URL,
        openapi_tags=config.TAGS_METADATA,
        default_response_class=CORJSONResponse,
    )

    mgino.db.init_app(app)

    app.include_router(
        api_v1,
        prefix="/api/v1",
        tags=['api']
    )
    app.include_router(
        api_admin,
        prefix="/admin",
        tags=['admin'],
    )

    register_exception(app)
    register_cors(app)

    register_event(app)
    return app


def register_event(app: FastAPI):
    @app.on_event("startup")
    async def startup():
        # app.extra = {'redis_cli': await mredis.get_redis()}
        app.redis_cli = await mredis.get_redis()

    @app.on_event("shutdown")
    async def shutdown():
        # redis_cli = app.extra.get('redis_cli')
        await mredis.close_redis(app.redis_cli)


def register_exception(app: FastAPI):
    """
    全局异常捕获
    :param app:
    :return:
    """

    # 捕获自定义异常
    @app.exception_handler(AuthError)
    async def query_params_exception_handler(request: Request, exc: AuthError):
        """
        捕获 自定义抛出的异常
        :param request:
        :param exc:
        :return:
        """
        logger.error(f"用户认证异常\nURL:{request.url}\nHeaders:{request.headers}")

        return ORJSONResponse(
            status_code=status.HTTP_200_OK,
            content={"msg_code": 401, "data": None, "msg": exc.err_desc},
        )

    # 捕获请求异常
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        """
        捕获 自定义抛出的异常
        :param request:
        :param exc:
        :return:
        """
        data = exc.detail
        logger.error(f"请求异常\nURL:{request.url}\nHeaders:{request.headers}\n{data}")
        return NotFoundResponse(content=data)

    # 捕获参数 验证错误
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """
        捕获请求参数 验证错误
        :param request:
        :param exc:
        :return:
        """

        data = exc.errors()[0]["msg"]
        print(traceback.format_exc())
        logger.error(f"参数错误\nURL:{request.url}\nHeaders:{request.headers}\n{exc.errors()[0]['loc']}\n{data}")
        return ValidationErrorResponse(content=exc.errors()[0]['loc'])

    # 捕获全部异常
    @app.exception_handler(CustomizeBase)
    async def all_exception_handler(request: Request, exc: CustomizeBase):
        logger.error(f"全局异常\nURL:{request.url}\nHeaders:{request.headers}\n{exc.err_desc}\n")
        # return CORJSONResponse(msg='111111', msg_code=1234)
        return ServerErrorResponse(msg=exc.err_desc)


def register_cors(app: FastAPI):
    """
    支持跨域
    :param app:
    :return:
    """

    app.add_middleware(
        CORSMiddleware,
        allow_origin_regex='https?://.*',
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
