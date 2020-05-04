from nonebot import on_command, CommandSession
from psutil import cpu_count, cpu_percent, virtual_memory

TEMPLATE_SYSTEM_STATUS = 'CPU总核数：%s\r\n内存总大小：%s\r\n当前CPU占用：%s%\r\n当前内存占用：%s%\r\n'


# 获取当前系统状态
@on_command('STELLIA!', only_to_me=False)
async def _(session: CommandSession):
    params = (cpu_count(), virtual_memory().total, cpu_percent(), virtual_memory().percent)
    await session.send(TEMPLATE_SYSTEM_STATUS % params, at_sender=True)
