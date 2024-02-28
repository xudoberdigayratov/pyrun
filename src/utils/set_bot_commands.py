from aiogram import types
from connect import bot

async def set_default_commands():
    await bot.set_my_commands(
        [
            types.BotCommand(command='start', description='restart'),
            types.BotCommand(command="help", description="help"),
            types.BotCommand(command="python", description="python"),
            types.BotCommand(command="python3", description="python"),
            types.BotCommand(command="py", description="python"),
        ]
    )
