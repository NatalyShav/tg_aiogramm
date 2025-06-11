import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from tg_aiogramm.config import TOKEN
import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

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

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help")

@dp.message(CommandStart)
async def start(massage:Message):
    await massage.answer('Приветики. Я бот!')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())