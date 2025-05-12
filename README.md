# ✅ 更新系统 & 安装 Python3 + pip
sudo apt update
sudo apt install python3 python3-pip -y

# ✅ 克隆项目仓库
git clone https://github.com/284267/telegram-auto-checkin.git
cd telegram-auto-checkin

# ✅ 安装依赖包
pip3 install -r requirements.txt

# ✅ 创建配置文件（从模板复制）
cp config_template.py config.py

# ✅ 编辑配置文件（填写你的 Telegram 信息）
nano config.py

# ⚙️ 在 config.py 中填写以下内容：
# - 你的 Telegram API ID（整数）
# - 你的 Telegram API Hash（字符串）
# - Bot 用户名列表（不加@）
# - 群组用户名列表（不加@）
# - 每个群或 Bot 的签到指令
# - 是否使用代理（例如：('socks5', '127.0.0.1', 7890)，如果不使用则写 None）

# ✅ 手动运行一次，首次登录 Telegram（扫码或验证码）
python3 tgqd.py

# ✅ （可选）设置定时任务：每天早上 8 点自动签到
# 打开 cron 配置
crontab -e

# 添加以下行（请改成你实际项目路径）
# 0 8 * * * cd /你的项目路径 && /usr/bin/python3 tgqd.py >> log.txt 2>&1

# ✅ （可选）添加忽略文件，避免敏感信息上传 GitHub
echo "config.py" >> .gitignore
echo "checkin_log.json" >> .gitignore
