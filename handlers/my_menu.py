import asyncio
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from conf import config_bot


from keyboard.for_add import add_date, category_task
from keyboard.for_show import see_task


router = Router()



class Form(StatesGroup):
    data_task = State()
    data_random = State()
    data_show = State()
    task = State()

@router.message(F.text=="Добавить свою задачу. \U0000270D")
async def add_task(message: Message, state: FSMContext) -> None:
    await message.reply("Теперь укажи дату в формате dd.mm.YYYY",  reply_markup=add_date())
    await state.set_state(Form.data_task)


@router.message(F.text=="Добавить рандомную задачу \U0001F939")
async def chose_random(message: Message, state: FSMContext) -> None:
    await message.answer("Смело! Теперь выбери категорию, и я придумаю задачу для тебя! :3", reply_markup=category_task())
    await state.set_state(Form.data_random)


@router.message(F.text=='Просмотр задач \U0001F440')
async def add_task(message: Message, state: FSMContext) -> None:
    await message.reply("Что бы посмотреть задачи на определенный день просто укажи дату в формате dd.mm.YYYY", reply_markup=see_task())
    await state.set_state(Form.data_show)
