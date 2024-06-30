from AiChatBot import Chiku
import asyncio
from pyrogram import filters
from config import OWNER_ID
from Murali import Owner
from pyrogram.errors import FloodWait
from AiChatBot.Db import get_served_chats, get_served_users

@Chiku.on_cmd(["gcast", "broadcast"])
async def broadcast_message(client, message):
    if message.from_user.id not in Owner and message.from_user.id not in OWNER_ID:
        return await message.reply_text(
            "»ʜᴇʜᴇ ᴏɴʟʏ ᴍʏ ᴏᴡɴᴇʀ ᴄᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ"
        )
    
    if message.reply_to_message:
        msg_id = message.reply_to_message.id
        query = None
    else:
        if len(message.command) < 2:
            return await message.reply_text(f"**Usage:**\n`/broadcast [message]` or reply to a message")
        query = message.text.split(None, 1)[1]
        if not query:
            return await message.reply_text("Please provide a message to broadcast.")
        msg_id = None

    sent_chats = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for chat_id in chats:
        
        try:
            if msg_id:
                await client.forward_messages(chat_id, message.chat.id, msg_id)
            else:
                await client.send_message(chat_id, text=query)
            sent_chats += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception:
            continue

    await message.reply_text(f"Broadcasted message to {sent_chats} chats.")

    sent_users = 0
    users = []
    susers = await get_served_users()
    for user in susers:
        users.append(int(user["user_id"]))
    for user_id in users:
        try:
            if msg_id:
                await client.forward_messages(user_id, message.chat.id, msg_id)
            else:
                await client.send_message(user_id, text=query)
            sent_users += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception:
            continue

    await message.reply_text(f"Broadcasted message to {sent_users} users.")

