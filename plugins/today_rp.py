from nonebot import on_command, CommandSession
import random
from datetime import datetime

TEMPLATE_JRRP = "使用毫无黑幕的随机算法计算当日人品。你今天的人品值为：%d"
TEMPLATE_DIVINATION = '求签 %s\r\n\r\n 经过毫无黑幕的随机算法计算\r\n结果为:%s'
TEMPLATE_DIVINATION_RESULT = ['大凶', '凶', '小吉', '中吉', '大吉']


def __generate_seeds(*args):
    print(args)
    return '--'.join(list(args))


@on_command('jrrp', only_to_me=False)
async def _(session: CommandSession):
    qq_number = str(session.ctx['user_id'])
    now_str = datetime.now().strftime('%Y-%m-%d')
    seed = __generate_seeds(now_str, qq_number)

    random.seed(seed)
    rp = random.randrange(0, 101)
    await session.send(TEMPLATE_JRRP % rp, at_sender=True)


@on_command('求签', only_to_me=False)
async def _(session: CommandSession):
    qq_number = str(session.ctx['user_id'])
    now_str = datetime.now().strftime('%Y-%m-%d')
    event = session.current_arg_text
    if event == '':
        await session.send('求签事件不可为空呢~', at_sender=True)
    else:
        # 时间 & 事件 & 人作为种子，每天算出来的结果都是一样的
        seed = __generate_seeds(now_str, event, qq_number)
        random.seed(seed)
        result = TEMPLATE_DIVINATION_RESULT[random.randrange(0, len(TEMPLATE_DIVINATION_RESULT))]
        await session.send(TEMPLATE_DIVINATION % (event, result), at_sender=True)
