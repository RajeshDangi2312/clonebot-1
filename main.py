import asyncio
import logging
import sys
from bot import Bot

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start_bot():
    """Main entry point to start the bot and keep it running."""
    try:
        logger.info("Initializing Bot...")
        bot = Bot()
        await bot.start()
        logger.info("Bot is Live!")
        
        # This keeps the bot active and prevents the script from closing
        await asyncio.Event().wait()
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")

if __name__ == "__main__":
    # asyncio.run is the modern, safe way to start the loop.
    # It handles creating the loop and closing it automatically.
    try:
        asyncio.run(start_bot())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot execution stopped by user.")
        sys.exit(0)
