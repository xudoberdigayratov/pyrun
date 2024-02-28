from aiogram import types
from connect import Database
from src.handlers.groups.command import group_router, IsGroup


@group_router.my_chat_member(IsGroup())
async def get_status(message: types.ChatMemberUpdated):
    chat_type = message.chat.type
    if chat_type in ('supergroup', 'group'):
        new_member = message.new_chat_member
        old_member = message.old_chat_member
        chat_id = message.chat.id
        if new_member.status == 'member' and old_member.status != 'administrator':
            await Database.update_groups(chat_id, 'active')
        elif new_member.status == 'administrator':
            await Database.update_groups(chat_id, 'active')
        elif new_member.status.LEFT:
            await Database.update_groups(chat_id, 'passive')
