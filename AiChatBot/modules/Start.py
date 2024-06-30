from AiChatBot import Chiku
from pyrogram import Client, filters
from AiChatBot.Db import get_served_chats, get_served_users, add_served_user, add_served_chat
import requests 
from Murali import Owner
from pyrogram.enums import ChatType
import random 
from config import OWNER_ID, LOGGER_ID
import asyncio
from AiChatBot.Strings import HELP_BUTTON, START_TEXT, START_BUTTON
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

EMOJIOS = [
    "💣", "💥", "🪄", "🎋", "✨", "🦹", "🌺", "🍀", "💞", "🎁", "💌", "🧨", "⚡", "🤡", "👻",
    "🎃", "🎩", "🕊", "🍭", "🐻", "🦄", "🐼", "🐰", "🌸", "🌈", "🌟", "🌼", "🐱", "🐶", "🐨",
    "🐥", "🎮", "🎵", "📚", "🎨", "☕", "🍕", "🍦", "🍰", "🎈", "🎉", "🐤", "🍬"
]

STICKER = [
    "CAACAgUAAx0CfAEyWgAClxdl9Gg4N-HyCImjGFXOQSHz50MD9wACzgoAAgrrYVWxPZWXGNr8SjQE",
    "CAACAgUAAx0CfAEyWgAClx1l9Gh9PHZKDIw8qbacmxzRD1QNAAOcDQAC0YVxVQijiuf_CF8_NAQ",
    "CAACAgUAAx0CfAEyWgAClyJl9Giplzk45LHa3SWbl30VQud5sgACJAgAAkemgVWsjZK8lbezvDQE",
    "CAACAgUAAx0CfAEyWgACmzZl-DHnr2MOLOPp34onib6dzUFjZgACQAgAApt6iFXzn_VE52urQDQE",
    "CAACAgUAAx0CfAEyWgAClydl9GjEpP5YDBYtPn-g8aC55Mmw_wACyQwAApDeqFbZJHowNnvidjQE",
    "CAACAgUAAx0CbEz78AABAQsvZfP2vNspUQkhtlqbZvDVUTvtIeIAApwNAALRhXFVCKOK5_8IXz8eBA",
    "CAACAgUAAx0CffjZyQACKoZmInOTHCv5lfpO580Y_UPEeUveYAAClAgAAspLwVT1oL4z_bhK7x4E",
    "CAACAgUAAx0CffjZyQACKo5mInRgNfyhH-Y3tKwKyj4_RoKu9gACsgYAAtAF2VYY6HZG8DUiyh4E",
    "CAACAgUAAx0CffjZyQACKoVmInNNz2YqgVIOm0b_XNASdarg0QAC9QkAAlTOgFSpIzlJ8dofZR4E",
    "CAACAgUAAx0CffjZyQACKohmInOZTlDo3YUTGWNdt1-8QFvrhQACqgwAArC9oFRVcuyU8PCqFR4E",
    "CAACAgUAAx0CffjZyQACKopmInPJwawFfy9z96S23cRxc5iI3QACegsAAtFEoVSKNlWkZeVvBh4E",
    "CAACAgUAAx0CffjZyQACKodmInOY37YoG7I-Mn9VbHbcE1VkYgACWAcAAmF4oFRci8T1o_XfEh4E",
    "CAACAgUAAx0CffjZyQACKotmInP5P_GvgKU67nB3ZXDU5UHdwQACBAkAAmGTqFTyMEUMwHr2WB4E",
    "CAACAgUAAx0CfAEyWgAClyxl9GkdhdvG8gmelpuDDXW43GdyYgACDAkAAgYmmVWwda82o5ssVx4E",
    "CAACAgQAAx0CfAEyWgACly9l9GoPSnyCro7QrrIPDIMl0VJNvAACKAwAArq5EFDBJa4kfYMtSB4E",
    "CAACAgUAAx0CfAEyWgAClzJl9Gphz8y2LOZXS_g4SBfUPQwAAeIAAs0EAAISTXlWi28Xpyv5nuUeBA"
]

PHOTOS = [
    "https://telegra.ph/file/018d6002a0ad3aee739f4.jpg",
    "https://telegra.ph/file/9d1b413d24ef703e931e3.jpg",
    "https://telegra.ph/file/035f1b9835c47f45952f7.jpg",
    "https://telegra.ph/file/ca93aeef2e7b45918b668.jpg",
    "https://telegra.ph/file/be64889b9a092f05bb51e.jpg",
    "https://telegra.ph/file/b75e6977d0fa2d5d78b0f.jpg",
    "https://telegra.ph/file/7a07ef4fd40ad2eb20c35.jpg",
    "https://telegra.ph/file/cc7adb01901d0e3d2ed3c.jpg",
    "https://telegra.ph/file/38e76bbfb4666757186f1.jpg",
    "https://telegra.ph/file/602b29a89fca3129194be.jpg",
    "https://telegra.ph/file/71d6213be9255750453a6.jpg",
    "https://telegra.ph/file/7576d27e926a634add7f4.jpg",
    "https://telegra.ph/file/c15485da3d83eb47ad0ff.jpg",
    "https://telegra.ph/file/2c46895723d637de84918.jpg",
    "https://telegra.ph/file/148858c4837e90c9cae49.jpg",
    "https://telegra.ph/file/aa5556e11d949e5f095c5.jpg",
    "https://telegra.ph/file/dd4479290dc8aecd5ed26.jpg",
    "https://telegra.ph/file/7226a80d33f1d9e9051a4.jpg",
    "https://telegra.ph/file/903078ebee2327f8a433c.jpg",
    "https://telegra.ph/file/f5e17db4530f3afb7df29.jpg",
    "https://telegra.ph/file/d104ea00a4f5d5a2bd6bd.jpg",
    "https://telegra.ph/file/e30c70f101f19dac328c6.jpg",
    "https://telegra.ph/file/9dbab97d92fefb83ffb83.jpg",
    "https://telegra.ph/file/574377193d0ac413757a4.jpg",
    "https://telegra.ph/file/704ef3c97af1163689206.jpg",
    "https://telegra.ph/file/18bb7adf017c4566f17bf.jpg",
    "https://telegra.ph/file/eeb95340c7f1b6548f4e2.jpg",
    "https://telegra.ph/file/b6c7cee4bb3767c59ab54.jpg",
    "https://telegra.ph/file/e8d502afc144e77d81c48.jpg"
]

@Chiku.on_cmd("start")
async def startbot(client, message):
    try:
        await Chiku.resolve_peer(OWNER_ID[0])
        OWNER = OWNER_ID[0]
    except:
        OWNER = OWNER_ID[0]

    imgg = await message.reply_photo(photo=random.choice(PHOTOS))
    await asyncio.sleep(0.001)
    await imgg.edit_caption(f"Hᴇʟʟᴏ {message.from_user.mention}")
    await asyncio.sleep(0.0001)
    Ahh = await message.reply_text(text=random.choice(EMOJIOS))
    await asyncio.sleep(0.0001)
    await Ahh.delete()
    jj = await message.reply_sticker(random.choice(STICKER))
    await asyncio.sleep(0.0001)
    await jj.delete()
    let = await message.reply_text("ʟᴇᴛ ᴍᴇ sᴛᴀʀᴛ")
    await asyncio.sleep(0.002)
    await let.edit("ʟᴇᴛ ᴍᴇ sᴛᴀʀᴛ......")
    await imgg.delete()
    STT = await message.reply_sticker(random.choice(STICKER))
    await asyncio.sleep(0.0001)
    fff = await message.reply_sticker(random.choice(STICKER))
    await STT.delete()
    await asyncio.sleep(0.001)
    await let.delete()
    Hlo = await message.reply_sticker(random.choice(STICKER))
    await asyncio.sleep(0.0001)
    await Hlo.delete()

    M = START_BUTTON(OWNER)
    response = requests.get("https://nekos.best/api/v2/neko").json()
    image_url = response["results"][0]["url"]
    await message.reply_photo(
        image_url,
        caption=START_TEXT.format(message.from_user.mention, Chiku.mention),
        reply_markup=M,
    )
    await fff.delete()
    try:
        if message.chat.type == ChatType.PRIVATE:
            await add_served_user(message.from_user.id)
        else:
            await add_served_chat(message.chat.id)
    except:
        pass
    await Chiku.send_message(LOGGER_ID, f"ꜱᴏᴍᴇᴏɴᴇ ᴊᴜꜱᴛ ꜱᴛᴀʀᴛᴇᴅ {Chiku.mention}\n\nɴᴀᴍᴇ - {message.from_user.mention}\nɪᴅ - {message.from_user.id}\nᴜꜱᴇʀɴᴀᴍᴇ - @{message.from_user.username}")
                                                                                                                                                                

@Chiku.on_cmd("stats")
async def statsbot(client, message):
    if message.from_user.id not in Owner and message.from_user.id not in OWNER_ID:
        return

    response = requests.get("https://nekos.best/api/v2/neko").json()
    m = response["results"][0]["url"]
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await message.reply_photo(
        photo=m,
        caption=f"""ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ᴛᴏᴛᴀʟ ꜱᴛᴀᴛꜱ ᴏꜰ {Chiku.mention}:

➻ ᴄʜᴀᴛs : {chats}
➻ ᴜsᴇʀs : {users}
"""
    )

