from nonebot import on_command, CommandSession, get_bot
import random
from datetime import datetime
from nonebot import on_natural_language, NLPSession, IntentCommand
import logging

today_rp = {}
last_cal_time = datetime.now().date()

template = "使用毫无黑幕的随机算法计算当日人品。你今天的人品值为：%d"


def __if_new_day_comes(current_date):
    global last_cal_time
    return current_date > last_cal_time


def flush_cal_time():
    global last_cal_time
    current_date = datetime.now().date()
    if __if_new_day_comes(current_date):
        last_cal_time = current_date
        today_rp.clear()


@on_command('今日人品')
def _(session: CommandSession):
    global today_rp
    qq_number = session.ctx.user_id
    if qq_number not in today_rp:
        rp = random.randrange(0, 100)
        today_rp[qq_number] = rp
    session.send(template % today_rp[qq_number], at_sender=True)
