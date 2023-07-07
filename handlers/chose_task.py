import asyncio
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
from conf import config_bot
from datetime import date, datetime
import random

from sql.bd_task import save_date, save_task
from keyboard.for_add import start_bot
from handlers.logic_catalog.logick import form_date, random_data
from handlers.my_menu import Form

router = Router()


DATA_NOW = date.today()


@router.message(Form.data_task, F.text == "На сегодня")
async def add_today(message: Message, state: FSMContext) -> None:
    date_task = DATA_NOW
    await save_date(date_task, message.chat.id)
    await state.update_data(text=date_task)
    await message.reply("Я запомнил! И чем ты планируешь заняться сегодня?", input_field_placeholder="Напиши мне свою задачу!")
    await state.set_state(Form.task)


@router.message(Form.data_task, F.text=="На завтра")
async def add_tommorow(message: Message, state: FSMContext) -> None:
    date_task = DATA_NOW.replace(day=DATA_NOW.day+1)
    await save_date(date_task, message.chat.id)
    await state.update_data(text=date_task)
    await message.reply("Чем ты хочешь заняться завтра?", input_field_placeholder="Напиши мне свою задачу!")
    await state.set_state(Form.task)


@router.message(Form.data_task)
async def user_data(message: Message, state: FSMContext) -> None:
    task_data = form_date(message.text)
    await save_date(task_data, message.chat.id)
    await state.update_data(text=task_data)
    await message.reply(f"Твоя будет сохранена на {message.text}, теперь напиши, чем ты хочешь заняться")
    await state.set_state(Form.task)


@router.message(Form.task)
async def get_task(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    dat = data["text"]
    await save_task(message.text, message.chat.id, dat)
    await message.reply(f'Отлично, твоя задача {message.text}, добавлена на {dat}', reply_markup=start_bot())
    await state.clear()
