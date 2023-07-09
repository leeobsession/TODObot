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


from keyboard.for_add import start_bot
from handlers.logic_catalog.logick import form_date, random_data
from handlers.show_catalog.show_task import UserState
from sql.bd_show import key_day_task, key_all_task


router = Router()


DATA_NOW = date.today()


@router.message(UserState.task_today, F.text == "Редактировать задачи.")
async def today_delit(message: Message, state: FSMContext) -> None:
    date_task = DATA_NOW
    res = await key_day_task(date_task, message.chat.id)
    kb = ReplyKeyboardBuilder()
    for i in res:
        kb.add(types.KeyboardButton(text=''.join(i)))
    kb.button(text="Вернуться в меню")
    kb.adjust(1)
    await message.reply('Выбери задачу которую хотел бы удалить. ОСТОРОЖНО! Востановлению не подлежит!', reply_markup=kb.as_markup(resize_keyboard=True))
    await state.set_state(UserState.del_today)


@router.message(UserState.task_tomorrow, F.text == "Редактировать задачи.")
async def today_delit(message: Message, state: FSMContext) -> None:
    date_task = DATA_NOW.replace(day=DATA_NOW.day+1)
    res = await key_day_task(date_task, message.chat.id)
    kb = ReplyKeyboardBuilder()
    for i in res:
        kb.add(types.KeyboardButton(text=''.join(i)))
    kb.button(text="Вернуться в меню")
    kb.adjust(1)
    await message.reply('Выбери задачу которую хотел бы удалить. ОСТОРОЖНО! Востановлению не подлежит!', reply_markup=kb.as_markup(resize_keyboard=True))
    await state.set_state(UserState.del_tomorrow)

@router.message(UserState.task_all, F.text == "Редактировать задачи.")
async def today_delit(message: Message, state: FSMContext) -> None:
    res = await key_all_task(message.chat.id)
    kb = ReplyKeyboardBuilder()
    for i in res:
        kb.add(types.KeyboardButton(text=''.join(i)))
    kb.button(text="Вернуться в меню")
    kb.adjust(1)
    await message.reply('Выбери задачу которую хотел бы удалить. ОСТОРОЖНО! Востановлению не подлежит!', reply_markup=kb.as_markup(resize_keyboard=True))
    await state.set_state(UserState.del_all)

@router.message(UserState.task_user, F.text == "Редактировать задачи.")
async def today_delit(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    dat = data["text"]
    res = await key_day_task(dat, message.chat.id)
    kb = ReplyKeyboardBuilder()
    for i in res:
        kb.add(types.KeyboardButton(text=''.join(i)))
    kb.button(text="Вернуться в меню")
    kb.adjust(1)
    await message.reply('Выбери задачу которую хотел бы удалить. ОСТОРОЖНО! Востановлению не подлежит!', reply_markup=kb.as_markup(resize_keyboard=True))
    await state.set_state(UserState.dell_task_user)