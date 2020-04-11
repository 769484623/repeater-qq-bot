import nonebot
import config
import asyncio

from plugins.auto_repeater import send_exit_msg, send_start_msg
from msg_template.start_exit_msg import BOT_START_MSG, BOT_EXIT_MSG


def start_bot():
    msg_list = [None, None]
    if not config.DISABLE_WELCOME_TEXT:
        msg_list = [BOT_START_MSG, BOT_EXIT_MSG]
    loop = asyncio.get_event_loop()
    # 复读姬上线问候语
    loop.run_until_complete(asyncio.wait([send_start_msg(msg_list[0], [559553404])]))

    nonebot.run(host='0.0.0.0', port=10240)
    # 复读姬退出问候语
    loop.run_until_complete(asyncio.wait([send_exit_msg(msg_list[1], [559553404])]))

    loop.close()


def init_bot():
    nonebot.init(config)
    # 复读姬自动复读插件
    nonebot.load_plugin('plugins.auto_repeater')
    # 复读姬人品计算器
    nonebot.load_plugin('plugins.today_rp')


if __name__ == '__main__':
    init_bot()
    start_bot()
