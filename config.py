from nonebot.default_config import *

API_ROOT = 'http://172.17.0.2:5700'
SUPERUSERS = {769484623}
COMMAND_START = {'.'}
HOST = '0.0.0.0'
PORT = 10240

CUSTOM_PLUGINS = [
    # 复读姬自动复读插件
    'plugins.auto_repeater',
    # 复读姬人品计算器
    'plugins.today_rp',
    # 母机系统状态
    'plugins.system_status'
]

DISABLE_WELCOME_TEXT = False
