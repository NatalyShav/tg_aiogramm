import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message,FSInputFile

from config import TOKEN
from config import API_KEY

import random
import aiohttp

from gtts import gTTS

# Вставьте сюда ваш API-ключ OpenWeatherMap
api_key = 'API_KEY'

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('weather'))
async def weather(message: Message):
    city = 'Moscow'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                data = await resp.json()
                temp = data['main']['temp']
                description = data['weather'][0]['description']
                reply = f"Погода в Москве:\nТемпература: {temp}°C\nОписание: {description.capitalize()}"
                await message.answer(reply)
            else:
                await message.answer("Не удалось получить информацию о погоде.")


@dp.message(Command('photo'))
async def photo(message: Message):
    photo_list = [
        "https://i.pinimg.com/originals/e4/21/50/e4215008df6962d94248502bed11a113.jpg",
        "https://ae01.alicdn.com/kf/H09e6e06905e043e89de4a6a14bbbfea8L/-.jpg"
    ]
    rand_photo = random.choice(photo_list)
    await message.answer_photo(photo=rand_photo, caption='Это супер крутая картинка')

@dp.message(F.text == "Что такое ИИ?")
async def aitext(message: Message):
    await message.answer("Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ")

@dp.message(F.photo)
async def handle_photo(message: Message):
    list_responses = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(list_responses)
    await message.answer(rand_answ)
    await bot.download(message.photo[-1],destination=f"img/{message.photo[-1].file_id}.jpg")

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help\n/photo\n/weather")

@dp.message(Command('start'))
async def start(message:Message):
    await message.answer(f'Приветики. {message.from_user.full_name}')

@dp.message()
async def echo(message: Message):
    # Просто отправляем то же сообщение обратно
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())