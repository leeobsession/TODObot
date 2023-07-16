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
from sql.bd_rand import get_home
from sql.bd_user import save_task, save_random
from handlers.random_catalog.random import UserState


router = Router()


DATA_NOW = date.today()


class Form(StatesGroup):
    data_random = State()


@router.message(UserState.home_task, F.text=="Рандомная дата! \U0001FAA0")
async def dat_home(message: Message, state: FSMContext) -> None:
    data_rand = random_data(DATA_NOW)
    num = random.randrange(1, 17)
    task = await get_home(num)
    await save_random(task, data_rand, message.chat.id)
    await message.reply(f'Ты крутой! Твоя задача \U000026AB {task} \U000026AB, добавлена на {data_rand}\U00002714', reply_markup=start_bot())
    await state.clear()

@router.message(UserState.home_task)
async def dat_sport(message: Message, state: FSMContext) -> None:
    data_rand = random_data(DATA_NOW)
    num = random.randrange(1, 17)
    task = await get_home(num)
    await save_random(task, data_rand, message.chat.id)
    await message.reply(f'Ты крутой! Твоя задача \U000026AB {task} \U000026AB, добавлена на {data_rand}\U00002714', reply_markup=start_bot())
    await state.clear()