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
from sql.bd_rand import save_random, get_hobby
from handlers.random_catalog.random import UserState
from sql.bd_task import save_task

router = Router()


DATA_NOW = date.today()


@router.message(UserState.hobby_task, F.text=="Рандомная дата! \U0001F483")
async def dat_hobby(message: Message, state: FSMContext) -> None:
    data_rand = random_data(DATA_NOW)
    num = random.randrange(1, 17)
    task = await get_hobby(num)
    await save_task(task, message.chat.id, data_rand)
    await message.reply(f'Ты крутой! Твоя задача {task}, добавлена на {data_rand}!', reply_markup=start_bot())
    await state.clear()

@router.message(UserState.hobby_task)
async def dat_sport(message: Message, state: FSMContext) -> None:
    data_rand = random_data(DATA_NOW)
    num = random.randrange(1, 17)
    task = await get_hobby(num)
    await save_task(task, message.chat.id, data_rand)
    await message.reply(f'Ты крутой! Твоя задача {task}, добавлена на {data_rand}!', reply_markup=start_bot())
    await state.clear()