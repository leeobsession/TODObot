import asyncio
import logging
from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
import apscheduler
from conf import config_bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from sql.bd_user import get_name, save_user, get_id
from keyboard.for_add import start_bot
from middlewares.appshed import check_and_call, SchedulerMiddleware

router = Router()


class StartForm(StatesGroup):
    name = State() 
    gpt_call = State()

@router.message(Command(commands=["start"]))
async def cmd_start(message: Message, bot: Bot, state: FSMContext)-> None:
    chat_id = message.chat.id
    users = await get_id(chat_id)
    if chat_id == users:
        name_user = await get_name(chat_id)
        await message.answer(f'Приятно снова тебя увидеть {name_user} \U0001F970!', reply_markup=start_bot())
    else:
        await message.answer("Привет! Давай познакомимся! Напиши пожалуйста мне свое имя, что бы я мог тебя запомнить! \U0001F63B")
        await state.set_state(StartForm.name)


@router.message(StartForm.name)
async def process_name(message: Message, bot: Bot, state: FSMContext) -> None:
    chat_id = message.chat.id
    name = message.text
    await save_user(chat_id, name)
    await state.update_data(text=name)
    await message.answer(f'Приятно познакомится {name} \U00002764! Я могу запомнить и сохранить твои задачи, рассказать гороскоп на сегодня или ты можешь написать в чат, что бы позвать умного помощника Тошу :3', reply_markup=start_bot())    
    await state.clear()
    await state.set_state(Form.gpt_call)

@router.message(Command(commands=["main_menu"]))
async def cmd_menu(message: Message, bot: Bot, state: FSMContext)-> None:
    await message.answer("Чем займемся?", reply_markup=start_bot())


@router.message(F.text=="Вернуться в меню")
async def back(message: Message, state: FSMContext) -> None:
    await message.answer("Ты передумал? \U0001F648", reply_markup=start_bot())
    await state.clear()
