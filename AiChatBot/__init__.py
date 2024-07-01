import asyncio
import logging
import time
from importlib import import_module
from os import listdir, path
from dotenv import load_dotenv
import config
import pymongo
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, OWNER_ID
from pyrogram.enums import ParseMode, ChatMemberStatus
from Abg import patch

loop = asyncio.get_event_loop()
load_dotenv()
boot = time.time()


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pymongo").setLevel(logging.ERROR)

# Hehehe

class ChikuBot(Client):
    def __init__(self):
        super().__init__(
            name="Chikubot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            lang_code="en",
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.DEFAULT,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention
        try:
            await self.resolve_peer(config.LOGGER_ID)
            await self.send_message(config.LOGGER_ID, f"๏ {self.mention} sᴛᴀʀᴛᴇᴅ ➛ \n\n๏ ɴᴀᴍᴇ ➛ {self.name}\n๏ ɪᴅ ➛ {self.id}\n๏ ᴜsᴇʀɴᴀᴍᴇ ➛ @{self.username} \n\n||ᴍᴀᴅᴇ ʙʏ ᴍᴜʀᴀʟɪ 🥀 ||")
        except:
            pass

    async def stop(self):
        await super().stop()
        
            


Chiku = ChikuBot()



#from AiChatBot.Db import git

#Up = git()

