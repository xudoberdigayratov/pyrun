from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.formatting import Text
from connect import *
from src.filters import IsSuperAdmin

admin_router = Router()
admin_router.message.filter(IsSuperAdmin())

@admin_router.message(Command(commands=['stat'], prefix='.!/'))
async def stat(message: types.Message):
    all_user, active_user, one_day_user, one_month_user = await Database.count_user(), await Database.count_active_user(), await Database.count_user_one_now(), await Database.count_user_one_month()

    all_group, active_group, one_day_group, one_month_group = await Database.count_group(), await Database.count_active_group(), await Database.count_group_one_now(), await Database.count_group_one_month()
    text = f"""🧑🏻‍💻 <b>Subscribers on bot: <code>{all_user}</code>

Active subscribers: <code>{active_user}</code>
In the last 24 hours: <code>{one_day_user}</code> subscribers added
Last 1 month: <code>{one_month_user}</code> subscribers added

➖➖➖➖➖➖➖➖➖➖

👥 Groups in bot: <code>{all_group}</code>

Active Groups: <code>{active_group}</code>
In the last 24 hours: <code>{one_day_group}</code> groups have been added
In the last 1 month: <code>{one_month_group}</code> groups have been added</b>
"""
    await message.answer(text)
