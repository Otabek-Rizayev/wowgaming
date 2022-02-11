import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "http://wowgaming.uz/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

def get_online():
    try:
        price = soup.find(class_="col-lg-12 text-center").get_text()[45:][:19]
        a = f"♻ {price}"
        return a.replace(")", "  ")
    except:
        return "server vaqtincha ishlamayapti..."


def get_who():
    try:
        price2 = soup.find(class_="table table-striped").get_text()[20:]   
        a = list(price2)
        b = "".join(a)
        c = b.replace("80", "\n")
        return f"Hozir o`yinda: \n{c}"
    except:
        return "serverdan javob kelmadi..."

    
    

