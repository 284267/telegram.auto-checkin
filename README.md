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

### 🧰 1. 安装 Python3（建议 Python 3.8+）

```bash
sudo apt update
sudo apt install python3 python3-pip -y


git clone https://github.com/284267/telegram-auto-checkin.git
cd telegram-auto-checkin
 安装依赖
pip3 install -r requirements.txt
复制配置模板并修改你的信息：
cp config_template.py config.py
nano config.py

根据模板填写以下内容：

Telegram API ID 和 Hash

签到的 Bot 用户名

群组签到内容

默认签到命令

是否使用代理（可设为 None）

python3 tgqd.py


