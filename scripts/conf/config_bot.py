import asyncio
import logging
from aiogram import Bot, Dispatcher, F, Router, html, types
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy
from handlers import start, my_menu, chose_task, appshed
from handlers.random_catalog import random, random_sport, random_home, random_hobby, random_all
from handlers.show_catalog import show_task, delit_task, y_n
from dotenv import get_variables
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handlers.appshed import check_and_call

config = get_variables('/home/lee_obsession/TODObot/scripts/conf/.evn')
TOKEN = config['TOKEN']


router = Router()


async def configurat():
    bot = Bot(token=TOKEN)
    logging.basicConfig(level=logging.INFO, filename='bot.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    dp = Dispatcher(storage=MemoryStorage(), fsm_strategy=FSMStrategy.USER_IN_CHAT)
    dp.include_routers(router, start.router, my_menu.router, chose_task.router)
    dp.include_routers(random.router, random_sport.router, random_all.router, random_home.router, random_hobby.router)
    dp.include_routers(show_task.router, delit_task.router, y_n.router)
    dp.include_routers(appshed.router)
    scheduler = AsyncIOScheduler()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(configurat())