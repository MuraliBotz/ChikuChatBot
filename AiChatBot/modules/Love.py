from pyrogram import Client, filters
import random
from AiChatBot import Chiku

def get_random_message(love_percentage):
    if love_percentage <= 30:
        return random.choice([
            "ʟᴏᴠᴇ ɪs ɪɴ ᴛʜᴇ ᴀɪʀ ʙᴜᴛ ɴᴇᴇᴅs ᴀ ʟɪᴛᴛʟᴇ sᴘᴀʀᴋ.",
            "ᴀ ɢᴏᴏᴅ sᴛᴀʀᴛ ʙᴜᴛ ᴛʜᴇʀᴇ's ʀᴏᴏᴍ ᴛᴏ ɢʀᴏᴡ.",
            "ɪᴛ's ᴊᴜsᴛ ᴛʜᴇ ʙᴇɢɪɴɴɪɴɢ ᴏғ sᴏᴍᴇᴛʜɪɴɢ ʙᴇᴀᴜᴛɪғᴜʟ."
        ])
    elif love_percentage <= 70:
        return random.choice([
            "ᴀ sᴛʀᴏɴɢ ᴄᴏɴɴᴇᴄᴛɪᴏɴ ɪs ᴛʜᴇʀᴇ. ᴋᴇᴇᴘ ɴᴜʀᴛᴜʀɪɴɢ ɪᴛ.",
            "ʏᴏᴜ'ᴠᴇ ɢᴏᴛ ᴀ ɢᴏᴏᴅ ᴄʜᴀɴᴄᴇ. ᴡᴏʀᴋ ᴏɴ ɪᴛ.",
            "ʟᴏᴠᴇ ɪs ʙʟᴏssᴏᴍɪɴɢ, ᴋᴇᴇᴘ ɢᴏɪɴɢ."
        ])
    elif love_percentage <= 90:
        return random.choice([
            "ʏᴏᴜ ᴀʀᴇ ᴀ ɢʀᴇᴀᴛ ᴘᴀɪʀ, ᴋᴇᴇᴘ ɪᴛ ᴜᴘ!",
            "ʏᴏᴜʀ ʙᴏɴᴅ ɪs sᴛʀᴏɴɢ ᴀɴᴅ ᴠɪʙʀᴀɴᴛ.",
            "ᴀʟᴍᴏsᴛ ᴘᴇʀғᴇᴄᴛ ᴛᴏɢᴇᴛʜᴇʀ."
        ])
    else:
        return random.choice([
            "ᴡᴏᴡ! ɪᴛ's ᴀ ᴍᴀᴛᴄʜ ᴍᴀᴅᴇ ɪɴ ʜᴇᴀᴠᴇɴ!",
            "ᴘᴇʀғᴇᴄᴛ ᴍᴀᴛᴄʜ! ᴄʜᴇʀɪsʜ ᴛʜɪs ʙᴏɴᴅ.",
            "ᴅᴇsᴛɪɴᴇᴅ ᴛᴏ ʙᴇ ᴛᴏɢᴇᴛʜᴇʀ. ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴs!"
        ])
      
@Chiku.on_cmd("love")
async def love_command(client, message):
    command, *args = message.text.split(" ")
    if not len(args) >= 2:
        return await message.reply_text("Please enter two names after /love command.")
        
    name1 = args[0].strip()
    name2 = args[1].strip()
    love_percentage = random.randint(10, 100)
    love_message = get_random_message(love_percentage)
    response = f"{name1}💕 + {name2}💕 = {love_percentage}%\n\n{love_message}"
    await message.reply_text(response)
    
