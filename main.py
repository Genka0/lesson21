from aiogram import Bot, Dispatcher, types, executor
from decouple import Config, Csv

config = Config()
config.read(".env")

bot = Bot(config("API_TOKEN"))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привіт, я бот, що зможе відповісти на кілька твоїх запитань!")

@dp.message_handler(commands=["help"])
async def command_help(message: types.Message):
    await message.answer("Напиши мені 2+2")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp)
