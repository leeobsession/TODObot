import asyncio 
import aiogram
from datetime import date
from typing import Dict, Any, Callable, Awaitable
from aiogram import BaseMiddleware
from aiogram.types.base import TelegramObject
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
from aiogram import Dispatcher, F, Router, html, types
from aiogram.types import (
    CallbackQuery,
    ChatMemberUpdated,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from sql.bd_shedule import check_shedul, show_shedul_task
from conf import config_bot
from keyboard.for_add import start_bot
from handlers.logic_catalog.logick import format_task

DATA_NOW = date.today()


router = Router()
scheduler = AsyncIOScheduler()

class SchedulerMiddleware(BaseMiddleware):
    def __init__(self, scheduler: AsyncIOScheduler):
        self.scheduler = scheduler
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        data["apscheduler"] = self.scheduler
        return await handler(event,data)


async def check_and_call(bot: Bot, user_id: int) -> None:
    res = await check_shedul(DATA_NOW, user_id)
    if res is True:
        call_user = await show_shedul_task(DATA_NOW, user_id)
        print(call_user)
        task = format_task(call_user)
        await bot.send_message(chat_id=user_id, text=f"""Привет! Не забудь про сегодняшние задачи!

        {task}""", reply_markup = start_bot())
    else:
        await bot.send_message(chat_id=user_id, text="Привет! Запишешь что-нибудь сегодня?", reply_markup = start_bot())

