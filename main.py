import asyncio
from connect import dp, bot, create_tables
from src import handlers, middlewares
from src.handlers.admins.panel import admin_router
from src.handlers.groups.command import group_router
from src.handlers.users.private import private_router
from src.middlewares import ThrottlingMiddleware
from src.utils.set_bot_commands import set_default_commands
from src.utils.notify_admins import on_startup_notify

async def main():
    await on_startup_notify()
    await create_tables()
    await set_default_commands()
    dp.message.middleware.register(ThrottlingMiddleware(slow_mode_delay=0.5))
    dp.include_router(router=admin_router)
    dp.include_router(router=group_router)
    dp.include_router(router=private_router)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())