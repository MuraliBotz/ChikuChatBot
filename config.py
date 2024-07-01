import os
from os import getenv


API_ID = int(os.environ.get("API_ID"))


API_HASH = os.environ.get("API_HASH")


BOT_TOKEN = os.environ.get("BOT_TOKEN")


OWNER_ID = list(
    map(int, getenv("OWNER_ID", "6764358144").split())
) 

#Fill Only Username Without @
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "MuraliBotz"
)  

MONGO_URL = os.environ.get("MONGO_URL")

LOGGER_ID = int(getenv("LOGGER_ID", "-1002242562595"))

# set True if you want yo set bot commands automatically 
SETCMD = getenv("SETCMD", "True")

# upstream repo 
UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/MuraliBotz/ChikuChatBot",
)

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

# GIT TOKEN ( if your edited repo is private)
GIT_TOKEN = getenv("GIT_TOKEN", None)
