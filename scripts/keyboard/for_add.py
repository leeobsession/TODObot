from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


def start_bot() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Добавить свою задачу. \U0000270D")
    kb.button(text="Добавить рандомную задачу \U0001F939")
    kb.button(text="Просмотр задач \U0001F440")
    kb.button(text="Посмотреть гороскоп на сегодня \U00002721")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True, one_time_keyboard=True)


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

def get_zodiac_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Овен', callback_data='aries')
    keyboard_builder.button(text='Телец', callback_data='taurus')
    keyboard_builder.button(text='Близнецы', callback_data='gemini')
    keyboard_builder.button(text='Рак', callback_data='cancer')
    keyboard_builder.button(text='Лев', callback_data='leo')
    keyboard_builder.button(text='Дева', callback_data='virgo')
    keyboard_builder.button(text='Весы', callback_data='libra')
    keyboard_builder.button(text='Скорпион', callback_data='scorpio')
    keyboard_builder.button(text='Стрелец', callback_data='sagittarius')
    keyboard_builder.button(text='Козерог', callback_data='capricorn')
    keyboard_builder.button(text='Водолей', callback_data='aquarius')
    keyboard_builder.button(text='Рыбы', callback_data='pisces')
    keyboard_builder.adjust(3)
    return keyboard_builder.as_markup()
    