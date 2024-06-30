import os

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegraph import upload_file

from AiChatBot import Chiku


@Chiku.on_cmd(["Tgm", "tl"])
async def telegraph(client, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "ᴘʟᴇᴀsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇᴅɪᴀ ᴛᴏ ᴜᴘʟᴏᴀᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴘʜ"
        )
    try:
        text = await message.reply("ᴘʀᴏᴄᴇssɪɴɢ...")

        async def progress(current, total):
            await text.edit_text(f"ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ... {current * 100 / total:.1f}%")

        try:
            local_path = await message.reply_to_message.download( progress=progress
            )
            await text.edit_text(" ᴜᴘʟᴏᴀᴅɪɴɢ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ...")
            upload_path = upload_file(local_path)
            await text.edit_text(
                f"🌐 | [ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ](https://telegra.ph{upload_path[0]})",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ",
                                url=f"https://telegra.ph{upload_path[0]}",
                            )
                        ]
                    ]
                ),
            )
            try:
                os.remove(local_path)
            except Exception:
               pass
        except Exception as e:
            await text.edit_text(f"❌ |ғɪʟᴇ ᴜᴘʟᴏᴀᴅ ғᴀɪʟᴇᴅ \n\n<i>ʀᴇᴀsᴏɴ: {e}</i>")
            try:
                os.remove(local_path)
            except Exception:
               pass
            return
    except Exception:
        pass
