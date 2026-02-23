#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
from pyrogram import Client

if os.environ.get("ENV", False):
    from sample_config import Config
    from sample_config import LOGGER
else:
    from config import Config
    from config import LOGGER

class User(Client):
    def __init__(self):
        session = Config.TG_USER_SESSION
        
        # Check if the session is a long String Session (BQ...) or a simple filename
        if session and len(session) > 60:
            super().__init__(
                name="actual_user_session",
                session_string=session, # This handles the long code correctly
                api_hash=Config.API_HASH,
                api_id=Config.APP_ID,
                workers=4
            )
        else:
            super().__init__(
                session, # This handles old-style filenames
                api_hash=Config.API_HASH,
                api_id=Config.APP_ID,
                workers=4
            )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username} started!"
        )
        return self, usr_bot_me.id

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
