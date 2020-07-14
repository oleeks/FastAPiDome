from sqlalchemy.engine.url import URL

DB_DRIVER = "mysql"
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_USER = 'root'
DB_PASSWORD = '123456'
DB_DATABASE = 'my_dome'

DB_DSN = URL(
    drivername=DB_DRIVER,
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_DATABASE,
)

DB_POOL_MIN_SIZE = 1
DB_POOL_MAX_SIZE = 16
DB_ECHO = False
DB_SSL = None
DB_USE_CONNECTION_FOR_REQUEST = True
DB_RETRY_LIMIT = 1
DB_RETRY_INTERVAL = 1
