from aiogram import Bot, Dispatcher, executor, types

from decouple import config

bot = Bot(config('API_TOKEN'))
dp = Dispatcher(bot)
# @ - декоратор. фукция, которая содержит в себе нашу функцию
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привіт, я допоможу тобі порахувати А + Б")
