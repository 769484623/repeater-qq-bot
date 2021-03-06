from nonebot import on_command, CommandSession, get_bot
from nonebot import on_natural_language, NLPSession, IntentCommand
import logging

last_msg_of_qq_groups = {}


async def send_start_msg(start_msg, qq_group_list: list = None):
    if start_msg is not None:
        if qq_group_list is None:
            qq_group_list = last_msg_of_qq_groups
        bot = get_bot()
        for group in qq_group_list:
            await bot.send_group_msg(group_id=int(group), message=start_msg)


async def send_exit_msg(exit_msg, qq_group_list: list = None):
    if exit_msg is not None:
        if qq_group_list is None:
            qq_group_list = last_msg_of_qq_groups
        bot = get_bot()
        for group in qq_group_list:
            await bot.send_group_msg(group_id=int(group), message=exit_msg)
    logging.getLogger('nonebot').info('Bot Exit')


@on_command('repeat', only_to_me=False)
async def repeater(session: CommandSession):
    await session.send(session.current_arg_text)


# 监听所有非命令聊天
@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
    from utils.math import random_win
    # 复读机只处理QQ群消息
    msg = session.ctx['raw_message']
    qq_group_id = session.ctx['group_id']
    if session.ctx['message_type'] == 'group':
        last_msg = last_msg_of_qq_groups.get(qq_group_id)
        if last_msg is not None:
            is_the_msg_the_same = msg == last_msg['msg']
            if is_the_msg_the_same:
                if not last_msg['is_repeated']:
                    last_msg['is_repeated'] = True
                    return IntentCommand(100, 'repeat', current_arg=msg)
                return IntentCommand(0, 'repeat')
        last_msg_of_qq_groups[qq_group_id] = {'msg': msg, 'is_repeated': False}
    # 随机复读
    if random_win(0.01):
        last_msg_of_qq_groups[qq_group_id] = {'msg': msg, 'is_repeated': True}
        return IntentCommand(100, 'repeat', current_arg=msg)
    return IntentCommand(0, 'repeat')
