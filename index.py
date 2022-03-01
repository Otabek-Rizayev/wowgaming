import aiohttp
import asyncio
from bs4 import BeautifulSoup
"""
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://wowgaming.uz') as response:
            text = await response.text(encoding="utf-8", errors="ignore")
            soup = BeautifulSoup(text, "html.parser")
            price = soup.find(id="modal-id2").get_text()[52:][:129]
            a = list(price)
            a[13] = " "
            b = "".join(a)
            c = b.replace("80", "\n")
            
            
            #d = c.replace("2", " ")[5:]
            
            print(c)
#
asyncio.run(main())"""
