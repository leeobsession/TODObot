import asyncio
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
from conf import config_bot
from datetime import date, datetime
import random


from keyboard.for_add import start_bot
from keyboard.for_show import clear_task, see_task
from handlers.logic_catalog.logick import form_date
from handlers.my_menu import Form
from sql.bd_show import check_task, check_all_task


router = Router()


DATA_NOW = date.today()


class UserState(StatesGroup):
    task_today = State()
    task_tomorrow = State()
    task_all = State()
    task_user = State()
    del_today = State()
    del_tomorrow = State()
    del_all = State()
    dell_task_user = State()
    chose_yes_or_no = State()


@router.message(F.text=="Продолжить редактировать")
async def today_delit(message: Message, state: FSMContext) -> None:
    await message.reply('Выбери день!', reply_markup=see_task())
    await state.set_state(Form.data_show)


@router.message(Form.data_show, F.text == "Задачи на сегодня.")
async def add_today(message: Message, state: FSMContext) -> None:
    date_task = DATA_NOW
    await state.update_data(text=date_task)
    res = await check_task(date_task, message.chat.id)
    await message.reply(f'''Отправляю тебе задачи на сегодня!

{res}''', reply_markup=clear_task())
    await state.set_state(UserState.task_today)


@router.message(Form.data_show, F.text == "Задачи на завтра.")
async def add_today(message: Message, state: FSMContext) -> None:
    date_task = DATA_NOW
    await state.update_data(text=date_task)
    res = await check_task(date_task, message.chat.id)
    await message.reply(f'''Отправляю тебе задачи на завтра!

{res}''', reply_markup=clear_task())
    await state.set_state(UserState.task_tomorrow)


@router.message(Form.data_show, F.text == "Показать все задачи.")
async def add_today(message: Message, state: FSMContext) -> None:
    res = await check_all_task(message.chat.id)
    await message.reply(f'''Отправляю все твои задачи! 

{res}''', reply_markup=clear_task())
    await state.set_state(UserState.task_all)


@router.message(Form.data_show)
async def get_task(message: Message, state: FSMContext) -> None:
    data_for_show = form_date(message.text)
    res = await check_task(data_for_show, message.chat.id)
    await state.update_data(text=data_for_show)
    await message.reply(f'''Отправляю тебе задачи на {data_for_show}!

{res}''', reply_markup=clear_task())
    await state.set_state(UserState.task_user)