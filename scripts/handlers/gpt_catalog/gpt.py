import asyncio
import contextlib
import logging
import openai
import io

from aiogram import Router, F, Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove, Voice
from dotenv import get_variables
from handlers.gpt_catalog.dict_for_gpt import create_dict
from conf import config_bot
from handlers.start import StartForm
from pydub import AudioSegment
import speech_recognition as sr


router = Router()
#config = get_variables('/home/lee_obsession/TODObot/scripts/conf/.evn')
config = get_variables('/home/leeobsession/.poetry.venv/TODObot/scripts/conf/.evn')
openai_messages = create_dict()


def update(openai_messages, role, content):
    openai_messages.append({"role": role, "content": content})
    return openai_messages

def recognize_speech(audio):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio_data = recognizer.record(source)
    return recognizer.recognize_google(audio_data, language='ru-RU')


async def save_voice_as_mp3(bot: Bot, voice: Voice) -> str:
    """Скачивает голосовое сообщение и сохраняет в формате mp3."""
    voice_file_info = await bot.get_file(voice.file_id)
    voice_ogg = io.BytesIO()
    await bot.download_file(voice_file_info.file_path, voice_ogg)
    
    voice_mp3_path = f"voice_files/voice-{voice.file_unique_id}.wav"
    AudioSegment.from_file(voice_ogg, format="ogg").export(
        voice_mp3_path, format="wav"
    )
    return voice_mp3_path


@router.message(F.content_type == "voice")
async def handle_voice_message(message: Message, bot: Bot, state: FSMContext) -> None:
    voice_file = await save_voice_as_mp3(bot, message.voice)
    text = recognize_speech(voice_file)
    update(openai_messages, "user", text)
    msg_for_user = await conf_openai(msg_for_openai=text)
    await message.answer(text=msg_for_user)


@router.message(F.text)
async def get_chat_gpt(message: Message, state: FSMContext) -> None:
    user_text = message.text
    update(openai_messages, "user", user_text)
    msg_for_user = await conf_openai(msg_for_openai=user_text)
    await message.answer(text=msg_for_user)


async def conf_openai(msg_for_openai: str):
    openai.api_key = config["OPENAI_API_KEY"]
    model = 'gpt-3.5-turbo'
    response = openai.ChatCompletion.create(model=model, messages=openai_messages)
    return response.choices[0].message.content
