from pyrogram.client import Client
from vars import *
import time

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Adultzonebot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "Dypixx"},
            sleep_threshold=15,
        )
        self.START_TIME = time.time()

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"::==>> Dypixx Tech <<==::\n┈━═☆ {me.first_name} ☆═━┈")

    async def stop(self, *args):
        await super().stop()
        me = await self.get_me()
        print(f"{me.first_name} is stopped...")

bot = Bot()


'''
Smile, please... 😊
Goodbye forever.

Thank you all for your care and support throughout this journey.

Unfortunately, my @dypixx account has been hacked. The hacker is now using it to promote unknown content. Please be cautious, stay alert, and don’t fall for anything they post.

Take care, stay safe — and once again, thank you for everything.
Goodbye.

— Dypixx
'''