# Telegram Auto Check-in 🤖🗓️

一个基于 [Telethon](https://github.com/LonamiWebs/Telethon) 的 Telegram 自动签到脚本，支持向多个机器人和群组发送签到指令，支持 SOCKS5 代理，并带有签到日志记录功能。适用于日常自动化打卡、Bot 任务执行等场景。

---

## ✨ 功能亮点

- ✅ 自动向多个 Telegram Bot 发送签到命令
- ✅ 支持群组签到（可为不同群设置不同文本）
- ✅ 签到记录保存，避免重复签到
- ✅ 支持 SOCKS5 代理（科学上网友好）
- ✅ 清晰日志输出，方便查看任务执行情况

---


---

## 🚀 安装与服务器部署指南

你可以将本项目部署到 Linux 服务器（如 Ubuntu、Debian、CentOS），实现每日自动 Telegram 签到任务。

---
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

# 在 config.py 中填写以下内容：
# - 你的 Telegram API ID（整数）
# - 你的 Telegram API Hash（字符串）
# - Bot 用户名列表（不加@）
# - 群组用户名列表（不加@）
# - 每个群或 Bot 的签到指令
# - 是否使用代理（例如：('socks5', '127.0.0.1', 7890)，如果不使用则写 None）

# ✅ 手动运行一次，首次登录 Telegram（扫码或验证码）
python3 tgqd.py

