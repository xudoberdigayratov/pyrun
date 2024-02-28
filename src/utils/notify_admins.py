from connect import config, bot
import logging

async def on_startup_notify():
    for admin in config.bot.admin:
        try:
            await bot.send_message(chat_id=admin, text="Bot Started!")
        except Exception as Err:
            logging.exception(Err)
