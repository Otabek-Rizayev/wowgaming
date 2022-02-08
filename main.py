import logging
from aiogram import Bot, Dispatcher, executor, types
from index import get_online
API_TOKEN = '5146056686:AAFsI3qbDMwGTSdckEiObbBhgIz2e0Npphg'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    
    await message.reply("WoWGaming botga hush kelibsiz.\nYordam uchun /help buyrug'ini kiriting!")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("Yordam!\n- /online buyrug'i orqali serverda qancha online borligini ko'rish mumkin.\n- /who buyrug'i orqali serverdagi barcha playerlar ro`yxatini ko'rish mumkin.")

@dp.message_handler(commands=['online'])
async def online(message: types.Message):
    await message.answer(get_online())

@dp.message_handler(commands=['who'])
async def who(message: types.Message):
    
    await message.reply("Bu kommanda hozircha ishlamaydi. Tez orada bartaraf etamiz!")


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.txt)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
