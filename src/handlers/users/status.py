from aiogram import types
from src.handlers.users.private import private_router
from connect import Database



@private_router.my_chat_member()
async def some_handler(my_chat_member: types.ChatMemberUpdated):
    if my_chat_member.chat.type =='private':
        status = my_chat_member.new_chat_member.status
        user_id = my_chat_member.from_user.id
        if status == 'member':
            await Database.update_user(user_id, 'active')
        elif status == 'kicked':
            await Database.update_user(user_id, 'passive')
        else:
            await Database.update_user(user_id, 'active')


