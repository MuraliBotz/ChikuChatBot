from pyrogram.types import CallbackQuery
from AiChatBot import Chiku
from AiChatBot.Strings import *
from pyrogram.enums import ChatType
import requests 
from config import OWNER_ID
from pyrogram import filters

@Chiku.on_callback_query(filters.regex("gohelp"))
async def help_panel(client, callback_query: CallbackQuery):
    try:
        await callback_query.edit_message_text(f"ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ʜᴇʟᴘ ꜱᴇᴄᴛɪᴏɴ ᴏꜰ {Chiku.mention}", reply_markup=HELP_BUTTON)
    except Exception as e:
        print(f"An error occurred while editing the HELP message: {e}")

@Chiku.on_callback_query(filters.regex("gotomain"))
async def gotomain(client, callback_query: CallbackQuery):
    try:
        await Chiku.resolve_peer(OWNER_ID[0])
        OWNER = OWNER_ID[0]
    except:
        OWNER = OWNER_ID[0]
    M = START_BUTTON(OWNER)
    try:
        await callback_query.edit_message_text(START_TEXT.format(callback_query.from_user.mention, Chiku.mention), reply_markup=M)
    except Exception as e:
        print(f"An error occurred while editing the HELP message: {e}")

@Chiku.on_callback_query(filters.regex("afk"))
async def afk(client, callback_query: CallbackQuery):
    try:
        if callback_query.message.chat.type in (ChatType.PRIVATE, ChatType.SUPERGROUP):
            await callback_query.edit_message_text(TEXT1, reply_markup=INHELPBUTTON)
    except Exception as e:
        print(f"An error occurred while editing the message: {e}")

@Chiku.on_callback_query(filters.regex("alive"))
async def alive(client, callback_query: CallbackQuery):
    try:
        if callback_query.message.chat.type in (ChatType.PRIVATE, ChatType.SUPERGROUP):
            await callback_query.edit_message_text(TEXT2, reply_markup=INHELPBUTTON)
    except Exception as e:
        print(f"An error occurred while editing the message: {e}")

@Chiku.on_callback_query(filters.regex("id"))
async def iddd(client, callback_query: CallbackQuery):
    try:
        if callback_query.message.chat.type in (ChatType.PRIVATE, ChatType.SUPERGROUP):
            await callback_query.edit_message_text(TEXT3, reply_markup=INHELPBUTTON)
    except Exception as e:
        print(f"An error occurred while editing the message: {e}")

@Chiku.on_callback_query(filters.regex("ping"))
async def pinghh(client, callback_query: CallbackQuery):
    try:
        if callback_query.message.chat.type in (ChatType.PRIVATE, ChatType.SUPERGROUP):
            await callback_query.edit_message_text(TEXT4, reply_markup=INHELPBUTTON)
    except Exception as e:
        print(f"An error occurred while editing the message: {e}")

@Chiku.on_callback_query(filters.regex("chatbott"))
async def chatbott(client, callback_query: CallbackQuery):
    try:
        if callback_query.message.chat.type in (ChatType.PRIVATE, ChatType.SUPERGROUP):
            await callback_query.edit_message_text(TEXT5, reply_markup=INHELPBUTTON)
    except Exception as e:
        print(f"An error occurred while editing the message: {e}")

@Chiku.on_callback_query(filters.regex("start"))
async def strt(client, callback_query: CallbackQuery):
    try:
        if callback_query.message.chat.type in (ChatType.PRIVATE, ChatType.SUPERGROUP):
            await callback_query.edit_message_text(TEXT6, reply_markup=INHELPBUTTON)
    except Exception as e:
        print(f"An error occurred while editing the message: {e}")

@Chiku.on_callback_query(filters.regex("dev"))
async def devel(client, callback_query: CallbackQuery):
    try:
        if callback_query.message.chat.type in (ChatType.PRIVATE, ChatType.SUPERGROUP):
            await callback_query.edit_message_text(TEXT7, reply_markup=INHELPBUTTON)
    except Exception as e:
        print(f"An error occurred while editing the message: {e}")

@Chiku.on_callback_query(filters.regex("telegraph"))
async def telegraph(client, callback_query: CallbackQuery):
    try:
        if callback_query.message.chat.type in (ChatType.PRIVATE, ChatType.SUPERGROUP):
            await callback_query.edit_message_text(TEXT8, reply_markup=INHELPBUTTON)
    except Exception as e:
        print(f"An error occurred while editing the message: {e}")

@Chiku.on_callback_query(filters.regex("love"))
async def love(client, callback_query: CallbackQuery):
    try:
        if callback_query.message.chat.type in (ChatType.PRIVATE, ChatType.SUPERGROUP):
            await callback_query.edit_message_text(TEXT9, reply_markup=INHELPBUTTON)
    except Exception as e:
        print(f"An error occurred while editing the message: {e}")

@Chiku.on_callback_query(filters.regex("close"))
async def close(client, callback_query: CallbackQuery):
    await callback_query.message.delete()

