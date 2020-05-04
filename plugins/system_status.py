from nonebot import on_command, CommandSession
from psutil import cpu_count, cpu_percent, virtual_memory, boot_time
from datetime import datetime

TEMPLATE_SYSTEM_STATUS = '母机启动时间:%s\r\n' \
                         'CPU总核数: %d \r\n' \
                         '内存总大小: %d MB\r\n' \
                         '母机CPU当前占用为: %.1f %%\r\n' \
                         '母机内存当前占用为: %.1f %%\r\n'


# 获取当前系统状态
@on_command('STELLIA!', only_to_me=False)
async def _(session: CommandSession):
    params = (
        datetime.fromtimestamp(boot_time()),
        cpu_count(),
        virtual_memory().total / 1024 / 1024,
        cpu_percent(),
        virtual_memory().percent
    )
    await session.send(TEMPLATE_SYSTEM_STATUS % params)
