from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand


@on_natural_language(keywords={'天气'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    print(session)
    return IntentCommand(90.0, 'weather')
