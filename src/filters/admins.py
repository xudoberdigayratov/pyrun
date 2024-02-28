from aiogram.filters import BaseFilter
from aiogram.types import Message
from connect import config

class IsSuperAdmin(BaseFilter):
    async def __call__(self, message:Message):
        if message.chat.type == 'private':
            user_id = message.from_user.id
            if str(user_id) in config.bot.admin:
                return True
            else:
                return False
        else:
            return False