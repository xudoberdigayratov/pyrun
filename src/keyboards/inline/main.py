from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from connect import bot

async def add_group():
    bot_ = await bot.get_me()
    keyboard = InlineKeyboardBuilder()
    keyboard.row(InlineKeyboardButton(text="• Add Group •", url=f"https://telegram.me/{bot_.username}?startgroup=new"))
    return keyboard.as_markup()