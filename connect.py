from data.config import load_config
from db_api.init_db import DBConnection
from db_api.database import SQLAlchemySession
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy

config = load_config(path='.env')

bot = Bot(config.bot.token, parse_mode=ParseMode.HTML)
stroge = MemoryStorage()
dp = Dispatcher(storage=stroge, fsm_strategy=FSMStrategy.CHAT)



async def create_tables():
    await DBConnection.main()


Database: SQLAlchemySession = SQLAlchemySession(f"mysql+asyncmy://{config.db.user}:{config.db.password}@{config.db.host}/{config.db.database}")

