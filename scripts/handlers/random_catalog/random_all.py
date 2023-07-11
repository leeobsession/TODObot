import asyncio
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from conf import config_bot
from datetime import date, datetime
import random

from keyboard.for_add import start_bot
from handlers.logic_catalog.logick import form_date, random_data
from sql.bd_rand import get_random
from handlers.random_catalog.random import UserState
from sql.bd_task import save_task, save_random


router = Router()


DATA_NOW = date.today()


@router.message(UserState.all_task, F.text=="Рандомная дата! \U00002620")
async def dat_all(message: Message, state: FSMContext) -> None:
    data_rand = random_data(DATA_NOW)
    num = random.randrange(1, 25)
    task = await get_random(num)
    await save_random(task, data_rand, message.chat.id)
    await message.reply(f'Ты крутой! Твоя задача {task}, добавлена на {data_rand}!', reply_markup=start_bot())
    await state.clear()

@router.message(UserState.all_task)
async def user_random_all(message: Message, state: FSMContext) -> None:
    data_rand = form_date(message.text)
    num = random.randrange(1, 25)
    task = await get_random(num)
    await save_random(task, data_rand, message.chat.id)
    await message.reply(f'Ты крутой! Твоя задача {task}, добавлена на {data_rand}!', reply_markup=start_bot())
    await state.clear()
