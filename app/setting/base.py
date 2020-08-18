import os
import secrets
from typing import Optional, List
from pydantic import BaseSettings
from sqlalchemy.engine.url import URL

class Config(BaseSettings):
    ENCODING: str= 'utf-8'
    SECRET_KEY = secrets.token_urlsafe(32)
    # 文档地址
    DOCS_URL: str = "/api/v1/docs"
    # 文档关联请求数据接口
    OPENAPI_URL: str = "/api/v1/openapi.json"
    # 禁用 redoc 文档
    REDOC_URL: Optional[str] = False

    TAGS_METADATA: List[dict] = [
        {
            "name": "首页",
            "description": "API接口",
        },
    ]

    # 配置mysql环境
    DB_DRIVER: str = "mysql"
    DB_HOST: str = '192.168.50.90'
    DB_PORT: str = '3306'
    DB_USER: str = 'oleeks'
    DB_PASSWORD: str = 'oleeks'
    DB_DATABASE: str = 'my_dome'
    DB_POOL_MIN_SIZE: int = 1
    DB_POOL_MAX_SIZE: int = 16
    DB_ECHO = False
    DB_SSL: Optional[str] = None
    DB_USE_CONNECTION_FOR_REQUEST: bool = False
    DB_RETRY_LIMIT: int = 1
    DB_RETRY_INTERVAL: int = 1
    DB_DNS = URL(
        drivername=DB_DRIVER,
        username=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_DATABASE,
    )

    # 配置redis环境
    REDIS_DB = 0
    REDIS_HOST = '192.168.50.90'
    REDIS_PORT = 6379
    REDIS_PASSWORD = 123456
    REDIS_POOL_MIN: int = 0
    REDIS_POOL_MAX: int = 10
    # token过期时间 60 minutes * 24 hours * 30 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30
    ALGORITHM: str = "HS256"


config = Config()
