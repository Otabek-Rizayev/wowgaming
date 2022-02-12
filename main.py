import logging
from aiogram import Bot, Dispatcher, executor, types
from index import get_online
from index import get_who
API_TOKEN = '5280417676:AAEKx7yiw6L10Cv74qgRETk53Kpip9Vpg9E'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    
    await message.reply("WoWGaming botga hush kelibsiz.\nYordam uchun /help buyrug'ini kiriting!")

@dp.message_handler(commands=['help'])
async def help_cmd(message: types.Message):
    await message.reply("Yordam!\n- /online buyrug'i orqali serverda qancha online borligini ko'rish mumkin.\n- /who buyrug'i orqali serverdagi barcha playerlar ro`yxatini ko'rish mumkin.")

@dp.message_handler(commands=['online'])
async def online_cmd(message: types.Message):
    await message.answer(get_online())

@dp.message_handler(commands=['who'])
async def who_cmd(message: types.Message):
    await message.answer(get_who())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
