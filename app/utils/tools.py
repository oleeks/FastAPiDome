from datetime import datetime, timedelta


def time2str(minutes=0, time_date=None, sft='%Y-%m-%d %H:%M:%S'):
    """
    :param time_date: 时间
    :param minutes: 间隔时间
    :param sft: 转化时间格式
    :return:
    """
    if not time_date:
        time_date = datetime.now()
    diff_time = time_date - timedelta(minutes=minutes)
    time_sft = diff_time.strftime(sft)
    return time_sft


def time2timestamp(time_stamp, digits=10):
    """
    转换为指定长度的timestamp
    :param time_stamp:
    :param digits:
    :return:
    """
    if not time_stamp:
        time_stamp = datetime.now().timestamp()

    digits = 10 ** (digits - 10)
    time_stamp = int(round(time_stamp * digits))
    return time_stamp


class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance