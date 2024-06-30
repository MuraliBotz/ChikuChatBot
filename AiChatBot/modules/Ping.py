from AiChatBot import Chiku
from pyrogram import filters
import time
from datetime import datetime
import requests

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

_boot_ = time.time()

@Chiku.on_cmd("ping")
async def pingbot(client, message):
    start = datetime.now()
    Hello = (datetime.now() - start).microseconds / 1000
    response = requests.get("https://nekos.best/api/v2/neko").json()
    m = response["results"][0]["url"]
    bot_uptime = int(time.time() - _boot_)
    Uptime = f"{get_readable_time(bot_uptime)}"
    await message.reply_photo(m, caption=f"<u>{Chiku.mention}</u> \n\nᴘɪɴɢ ᴘᴏɴɢ `{Hello}` ms\nᴜᴘᴛɪᴍᴇ - {Uptime}")

