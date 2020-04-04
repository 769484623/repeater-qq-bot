import nonebot
import config

nonebot.init(config)
nonebot.load_builtin_plugins()
nonebot.run(host='0.0.0.0', port=10240)
