import asyncio
import logging
import subprocess 
from aiogram import Bot, Dispatcher, types,F
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ContentType
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import random
import requests
import pyttsx3
import subprocess
logging.basicConfig(level=logging.INFO)
bot = Bot(token='7404224531:AAG6DIPxsYc6J06OsTO3ZUZBrp5EZgYcuHE')

dp = Dispatcher()


btn_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Хоррор')],
        [KeyboardButton(text='Экшен')],
        [KeyboardButton(text='Комедия')],
        [KeyboardButton(text='Фантастика')],
        [KeyboardButton(text='Детективы')]
    ],
    resize_keyboard=True
)

horror = ['https://www.kinopoisk.ru/film/1112132/', 'https://www.kinopoisk.ru/film/495892/', 'https://www.kinopoisk.ru/film/1200179/','https://www.kinopoisk.ru/film/494/','https://www.kinopoisk.ru/film/801/']
action = ['https://www.kinopoisk.ru/film/1009536/', 'https://www.kinopoisk.ru/series/1142153/', 'https://www.kinopoisk.ru/film/4850165/','https://www.kinopoisk.ru/film/740644/','https://www.kinopoisk.ru/film/463686/']
fantastic = ['https://www.kinopoisk.ru/film/463634/', 'https://www.kinopoisk.ru/film/444/', 'https://www.kinopoisk.ru/film/1008445/','https://www.kinopoisk.ru/film/4536580/','https://www.kinopoisk.ru/film/1322324/']
comedia = ['https://www.kinopoisk.ru/film/1355139/', 'https://www.kinopoisk.ru/series/5059049/', 'https://www.kinopoisk.ru/film/1345717/','https://www.kinopoisk.ru/film/46225/','https://www.kinopoisk.ru/film/842037/']
detectives = ['https://www.kinopoisk.ru/film/1188529/','https://www.kinopoisk.ru/series/1224067/','https://www.kinopoisk.ru/series/4443734/','https://www.kinopoisk.ru/series/4635111/','https://www.kinopoisk.ru/film/1368311/']


@dp.message(Command('films'))
async def smd_name(message: Message):
    await message.answer('Выберите жанр', reply_markup=btn_keyboard)

@dp.message(lambda message: message.text == 'Хоррор')
async def show_horror(message: Message):
    await message.reply('А вот и не плохой ужастик' + random.choice(horror))

@dp.message(lambda message: message.text == 'Экшен')
async def show_action(message: Message):
    await message.reply('А вот и не плохой экшен' + random.choice(action))

@dp.message(lambda message: message.text == 'Фантастика')
async def show_fantastic(message: Message):
    await message.reply('А вот и не плохой фантастик' + random.choice(fantastic))

@dp.message(lambda message: message.text == 'Комедия')
async def show_comedia(message: Message):
    await message.reply('А вот и не плохой Камеди ' + random.choice(comedia))

@dp.message(lambda message: message.text == 'Детективы')
async def show_detectives(message: Message):
    await message.reply('А вот и не плохой Детектив ' + random.choice(detectives))



@dp.message(Command('start'))
async def cmd_name(message: Message):
    await message.answer('Привет, я тестовый бот''\n Смотреть фильм - /films')

@dp.message(Command('info'))
async def cmd_name(message: Message):
    await message.reply('У меня есть такие команды -\n /start, \n /info, \n  /who, \n  /mobile_games, \n /computer_games')

@dp.message(Command('who'))
async def cmd_name(message: Message):
    await message.reply('Satylganov Nurkhan')

@dp.message(Command('mobile_games'))
async def cmd_name(message: Message):
    await message.reply('Скачать игры по этой ссылки: ')

@dp.message(Command('computer_games'))
async def cmd_name(message: Message):
    await message.reply('Скачать игры по этой ссылки: ')

@dp.message(Command('name'))
async def cmd_name(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) > 1:
      await message.answer(f'Привет, <b>{args[1]}</b>', parse_mode='HTML')  
    else:
      await message.answer('Пожалуйста, укажи свое имя после команды /name!')
    

@dp.message(Command('button'))
async def cmd_start(message: Message):
    kb = [
        [types.KeyboardButton(text='Игры')],
        [types.KeyboardButton(text='Фильмы')],
        [types.KeyboardButton(text='Тест')],
        [types.KeyboardButton(text='Функции')],
        [types.KeyboardButton(text='5')]


    ]
    Keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('Какую кнопку вы выбрали?', reply_markup=Keyboard  )

@dp.message(lambda message: message.text == 'Игры')
async def first_btn(message: Message):
    await message.reply('Запустить игру - /gamee')


@dp.message(lambda message: message.text == 'Фильмы')
async def second_btn(message: Message):
    await message.reply('Запустить фильмы - /films')

@dp.message(lambda message: message.text == 'Тест')
async def trird_btn(message: Message):
    await message.reply('Запустить тест - /test')

@dp.message(lambda message: message.text == 'Функции')
async def fourth_btn(message: Message):
    await message.reply('Все функции - /start, /info, /gamee, /mobile_game, /films, /test ')

@dp.message(lambda message: message.text == '5')
async def fifth_btn(message: Message):
    await message.reply(f'Вы нажали  кнопку 5  {message.from_user.first_name}')





@dp.message(Command('test'))
async def any_message(message: types.Message):
    await message.answer('Hello, <b>world</b>!', parse_mode='HTML')
    await message.answer('Hello, *world*/!', parse_mode='MarkdownV2')


# @dp.message()
# async def echo_message(message: types.Message):
#     await message.answer(f'Привет {message.from_user.first_name}, твой текст: \n{message.text}')


@dp.message(F.content_type == 'animation')
async def echo_gif(message: types.Message):
    await message.reply_animation(message.animation.file_id)


@dp.message(Command('special_buttons'))
async def cmd_special_buttons(message: types.Message):
    kb = [
        [types.KeyboardButton(text='Запросить контакт', request_contact=True)],
        [types.KeyboardButton(text='Запросить викторину', request_poll=types.KeyboardButtonPollType(type='quiz'))],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.reply('Выберите действие', reply_markup=keyboard)


@dp.message(lambda message: message.text == '/vk')
async def send_quiz(message: types.Message):
    question = 'Какой самый большой океан на Земле?'
    options = ['Атлантический', 'Индийский', 'Тихий', 'Северный Ледовитый',]
    correct_option_id = 2

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=options,
        type='quiz',
        correct_option_id=correct_option_id,
        is_anonymous=False
    )


engine = pyttsx3.init()

engine.setProperty('rare',150)
engine.setProperty('volume',0.5)


engine.say('Добро пожаловать как ваши дела')

engine.runAndWait()





@dp.message(Command('gamee'))
async def launch_game(message: Message):
    def run_game():
        try:
            subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
            return 'Игра запущена!'
        except FileNotFoundError:
            return 'Путь к игре не найден. Проверь путь в коде.'
        
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, run_game)

    await message.reply(response)
        











@dp.message(Command("name1"))
async def cmd_name(message: Message):  
    args = message.text.split(maxsplit=1)
    if len(args) > 1:
        await message.answer(f"Привет, <b>{args[1]}</b>", parse_mode="HTML") 
    else:
        await message.answer("Пожалуйста, укажи свое имя после команды /1name.")

















































async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
