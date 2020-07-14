from fastapi_dome.app.core.mgino import Gino
from fastapi_dome.app.config import db_config

db = Gino(
    dsn=db_config.DB_DSN,
    pool_min_size=db_config.DB_POOL_MIN_SIZE,
    pool_max_size=db_config.DB_POOL_MAX_SIZE,
    echo=db_config.DB_ECHO,
    ssl=db_config.DB_SSL,
    use_connection_for_request=db_config.DB_USE_CONNECTION_FOR_REQUEST,
    retry_limit=db_config.DB_RETRY_LIMIT,
    retry_interval=db_config.DB_RETRY_INTERVAL,
)
