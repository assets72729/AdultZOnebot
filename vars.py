import os
from typing import List

API_ID = int(os.getenv("API_ID", "24890303"))
API_HASH = os.getenv("API_HASH", "94cf78d1e6883ecb10f32e31fc23cfe0")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_URI", "")
DATABASE_CHANNEL_ID = int(os.getenv("DATABASE_CHANNEL_ID", "-1002723839767"))
ADMIN_ID = int(os.getenv("ADMIN_ID", "7289855833"))
LOG_CHNL = int(os.getenv("LOG_CHNL", "-1002890514174"))
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "HiiWlcme") # Without @
IS_FSUB = bool(os.environ.get("FSUB", True))
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002705791364").split()))
DATABASE_CHANNEL_LOG = int(os.getenv("DATABASE_CHANNEL_ID", "-1002890514174"))
FREE_VIDEO_DURATION = int(os.getenv("FREE_VIDEO_DURATION", "240"))


'''
Smile, please... 😊
Goodbye forever.

Thank you all for your care and support throughout this journey.

Unfortunately, my @dypixx account has been hacked. The hacker is now using it to promote unknown content. Please be cautious, stay alert, and don’t fall for anything they post.

Take care, stay safe — and once again, thank you for everything.
Goodbye.

— Dypixx
'''