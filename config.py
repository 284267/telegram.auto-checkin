# config.py（示例模板文件，请根据实际使用场景填写）

# Telegram API 信息（请前往 https://my.telegram.org 获取）
api_id = 你的_api_id                 # 示例：123456
api_hash = '你的_api_hash'           # 示例：'abcd1234efgh5678'

# 本地会话文件名（随便起个名字）
session_name = 'your_session_name'

# config.py（代理现在变成可选项了！）

# 如果不使用代理，将其设置为 None
# 使用代理则按如下格式填写：
# proxy = ('socks5', '127.0.0.1', 7890)
proxy = None  # 默认不开启代理

# 🤖 需要签到的 Telegram Bot 用户名（不带 @）
bots_to_checkin = [
    'bot_name_1',
    'bot_name_2',
    # '更多的 bot ...'
]

# 🧾 默认签到命令
checkin_command = '/checkin'

# 👥 需要签到的群组用户名（不带 @）
groups_to_checkin = [
    'group_name_1',
    'group_name_2',
    # '更多的群组 ...'
]

# ✅ 群组签到的自定义消息（如不设定，则使用默认命令）
group_checkin_texts = {
    'group_name_1': '签到内容示例',
    'group_name_2': '/daily_checkin'
}

# 🤖 特定 bot 的个性化签到消息（如有差异）
bot_checkin_texts = {
    'bot_name_2': '签到'
}
