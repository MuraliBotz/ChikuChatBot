from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from AiChatBot import Chiku as app
from config import LOGGER_ID as LOG_GROUP_ID
from AiChatBot.Db import get_served_chats, remove_served_chat, add_served_chat

import requests


@app.on_message(filters.new_chat_members, group=2)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"

        response = requests.get("https://nekos.best/api/v2/neko").json()
        image_url = response["results"][0]["url"]
        served_chats = len(await get_served_chats())
        chat_id = message.chat.id
        if message.chat.username:
            chatusername = f"{message.chat.username}"
        else:
            chatusername = await client.export_chat_invite_link(message.chat.id)
        
        msg = (
            f"❄️ <b><u>ʙᴏᴛ #ᴀᴅᴅᴇᴅ ᴛᴏ ɴᴇᴡ ɢʀᴏᴜᴘ </u></b> \n\n"
            f"┏━━━━━━━━━━━━━━━━━┓\n"
            f"┣★ **ᴄʜᴀᴛ** › : {message.chat.title}\n"
            f"┣★ **ᴄʜᴀᴛ ɪᴅ** › : {chat_id}\n"
            f"┣★ **ᴄʜᴀᴛ ᴜɴᴀᴍᴇ** › : @{message.chat.username}\n"
            f"┣★ **ɢʀᴏᴜᴘ ʟɪɴᴋ** › : [ᴛᴏᴜᴄʜ]({chatusername}) \n"
          #  f"┣★ **ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs** › : {count}\n"
            f"┣★ **ᴛᴏᴛᴀʟ ᴄʜᴀᴛ** › : {served_chats}\n"
            f"┣★ **ᴀᴅᴅᴇᴅ ʙʏ** › : {added_by} \n"
            f"┗━━━━━━━━━★ "
        )
        await app.send_photo(LOG_GROUP_ID, photo=image_url, caption=msg)
  
        await add_served_chat(chat_id)

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        response = requests.get("https://nekos.best/api/v2/neko").json()
        image_url = response["results"][0]["url"]
        chat_id = message.chat.id
        left = (
            f"❄️ <b><u>ʙᴏᴛ #ʟᴇғᴛ_ɢʀᴏᴜᴘ </u></b> \n\n"
            f"๏ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➠ {title}\n"
            f"๏ ɢʀᴏᴜᴘ ɪᴅ ➠ {chat_id}\n"
            f"๏ ʙᴏᴛ ʀᴇᴍᴏᴠᴇᴅ ʙʏ ➠ {remove_by}\n"
        )
        await app.send_photo(LOG_GROUP_ID, photo=image_url, caption=left)
        await remove_served_chat(chat_id)
        
