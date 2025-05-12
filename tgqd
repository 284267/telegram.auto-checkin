from telethon import TelegramClient
import asyncio
import datetime
import json
import os
import socks
import config

LOG_FILE = 'checkin_log.json'

# 加载签到日志
def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            return json.load(f)
    return {}

# 保存签到日志
def save_log(log):
    with open(LOG_FILE, 'w') as f:
        json.dump(log, f, ensure_ascii=False, indent=2)

# 初始化 Telegram 客户端
proxy_type = socks.SOCKS5 if config.proxy[0] == 'socks5' else None
client = TelegramClient(config.session_name, config.api_id, config.api_hash, proxy=(proxy_type, config.proxy[1], config.proxy[2]))

async def checkin_all():
    now = datetime.datetime.now()
    today_str = now.strftime('%Y-%m-%d')
    print(f"\n🕒 [{today_str}] 启动签到任务...")

    log = load_log()

    try:
        await client.start()
        print("✅ 成功连接 Telegram")

        # ===== Bot 签到 =====
        for bot in config.bots_to_checkin:
            last_checkin = log.get(bot)
            if last_checkin == today_str:
                print(f"✅ @{bot} 今天已签到，跳过")
                continue

            print(f"\n🤖 正在给机器人 @{bot} 发送签到指令：{config.checkin_command}")
            try:
                await client.send_message(bot, config.checkin_command)
                print(f"🎯 @{bot} 签到成功！")
                log[bot] = today_str
                await asyncio.sleep(2)
            except Exception as e:
                print(f"❌ @{bot} 报错：{e}")

        # ===== 群签到 =====
        for group in config.groups_to_checkin:
            group_key = f"group_{group}"
            last_checkin = log.get(group_key)
            if last_checkin == today_str:
                print(f"✅ 群 @{group} 今天已签到，跳过")
                continue

            # ✅ 这里是修复后的部分：从字典里读取签到文本
            group_text = config.group_checkin_texts.get(group, config.checkin_command)

            print(f"\n👥 正在向群 @{group} 发送签到信息：{group_text}")
            try:
                await client.send_message(group, group_text)
                print(f"📢 群 @{group} 签到成功！")
                log[group_key] = today_str
                await asyncio.sleep(2)
            except Exception as e:
                print(f"❌ 群 @{group} 报错：{e}")

    except Exception as e:
        print("❌ Telegram 连接失败：", e)

    finally:
        save_log(log)
        await client.disconnect()
        print("\n🔌 所有签到任务完成，连接已断开。\n")

if __name__ == "__main__":
    asyncio.run(checkin_all())
