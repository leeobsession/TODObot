import asyncio
import logging
import tg_logger
import contextlib
import openai 
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
from handlers.admin import for_admin
from handlers.gpt_catalog import gpt
from handlers.admin.for_admin import start_bot, stop_bot, loger_error
from middlewares.appshed import SchedulerMiddleware, check_and_call


DATA_NOW = date.today()


router = Router()


async def configurat():
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    logging.basicConfig(
        level=logging.INFO, 
        filename='bot_info.log', 
        format='%(asctime)s - %(name)s  - %(module)s - %(levelname)s',
        datefmt='%H:%M:%S',
        )
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)

    dp = Dispatcher(storage=MemoryStorage(), fsm_strategy=FSMStrategy.USER_IN_CHAT)
    
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    
    scheduler = AsyncIOScheduler(timezone='Asia/Vladivostok')
    scheduler.start()
    dp.update.middleware.register(SchedulerMiddleware(scheduler))
    dp.include_routers(router, start.router, my_menu.router, chose_task.router, horoscope.router)
    dp.include_routers(random.router, random_sport.router, random_all.router, random_home.router, random_hobby.router)
    dp.include_routers(show_task.router, delit_task.router, y_n.router, for_admin.router)
    dp.include_routers(gpt.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(configurat())
