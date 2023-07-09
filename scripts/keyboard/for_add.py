from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start_bot() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Добавить свою задачу. \U0000270D")
    kb.button(text="Добавить рандомную задачу \U0001F939")
    kb.button(text="Просмотр задач \U0001F440")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Добавь или посмотри свои задачи")


def add_date() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="На сегодня")
    kb.button(text='На завтра')
    kb.button(text="Вернуться в меню")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="dd.mm.YYYY")


def category_task() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Фитнес \U0001F3CB", callback_data="Фитнес \U0001F3CB")
    kb.button(text='Домашние дела \U0001FAA0', callback_data="Домашние дела \U0001FAA0")
    kb.button(text="Развлечения \U0001F483", callback_data="Развлечения \U0001F483")
    kb.button(text="Любая \U00002620", callback_data="Любая \U00002620")
    kb.button(text="Вернуться в меню")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True)
