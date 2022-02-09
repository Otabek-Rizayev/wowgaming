import requests
from bs4 import BeautifulSoup

def get_online():
    try:
        url = "http://wowgaming.uz/"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        price = soup.find(class_="col-lg-12 text-center").get_text()[45:][:19]
        a = f"♻ {price}"
        print(a.replace(")", " "))
    except:
        return "server vaqtincha ishlamayapti..."

print(get_online())
