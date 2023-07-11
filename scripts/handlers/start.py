import asyncio
import logging
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove
from conf import config_bot

from sql.bd_user import get_name, check_user, save_id, get_id
from keyboard.for_add import start_bot


router = Router()


class StartForm(StatesGroup):
    name = State() 
    menu_for_user = State()

logging.basicConfig(level=logging.INFO, filename='bot.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


@router.message(Command(commands=["start"]))
async def cmd_start(message: Message, state: FSMContext)-> None:
    chat_id = message.chat.id
    print(chat_id)
    users = await get_id(chat_id)
    print(users)
    if chat_id == users:
        name_user = await get_name(chat_id)
        await message.answer(f'Приятно снова тебя увидеть {name_user}', input_field_placeholder="Добавь или посмотри свои задачи", reply_markup=start_bot())
    else:
        await message.answer("Привет! Давай познакомимся! Напиши пожалуйста мне свое имя, что бы я мог тебя запомнить!")
        await state.set_state(StartForm.name)


@router.message(StartForm.name)
async def process_name(message: Message, state: FSMContext) -> None:
    chat_id = message.chat.id
    name = message.text
    await save_id(chat_id, name)
    await state.update_data(text=name)
    await message.answer(f'Приятно познакомится {name}! Теперь можешь добавить задачу, и я ее тоже запомню! :3', reply_markup=start_bot())
    await state.clear()


@router.message(F.text=="Вернуться в меню")
async def back(message: Message, state: FSMContext) -> None:
    await message.answer("Ты передумал?", reply_markup=start_bot())
    await state.clear()
