import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

Owner = list(map(int, getenv("Owner", "6764358144 7301077117").split()))
