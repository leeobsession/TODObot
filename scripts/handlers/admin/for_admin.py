import asyncio
import logging

from datetime import date
from aiogram import Router, F, Bot, html
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
import apscheduler

from conf import config_bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from conf.settings import settings
from sql.bd_user import get_name, save_user, get_id
from keyboard.for_add import start_bot
from middlewares.appshed import check_and_call, SchedulerMiddleware
from sql.bd_user import get_name, save_user, get_id
from sql.bd_shedule import check_shedul, show_shedul_task, list_id
from handlers.logic_catalog.logick import format_task


DATA_NOW = date.today()


router = Router()


async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Бот запущен!")


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Бот выключен!")


async def loger_error(bot: Bot, messages: str):
    await bot.send_message(settings.bots.admin_id, text=f"{messages}")


@router.message(Command(commands=["start_call"]))
async def cmd_start(message: Message, bot: Bot, apscheduler: AsyncIOScheduler)-> None:
    await bot.send_message(settings.bots.admin_id, text="Включаю всем оповещения!")
    apscheduler.add_job(check_and_call, trigger='cron', hour=9, day='*',  kwargs={'bot': bot}, id='start_job')
    #apscheduler.add_job(test_shedule, trigger='cron', minute='*/5', kwargs={'bot': bot}, id='start_test')

@router.message(Command(commands=["stop_call"]))
async def cmd_stop(message: Message, bot: Bot, apscheduler: AsyncIOScheduler)-> None:
    await bot.send_message(settings.bots.admin_id, text="Отключаю оповещения!")
    apscheduler.remove_job('start_job')
    #apscheduler.remove_job('start_test')

