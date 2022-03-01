import logging
from aiogram import Bot, Dispatcher, executor, types
#from index import get_online, get_who
from bs4 import BeautifulSoup
import asyncio
import aiohttp

API_TOKEN = '5146056686:AAFsI3qbDMwGTSdckEiObbBhgIz2e0Npphg'
#5146056686:AAFsI3qbDMwGTSdckEiObbBhgIz2e0Npphg
#5280417676:AAEKx7yiw6L10Cv74qgRETk53Kpip9Vpg9E
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("WoWGaming botga hush kelibsiz!\nYordam uchun /help buyrug`ini kiritng.")

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("🟢 - /online buyrug`i serverda nechta online borligini ko`rsatadi.\n♻ - /who buyrug`i serverda kimlar borligini ko`rsatadi.")

"""
@dp.message_handler(commands=['top'])
async def top(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://wowgaming.uz') as response:
                text = await response.text(encoding="utf-8", errors="ignore")
                soup = BeautifulSoup(text, "html.parser")
                price = soup.find(class_="modal-dialog modal-lg").get_text()
                await message.answer(price)"""
                
@dp.message_handler(commands=['online'])
async def online_cmd(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://wowgaming.uz') as response:
            try:
                text = await response.text(encoding="utf-8", errors="ignore")
                soup = BeautifulSoup(text, "html.parser")
                price = soup.find(class_="col-lg-12 text-center").get_text()[45:][:19]
                ch = message.text.lower()
                a = f"♻ {price}"
                b = a.replace(")", "  ")
                if b:
                    await message.answer(b)
                else:
                    await message.answer("Hozir serverda hech kim yo`q!")
            except:
                await message.reply("server vaqtincha ishlamayapti...")



@dp.message_handler(commands=['who'])
@dp.message_handler(text_startswith="что там")
async def who_cmd(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://wowgaming.uz') as response:
            try:
                text = await response.text(encoding="utf-8", errors="ignore")
                soup = BeautifulSoup(text, "html.parser")
                price2 = soup.find(class_="table table-striped").get_text()[20:]   
                c = list(price2)
                d = "".join(c)
                e = d.replace("80", "\n")
                if e not in "веньВремя":
                    f = f"🟢 Hozir o`yinda: \n{e}"
                    await message.answer(f)
                else:
                    await message.answer("🔴 Hozir serverda hech kim yo`q!")
            except:
                await message.reply("server vaqtincha ishlamayapti...")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
