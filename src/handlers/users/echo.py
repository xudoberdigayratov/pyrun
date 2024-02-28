from aiogram import types
from src.handlers.users.private import private_router, IsPrivate

@private_router.message(IsPrivate())
async def echo(message: types.Message):
    await message.answer("Sorry, I couldn't understand that, do you need /help ?")