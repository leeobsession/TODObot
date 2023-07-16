import asyncio
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup
from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from conf import config_bot
from datetime import date, datetime
import random


from keyboard.for_add import start_bot
from keyboard.for_show import see_task
from keyboard.for_yes_no import yes_or_no, again
from handlers.logic_catalog.logick import form_date, random_data
from handlers.show_catalog.show_task import UserState
from sql.bd_show import key_day_task, key_all_task
from sql.bd_user import yes_delit
from handlers.my_menu import Form


router = Router()


DATA_NOW = date.today()


@router.message(UserState.del_today)
async def today_delit(message: Message, state: FSMContext) -> None:
    await state.update_data(task_deliter=message.text)
    await message.reply(f'Ты хочешь удалить {message.text}\U00002049', reply_markup=yes_or_no())
    await state.set_state(UserState.chose_yes_or_no)


@router.message(UserState.del_tomorrow)
async def today_delit(message: Message, state: FSMContext) -> None:
    await state.update_data(task_deliter=message.text)
    await message.reply(f'Ты хочешь удалить {message.text}\U00002049', reply_markup=yes_or_no())
    await state.set_state(UserState.chose_yes_or_no)

@router.message(UserState.del_all)
async def today_delit(message: Message, state: FSMContext) -> None:
    await state.update_data(task_deliter=message.text)
    await message.reply(f'Ты хочешь удалить {message.text}\U00002049', reply_markup=yes_or_no())
    await state.set_state(UserState.chose_yes_or_no)

@router.message(UserState.dell_task_user)
async def today_delit(message: Message, state: FSMContext) -> None:
    await state.update_data(task_deliter=message.text)
    await message.reply(f'Ты хочешь удалить {message.text}\U00002049', reply_markup=yes_or_no())
    await state.set_state(UserState.chose_yes_or_no)

@router.message(UserState.chose_yes_or_no, F.text=="ДА! Удаляем!")
async def today_delit(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    text = data['task_deliter']
    await yes_delit(text, message.chat.id)
    await message.reply('Задача успешно удалена! Востановлению не подлежит \U0001F647', reply_markup=again())
    await state.clear()

@router.message(UserState.chose_yes_or_no, F.text=="НЕТ! Я еще подумаю!")
async def today_delit(message: Message, state: FSMContext) -> None:
    await message.reply('Хорошо, я не буду ее удалять \U0001F645', reply_markup=again())
    await state.clear()



  

