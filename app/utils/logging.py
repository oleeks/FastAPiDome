import os
import time
from loguru import logger

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 设置log日志文件
log_path = os.path.join(basedir, 'logs')

if not os.path.exists(log_path):
    os.mkdir(log_path)

log_error_path = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}_error.log')
log_info_path = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}_info.log')
# 日志配置
logger.add(
    log_error_path,
    level="ERROR",
    rotation="12:00",
    retention="5 days",
    encoding="utf-8",
    serialize=False,  # 序列化为json
    enqueue=True
)

logger.add(
    log_info_path,
    level="INFO",
    format="{time:YYYY-MM-DD HH :mm:ss.SSS} - {level} - {file} - {message} - {function} - {line}",
    encoding="utf-8",
    rotation="00:00",  # 文件过大就会重新生成一个新文件  "12:00" 每天12点创建新文件
    enqueue=True,  # 异步写入
    serialize=False,  # 序列化为json
    retention="10 days",  # 一段时间后会清空
    compression="zip"  # 保存为zip格式
)

__all__ = ["logger"]
