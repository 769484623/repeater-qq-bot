import nonebot
import config
import asyncio

from plugins.auto_repeater import send_exit_msg, send_start_msg

loop = asyncio.get_event_loop()

nonebot.init(config)
nonebot.load_plugin('plugins.auto_repeater')

# 复读姬上线问候语
loop.run_until_complete(asyncio.wait([send_start_msg('复读姬援交回来啦~功能正常使用~', [559553404])]))

nonebot.run(host='0.0.0.0', port=10240)

# 复读姬退出问候语
loop.run_until_complete(asyncio.wait([send_exit_msg('复读姬援交去啦~接下来功能将不可用~')]))

loop.close()
