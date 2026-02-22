import asyncio
import logging
from bot import Bot

# This ensures the bot starts properly in an async loop
async def start_bot():
    bot = Bot()
    await bot.start()
    # This keeps the bot running forever
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        asyncio.run(start_bot())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped.")
