import asyncio
from aioredis import create_redis_pool, Redis


from app.setting import config
from app.utils.exceptions import CustomizeBase


async def get_redis():
    try:
        pool = await create_redis_pool(
            address=(config.REDIS_HOST, config.REDIS_PORT),
            password=config.REDIS_PASSWORD,
            db=config.REDIS_DB,
            minsize=config.REDIS_POOL_MIN,
            maxsize=config.REDIS_POOL_MAX,
            encoding=config.ENCODING,
        )
        return pool
    except ConnectionRefusedError as e:

        raise CustomizeBase(err_desc=f'cannot connect to redis on: {config.REDIS_HOST}:{config.REDIS_PASSWORD} {e}')


async def close_redis(redis_cli: Redis):
    redis_cli.close()
    await redis_cli.wait_closed()

