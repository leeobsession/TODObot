from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def rand_s() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Рандомная дата! \U0001F3CB", callback_data="Рандомная дата! \U0001F3CB")
    kb.button(text="Вернуться в меню")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="dd.mm.YYYY")


def rand_h() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Рандомная дата! \U0001FAA0", callback_data="Рандомная дата! \U0001FAA0")
    kb.button(text="Вернуться в меню")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="dd.mm.YYYY")


def rand_hob() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Рандомная дата! \U0001F483", callback_data="Рандомная дата! \U0001F483")
    kb.button(text="Вернуться в меню")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="dd.mm.YYYY")


def rand_all() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Рандомная дата! \U00002620", callback_data="Рандомная дата! \U00002620")
    kb.button(text="Вернуться в меню")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="dd.mm.YYYY")