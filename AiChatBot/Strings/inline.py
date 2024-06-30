from AiChatBot import Chiku
from config import OWNER_ID, SUPPORT_GROUP
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from typing import Union


def small_caps(text):
    conversion = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                               "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ")
    return text.translate(conversion)


    
HELP_BUTTON = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(text=small_caps("Afk"), callback_data="afk"),
        InlineKeyboardButton(text=small_caps("Alive"), callback_data="alive"),
        InlineKeyboardButton(text=small_caps("id"), callback_data="id")
    ],
    [
        InlineKeyboardButton(text=small_caps("ping"), callback_data="ping"),
        InlineKeyboardButton(text=small_caps("Chatbot"), callback_data="chatbott"),
        InlineKeyboardButton(text=small_caps("start"), callback_data="start")
    ],
    [
        InlineKeyboardButton(text=small_caps("Dev"), callback_data="dev"),
        InlineKeyboardButton(text=small_caps("T-Graph"), callback_data="telegraph"),
        InlineKeyboardButton(text=small_caps("Love"), callback_data="love")
    ],
    [
        InlineKeyboardButton(text=small_caps("Back"), callback_data="gotomain"),
        InlineKeyboardButton(text=small_caps("close"), callback_data="close"),
       
]
])

INHELPBUTTON = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(text=small_caps("Back"), callback_data="gohelp"),
        InlineKeyboardButton(text=small_caps("close"), callback_data="close"),
       
]
])

def START_BUTTON(OWNER: Union[bool, int] = None):    
    button = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ 💓",
                        url=f"https://t.me/{Chiku.username}?startgroup=true",
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅꜱ ",
                        callback_data="gohelp",
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="ᴅᴇᴠᴇʟᴏᴘᴇʀ ",
                        user_id=OWNER,
                    ),
                    InlineKeyboardButton(
                        text="ꜱᴜᴘᴘᴏʀᴛ",
                        url=f"https://t.me/{SUPPORT_GROUP}",
                    ),
                ],
            ]
        )
    return button 

