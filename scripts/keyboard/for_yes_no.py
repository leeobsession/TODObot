from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def yes_or_no() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="ДА! Удаляем!")
    kb.button(text="НЕТ! Я еще подумаю!")
    kb.button(text="Вернуться в меню")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True)

def again() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Продолжить редактировать")
    kb.button(text="Вернуться в меню")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True)