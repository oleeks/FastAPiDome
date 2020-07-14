from datetime import datetime, timedelta


def time2str(minutes=0, sft='%Y-%m-%d %H:%M:%S'):
    """
    :param minutes: 间隔时间
    :param sft: 转化时间格式
    :return:
    """
    diff_time = datetime.now() - timedelta(minutes=minutes)
    time_sft = diff_time.strftime(sft)
    return time_sft


def time2timestamp(time_stamp, digits=10):
    """
    转换为指定长度的timestamp
    :param digits:
    :return:
    """
    if not time_stamp:
        time_stamp = datetime.now().timestamp()

    digits = 10 ** (digits - 10)
    time_stamp = int(round(time_stamp * digits))
    return time_stamp
