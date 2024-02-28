from aiogram.filters import BaseFilter
from aiogram.types import Message

class IsGroup(BaseFilter):
    async def __call__(self, message:Message):
        return message.chat.type in ["group", "supergroup"]

