from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def see_task() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Задачи на сегодня.")
    kb.button(text="Задачи на завтра.")
    kb.button(text="Показать все задачи.")
    kb.button(text="Вернуться в меню")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="dd.mm.YYYY")

def clear_task() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Редактировать задачи.")
    kb.button(text="Вернуться в меню")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True)

