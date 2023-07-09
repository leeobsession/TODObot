import asyncio 
import aiogram
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram import Bot, Dispatcher, F, Router, html, types
from aiogram.types import (
    CallbackQuery,
    ChatMemberUpdated,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from sql.bd_shedule import shed_user, check_shedul, show_shedul_task
from conf import config_bot
from datetime import date
import datetime
from keyboard.for_add import start_bot

DATA_NOW = date.today()


router = Router()


@router.message()
async def check_and_call(bot: Bot):
    users = await shed_user()
    for user in users:
        res = await check_shedul(DATA_NOW, user)
        if res is True:
            call_user = await show_shedul_task(DATA_NOW, user)
            await bot.send_message(chat.id == user, text = f"""Привет! Не забудь про сегодняшние задачи!
            {call_user}""", reply_markup = start_bot())
        else:
            await bot.send_message(chat.id == user, text = f"Привет! Запишешь что-нибудь сегодня?", reply_markup = start_bot())

async def callback():
    await scheduler.every().day.at("09:00").do(check_and_call())
    while True:
        await scheduler.run_pending()
        await scheduler.start()
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(callback())

