#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 29794396
API_HASH = "c70b56706944684687bcdc069ae80e72"
BOT_TOKEN = "7661367459:AAHqQqu_5HYUsgNkiEPZGc1ufax-IGwhxkk"
SESSION = "1BVtsOIYBu2lLGzvQOwiCM0U7G1uWv3EvxOxeaJZTT0ULk4Bepou7OHJFOodQMFbv7IvUI2j0-wiJ78GdkWOTaHKMs5W-9lN87gjDhv2AZu2t8Z3W_tsO_J34N0xiY5-Yugc8KOct3vzyd9cP8avfhp44Z7DKdaqoNy5bEPxOgkwLthfy775_FPw3bvVWqshRlBXCmhT1-FcLw1z1HDWP04dEKYaPIzuKyUB7VbNiYZ5OqJvXiTlMDYpOQ8G1xxAS_BU3S5BdtWqZevTTY2GGKJoLNO2bGbF9Z1xEZmiVSxoyx-hG9xvEAvwB8oxLuKsxWj2n68noa_OEeOY8_F7pKyuY7NgS2n8="
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
