import asyncio
import logging


from datetime import datetime, date
from aiogram import Bot, Dispatcher, F, Router, types, html
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.strategy import FSMStrategy
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from conf.settings import settings
from handlers import start, my_menu, chose_task
from handlers.random_catalog import random, random_sport, random_home, random_hobby, random_all
from handlers.show_catalog import show_task, delit_task, y_n
from handlers.horoscope_catalog import horoscope
from middlewares.appshed import SchedulerMiddleware, check_and_call



DATA_NOW = date.today()


router = Router()

async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Бот запущен!")


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Бот выключен!")


async def configurat():
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO, filename='bot.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    dp = Dispatcher(storage=MemoryStorage(), fsm_strategy=FSMStrategy.USER_IN_CHAT)
    
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    
    scheduler = AsyncIOScheduler(timezone='Asia/Vladivostok')
    scheduler.start()
    dp.update.middleware.register(SchedulerMiddleware(scheduler))
    dp.include_routers(router, start.router, my_menu.router, chose_task.router, horoscope.router)
    dp.include_routers(random.router, random_sport.router, random_all.router, random_home.router, random_hobby.router)
    dp.include_routers(show_task.router, delit_task.router, y_n.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(configurat())
