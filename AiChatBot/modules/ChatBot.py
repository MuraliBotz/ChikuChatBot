from pyrogram import Client, filters, types, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from motor.motor_asyncio import AsyncIOMotorClient
import requests
from config import *
from AiChatBot.Db import add_served_user, add_served_chat, get_served_chats, get_served_users
from AiChatBot import Chiku
from pyrogram.enums import ChatAction, ChatType

mongo_client = AsyncIOMotorClient(MONGO_URL)
db = mongo_client.chikudatabass
chatbotdatabase = db.cchikudarabase

async def is_admin(chat_id: int, user_id: int) -> bool:
    member = await Chiku.get_chat_member(chat_id, user_id)
    return member.status in [enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER]

@Chiku.on_message(filters.command("chatbot") & filters.group, group=6)
async def chatbot_command(_, message: Message):
    if await is_admin(message.chat.id, message.from_user.id):
        response = requests.get("https://nekos.best/api/v2/neko").json()
        image_url = response["results"][0]["url"]
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="Eɴᴀʙʟᴇ", callback_data="enable_chatbot"),
                    InlineKeyboardButton(text="Dɪsᴀʙʟᴇ", callback_data="disable_chatbot"),
                ]
            ]
        )
        await message.reply_photo(image_url, caption=f"ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ᴀɴʏ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪꜱᴀʙʟᴇ ᴄʜᴀᴛʙᴏᴛ ɪɴ {message.chat.title}", reply_markup=keyboard)
    else:
        await message.reply_text("ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪꜱ ᴏɴʟʏ ꜰᴏʀ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴꜱ.", show_alert=True)

@Chiku.on_callback_query(filters.regex(r"^(enable|disable)_chatbot$"))
async def enable_disable_chatbot(_, query: types.CallbackQuery):
    chat_id = query.message.chat.id
    action = query.data
  
    if await is_admin(chat_id, query.from_user.id):
        if action == "enable_chatbot":
            if await chatbotdatabase.find_one({"chat_id": chat_id}):
                await query.answer("ᴄʜᴀᴛʙᴏᴛ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ .", show_alert=True)
            else:
                await chatbotdatabase.insert_one({"chat_id": chat_id, "admin_id": query.from_user.id})
                await query.answer("ᴄʜᴀᴛʙᴏᴛ ᴇɴᴀʙʟᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ !", show_alert=True)
                await query.message.edit_text(f"ᴄʜᴀᴛʙᴏᴛ ᴇɴᴀʙʟᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ  ʙʏ {query.from_user.mention()}")
        else:
            chatbot_info = await chatbotdatabase.find_one({"chat_id": chat_id})
            if chatbot_info:
                await chatbotdatabase.delete_one({"chat_id": chat_id})
                await query.answer("ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅᴇꜱᴀʙʟᴇᴅ ᴄʜᴀᴛʙᴏᴛ !", show_alert=True)
                await query.message.edit_text(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅᴇꜱᴀʙʟᴇᴅ ᴄʜᴀᴛʙᴏᴛ ʙʏ {query.from_user.mention()}")
            else:
                await query.answer("ᴍᴀᴋᴇ ꜱᴜʀᴇ ʏᴏᴜ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ ᴄʜᴀᴛʙᴏᴛ .", show_alert=True)
    else:
        await query.answer("ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪꜱ ᴏɴʟʏ ꜰᴏʀ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴꜱ.", show_alert=True)

@Chiku.on_message(
    (filters.text & ~filters.bot), group=4
)
async def chatbottexts(client, message):
    user_id = message.from_user.id
    user_message = message.text
    if message.chat.type == ChatType.PRIVATE:
        api_url = f"http://api.brainshop.ai/get?bid=181999&key=BTx5oIaCq8Cqut3S&uid={user_id}&msg={user_message}"
        response = requests.get(api_url).json()["cnt"]
        await message.reply_text(response)
    else:
        if (message.reply_to_message and message.reply_to_message.from_user.is_self) or not message.reply_to_message:
            chatbot_info = await chatbotdatabase.find_one({"chat_id": message.chat.id})
            if chatbot_info:
                try:
                    api_url = f"http://api.brainshop.ai/get?bid=181999&key=BTx5oIaCq8Cqut3S&uid={user_id}&msg={user_message}"
                    response = requests.get(api_url).json()["cnt"]
                    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
                    await message.reply_text(response)
                except Exception as e:
                    print(f"An error occurred in group chat bot: {str(e)}")
                    pass
