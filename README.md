# Telegram Auto Check-in 🤖🗓️

一个基于 Telethon 的 Telegram 自动签到脚本，支持向多个机器人和群组发送签到指令，支持 SOCKS5 代理，并带有签到日志记录功能。适用于日常自动化打卡、Bot 任务执行等场景。

=========================

✨ 功能亮点：

✅ 自动向多个 Telegram Bot 发送签到命令  
✅ 支持群组签到（可为不同群设置不同文本）  
✅ 签到记录保存，避免重复签到  
✅ 支持 SOCKS5 代理（科学上网友好）  
✅ 清晰日志输出，方便查看任务执行情况  

=========================

🚀 安装与服务器部署指南（支持 Ubuntu / Debian / CentOS）

✅ 步骤一：更新系统 & 安装 Python3 + pip

sudo apt update  
sudo apt install python3 python3-pip -y

✅ 步骤二：克隆项目仓库

git clone https://github.com/284267/telegram-auto-checkin.git  
cd telegram-auto-checkin

✅ 步骤三：安装依赖

pip3 install -r requirements.txt

✅ 步骤四：复制配置文件模板

cp config_template.py config.py

✅ 步骤五：编辑配置文件

nano config.py

📌 在 config.py 中填写以下内容：

- api_id：你的 Telegram API ID（整数）  
- api_hash：你的 API Hash（字符串）  
- session_name：会话文件名（随便起）  
- proxy：如需代理，填写例如 ('socks5', '127.0.0.1', 7890)，否则填 None  
- bots_to_checkin：要签到的 bot 名称列表（无 @）  
- groups_to_checkin：群组名称列表（无 @）  
- checkin_command：默认签到指令  
- group_checkin_texts / bot_checkin_texts：为群组或 bot 单独配置的签到内容（可选）

✅ 步骤六：首次登录 Telegram（扫码或验证码）

python3 tgqd.py

运行后你需要输入验证码或扫码完成一次登录，之后会话保存，无需重复。

✅ 步骤七（可选）：设置定时任务（每天自动签到）

crontab -e

添加以下行，表示每天早上 8 点自动执行：

0 8 * * * cd /你的项目路径 && /usr/bin/python3 tgqd.py >> log.txt 2>&1

✅ 步骤八（可选）：忽略敏感信息文件，避免上传 GitHub

echo "config.py" >> .gitignore  
echo "checkin_log.json" >> .gitignore

=========================

🎉 完成！

你现在已经完成部署，可立即使用！后续你可以自定义更多 bot、签到指令、签到时间，也可以结合 `screen`、`supervisor`、`Docker` 等方式进行扩展！

