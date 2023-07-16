import httpx
import lxml
from bs4 import BeautifulSoup
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Dispatcher, Router
import asyncio
from handlers.my_menu import Form
from keyboard.for_add import start_bot

router = Router()


headers = {
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}


async def get_response(link: str):
    async with httpx.AsyncClient(headers=headers, follow_redirects=True) as htx:
        result: httpx.Response = await htx.get(url=link)
        if result.status_code != 200:
            #TODO сделать смену прокси и юзерагента
            return await get_response(link=link)
        else:
            return await result.aread()


async def get_text_horoscope(zodiac: str):
    link = f'https://horo.mail.ru/prediction/{zodiac}/today/'
    response_result = await get_response(link=link)
    beautifulsoup: BeautifulSoup = BeautifulSoup(markup=response_result, features='lxml')
    text = beautifulsoup.find(name='div', class_='article__text')
    return text.text


@router.callback_query()
async def get_horoscope(call: CallbackQuery):
    await call.answer()
    zodiac = call.data
    text = await get_text_horoscope(zodiac=zodiac)
    await call.message.edit_text(text=text, show_alert=True)