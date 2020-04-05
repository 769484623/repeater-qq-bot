from nonebot import on_command, CommandSession, get_bot
from nonebot import on_natural_language, NLPSession, IntentCommand
import logging

last_msg_of_qq_groups = {}


async def send_start_msg(start_msg, qq_group_list: list = None):
    if qq_group_list is None:
        qq_group_list = last_msg_of_qq_groups
    bot = get_bot()
    for group in qq_group_list:
        await bot.send_group_msg(group_id=int(group), message=start_msg)


async def send_exit_msg(exit_msg, qq_group_list: list = None):
    if qq_group_list is None:
        qq_group_list = last_msg_of_qq_groups
    bot = get_bot()
    for group in qq_group_list:
        await bot.send_group_msg(group_id=int(group), message=exit_msg)
    logging.getLogger('nonebot').info('Bot Exit')


@on_command('group_repeat')
async def auto_repeater(session: CommandSession):
    if session.ctx['message_type'] == 'group':
        qq_group_id = session.ctx['group_id']
        msg = session.ctx['raw_message']
        last_msg = last_msg_of_qq_groups.get(qq_group_id)
        if last_msg is not None:
            is_the_msg_the_same = msg == last_msg['msg']
            if is_the_msg_the_same:
                print(last_msg)
                if not last_msg['is_repeated']:
                    last_msg['is_repeated'] = True
                    await session.send(msg)
                return
        last_msg_of_qq_groups[qq_group_id] = {'msg': msg, 'is_repeated': False}


@on_command('repeat', only_to_me=False)
async def repeater(session: CommandSession):
    await session.send(session.current_arg_text)


# 监听所有非命令聊天
@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
    # 复读机只处理QQ群消息
    return IntentCommand(90, 'group_repeat')
