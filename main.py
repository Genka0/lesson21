from aiogram import Bot, Dispatcher, types, executor

from decouple import config

bot = Bot(config('API_TOKEN'))
dp = Dispatcher(bot)
# @ - декоратор. фукция, которая содержит в себе нашу функцию
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привіт, я бот, що зможе відповісти на кілька твоїх запитань!")
@dp.message_handler(commands = ["help"])
async def command_help(message: types.Message):
    await message.answer("Напиши мені 2+2")

@dp.message_handler()
async def echo(message: types.Message):
    # await message.answer(message.text)
    print(message)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)