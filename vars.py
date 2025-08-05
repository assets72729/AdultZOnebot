import os
from typing import List

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_URI", "")
DATABASE_CHANNEL_ID = int(os.getenv("DATABASE_CHANNEL_ID", ""))
ADMIN_ID = int(os.getenv("ADMIN_ID", ""))
LOG_CHNL = int(os.getenv("LOG_CHNL", ""))
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "HiiWlcme") # Without @
IS_FSUB = bool(os.environ.get("FSUB", True))
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "").split()))
DATABASE_CHANNEL_LOG = int(os.getenv("DATABASE_CHANNEL_ID", ""))
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
