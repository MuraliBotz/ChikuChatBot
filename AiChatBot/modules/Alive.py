from AiChatBot import Chiku
from pyrogram import client, filters 
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from AiChatBot.modules.Ping import get_readable_time
import time

_boot_ = time.time()

@Chiku.on_cmd("alive")
async def alive(client, message):
    response = requests.get("https://nekos.best/api/v2/neko").json()
    M = response["results"][0]["url"]
    bot_uptime = int(time.time() - _boot_)
    Uptime = f"{get_readable_time(bot_uptime)}"
    await message.reply_photo(M, caption=f"{Chiku.mention} ɪꜱ ꜱᴛɪʟʟ ᴀʟɪᴠᴇ ʙᴀʙʏ ❤️\n\nɪ ᴅɪᴅɴ'ᴛ ꜱʟᴇᴘᴛ ꜰʀᴏᴍ {Uptime} ", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 💓",
                        url=f"https://t.me/{Chiku.username}?startgroup=true",
                    ),
                ],
            ]
    ))
