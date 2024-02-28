import time

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message
from connect import Database


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, slow_mode_delay=0.5):
        self.user_timeouts = {}
        self.slow_mode_delay = slow_mode_delay
        super(ThrottlingMiddleware, self).__init__()

    async def __call__(self, handler, event: Message, data):
        user_id = event.from_user.id
        chat_type = event.chat.type
        if chat_type == 'private':
            current_time = time.time()
            await Database.add_user(user_id=event.from_user.id)
            # Checking if there is a record of this user's last request
            last_request_time = self.user_timeouts.get(user_id, 0)
            if current_time - last_request_time < self.slow_mode_delay:
                # Enable slow mode if requests are too frequent
                await event.reply("Too many requests! Wait a moment.")
                return

            else:
                # Update the time of the last request
                self.user_timeouts[user_id] = current_time
                # Pass the event to the handler
                return await handler(event, data)
        else:
            if chat_type in ('group', 'supergroup'):
                await Database.add_groups(user_id=event.chat.id)

            return await handler(event, data)
