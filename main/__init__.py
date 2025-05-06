#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
PORT = int(env.get("PORT", 8080))
BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
API_ID = 29794396
API_HASH = "c70b56706944684687bcdc069ae80e72"
BOT_TOKEN = "7661367459:AAHqQqu_5HYUsgNkiEPZGc1ufax-IGwhxkk"
SESSION = "BQHGoFwAucc7P_WPxtTva47hCvNWdq08n_CLHMwVgsiiinxnFqP11mvkbBQ0nXWyrdkJ6f3wq__wlZle2ViFHvDmY9yZ7dZjc54M3ittT0V22mbf24SGKfZzlBBaVh38GiVzDZ-5mQOlJg8zPB4ucAiqjVnFZMWXzwOgwBIbfFz6VnB0_8Jh3RxyXYqM0Fy0KIKWzVEOF3NPAbm8jlIE7r9Vf0v3c6i_55ElVCDXlcSda9KfaW4iGXvURyqqh3Qn3ikQxyWiMj9ftY_nTtaZFJKUE-6gB5pqzSfDai_nrprjfodNXWt_a-qXLJgKnVjcE4719QdUYnOuuJtgNH4zvzP6pJIVpwAAAAFfM6NEAA"
FORCESUB = "anisharedone"
AUTH = 5892186948

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
