from aiogram import Bot, Dispatcher, types, executor
import random
import datetime


API_TOKEN = '6333977701:AAHiCobZTPKoqZ7XzfuZTFdPhFMFYUXxvyY'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
# date_of_creation = 1694457657 #12.09.2023 у unix

def get_random_response(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        responses = file.read().splitlines()
    return random.choice(responses)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привіт, я бот, що відповість на кілька твоїх запитань!")

@dp.message_handler(commands=["help"])
async def command_help(message: types.Message):
    await message.answer("Ось що ти можешь мені написати: 'Привіт!', 'Як справи?', 'Яка погода?', 'Як тебе звати?', 'Котра година?', 'Скільки тобі днів?' та 'Слава Україні!'")

# @dp.message_handler()
# async def echo(message: types.Message):
#     print(message)


@dp.message_handler()
async def answer_question(message: types.Message):
    text = message.text.lower()

    if "привіт" in text:
        response = get_random_response('hello.txt')
    elif "як справи" in text:
        response = get_random_response('whatsup.txt')
    elif "яка погода?" in text:
        response = get_random_response('about_wether.txt')
    elif "як тебе звати?" in text:
        response = get_random_response('whats_your_name.txt')
    elif "скільки тобі днів" in text:
        response = get_random_response('how_old_r_u.txt')
    elif "слава україні" in text:
        response = ('slava_ukraini.txt')
    elif "котра година" in text:
        message_date = message.date
        # Перетворимо об'єкт datetime.datetime у строку з форматом, який ділить цю дату на рік-місяць-день і т.д
        formatted_date = message_date.strftime("%Y-%m-%d %H:%M:%S")#якщо цією строкою не вказати формат в якому я 
        #хочу бачити дату, то вийде наступне"(2023, 9, 10, 20, 45, 26))". дуже зрозуміло
        response = "Час відправки вашого повідомлення у системі Unix timestamp з урахуванням розташування серверу (Польща): " + formatted_date
        # current_time = get_current_time()
        # response = f"Поточний час: {current_time}"
    else:
        response = "Вибач, не розумію питання(."

    await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
