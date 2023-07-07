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
from keyboard.for_random import rand_s, rand_h, rand_hob, rand_all
from handlers.logic_catalog.logick import form_date, random_data
from handlers.my_menu import Form


class UserState(StatesGroup):
    fitnes = State()
    home_task = State()
    hobby_task = State()
    all_task = State()


router = Router()


@router.message(Form.data_random, F.text=="Фитнес \U0001F3CB")
async def chose_sport(message: Message, state: FSMContext) -> None:
    await message.reply("Ты выбрал задание на спорт! Теперь напиши дату в формате dd.mm.YYYY или жмякни на кнопку что бы я выбрал дату за тебя :3", reply_markup=rand_s())
    await state.set_state(UserState.fitnes)


@router.message(Form.data_random, F.text=="Домашние дела \U0001FAA0")
async def chose_home(message: Message, state: FSMContext) -> None:
    await message.reply("Ты выбрал дела по дому, поэтому напиши мне дату в формате dd.mm.YY и готовь веник!", reply_markup=rand_h())
    await state.set_state(UserState.home_task)


@router.message(Form.data_random, F.text=="Развлечения \U0001F483")
async def chose_hobby(message: Message, state: FSMContext) -> None:
    await message.reply("Сейчас я подберу что-нибудь что бы тебя развлечь! Только напиши дату в формате dd.mm.YYY или жмякая кнопку!", reply_markup=rand_hob())
    await state.set_state(UserState.hobby_task)


@router.message(Form.data_random, F.text=="Любая \U00002620")
async def chose_all(message: Message, state: FSMContext) -> None:
    await message.reply("Ого! Ты смельчак! Тогда я выберу на свой вкус! Жмякая на кнопку или напиши дату сам в формате dd.mm.YYYY!", reply_markup=rand_all())
    await state.set_state(UserState.all_task)
