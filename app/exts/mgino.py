from gino.ext.starlette import Gino as _Gino
from app.setting import config


class Gino(_Gino):
    async def set_bind(self, bind, loop=None, **kwargs):
        kwargs.setdefault("strategy", "starlette")
        if bind.drivername.startswith('mysql'):
            kwargs.pop("min_size")
            kwargs.pop("max_size")
            kwargs.setdefault("autocommit", True)
        return await super().set_bind(bind, loop=loop, **kwargs)


db = Gino(
    dsn=config.DB_DNS,
    pool_min_size=config.DB_POOL_MIN_SIZE,
    pool_max_size=config.DB_POOL_MAX_SIZE,
    echo=config.DB_ECHO,
    ssl=config.DB_SSL,
    use_connection_for_request=config.DB_USE_CONNECTION_FOR_REQUEST,
    retry_limit=config.DB_RETRY_LIMIT,
    retry_interval=config.DB_RETRY_INTERVAL,
)
