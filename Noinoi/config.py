import os
from os import getenv
from dotenv import load_dotenv
from Noinoi.DREAMS.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQCbBG5IUa0Oh_r-h5kAcupsPQUefNMmH7hzrWppaMaZWpzN-x3DTylBpKipbr2dHjd8CltY6ooNBLOTOncZFJkjAfRV3ggN0bfN_sn9-emnY6JOYrq2lw2SkzQZVj_bwDjr3FtwAy6NTiiFGyYU50IsnE8Oqv_rnXLL_sQKrvNCBbxdDOiuXizePLEyZTg6mr75HSXX51UCO41SmLqQnSRs7fEK8bwn6-yMXqOx-1ObmNiSFZZDYOnp2PKHhyfmatawXWpeC42r7FCe9oCHGPrF_cO4OeViV5h5P8gSVCL5heauh917LNsVV2IwVSqqk9uTWu6CRVzKco5ON-ScOrG-AAAAASrnbxEA")
BOT_TOKEN = getenv("BOT_TOKEN", "5007724504:AAFm7cZ50CRv0FjDZmaZ77Fh6YsxoW83Tw0")
BOT_NAME = getenv("BOT_NAME", " Alexa bot")
API_ID = int(getenv("API_ID", "9273779"))
API_HASH = getenv("API_HASH", "287aab6efb13cdd2f042232e704d26ce")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/5b395a5e54aee892814dc.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/ce5c01d04da27473b5b42.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/ce5c01d04da27473b5b42.jpg")
OWNER_NAME = getenv("OWNER_NAME", "Stargirl_xdd")
ALIVE_NAME = getenv("ALIVE_NAME", "I am Alive 🔥")
BOT_USERNAME = getenv("BOT_USERNAME", "Thealexa_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Tsf_founder")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "https://t.me/starz_support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/starz_bots")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001724276398"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5032100535").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/5b395a5e54aee892814dc.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "200"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/starzbots/tsf")
