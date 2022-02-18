import logging
from aiogram import Bot, Dispatcher, executor, types
#from index import get_online, get_who
from bs4 import BeautifulSoup
import asyncio
import aiohttp

API_TOKEN = '5146056686:AAFsI3qbDMwGTSdckEiObbBhgIz2e0Npphg'
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#asyncio.run(main())
@dp.message_handler(commands=['online'])
async def online_cmd(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://wowgaming.uz') as response:
            text = await response.text(encoding="utf-8", errors="ignore")
            soup = BeautifulSoup(text, "html.parser")
            price = soup.find(class_="col-lg-12 text-center").get_text()[45:][:19]
            a = f"♻ {price}"
            b = a.replace(")", "  ")
            await message.answer(b)
#except:
        #await message.reply("server vaqtincha ishlamayapti...")


@dp.message_handler(commands=['who'])
async def who_cmd(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://wowgaming.uz') as response:
            text = await response.text(encoding="utf-8", errors="ignore")
            soup = BeautifulSoup(text, "html.parser")
            price2 = soup.find(class_="table table-striped").get_text()[20:]   
            c = list(price2)
            d = "".join(c)
            e = d.replace("80", "\n")
            f = f"🌐 Hozir o`yinda: \n{e}"
            await message.answer(f)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
