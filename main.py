from aiogram import Bot, Dispatcher, types, executor
import random

# Вставьте свой токен бота здесь
API_TOKEN = '6333977701:AAHiCobZTPKoqZ7XzfuZTFdPhFMFYUXxvyY'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Функция для получения случайного ответа из файла
def get_random_response(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        responses = file.read().splitlines()
    return random.choice(responses)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привіт, я бот, що відповість на кілька твоїх запитань!")

@dp.message_handler(commands=["help"])
async def command_help(message: types.Message):
    await message.answer("Напиши мені якийсь типовий запит, і я дам тобі відповідь!")

@dp.message_handler()
async def answer_question(message: types.Message):
    text = message.text.lower()

    if "привіт" in text:
        response = get_random_response('pryvit.txt')
    elif "як справи" in text:
        response = get_random_response('jak_sprawy.txt')
    # elif "какая погода" in text:
    #     response = get_random_response('kakaya_pogoda.txt')
    elif "як тебе звати?" in text:
        response = get_random_response('jak_tebe_zwaty.txt')
    # elif "сколько тебе дней" in text:
    #     response = get_random_response('skolko_tebya_dney.txt')
    # elif "который час" in text:
    #     response = get_random_response('kotoriy_chas.txt')
    elif "слава україні" in text:
        response = ('slava_ukraini')
    else:
        response = "Вибач, не розумію питання(."

    await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
