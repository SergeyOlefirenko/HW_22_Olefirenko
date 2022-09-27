import time
from threading import Thread
import requests
from lxml import html
from bs4 import BeautifulSoup

#Парсинг сайта
def carsdata():
    url = f'https://auto.ria.com/legkovie/?page='
    for i in range(1, 11):
        response = requests.get(url + str(i))
        index = 1
        if response.status_code == 200:
            tree = html.fromstring(response.text)
            names = []
            prices = []
            for idx in range(1, 11):
                nPath = f'//*[@id="searchResults"]/section[{index}]/div[4]/div[2]/div[1]/div/a/span/text()'
                xPath = f'//*[@id="searchResults"]/section[{index}]/div[4]/div[2]/div[2]/span/span[1]/text()'
                name = tree.xpath(nPath)
                price = tree.xpath(xPath)
                if (len(name) > 0):
                    names.append(name[0])
                    prices.append(price[0])
                else:
                    print(name, price)
                index += 1
            for idx in range(len(prices)):
                print(f'{str(idx + 1)}: {names[idx]}, price:{prices[idx]}$')
start = time.perf_counter()
for i in range(1):
    th = Thread(target=carsdata, args=())
    th.start()
    end = time.perf_counter()
    print(f'time with threads = {end - start:0.2f}')
    print(f'working time = {end - start}')


#Пример без использования функции и потоков

# url = f'https://auto.ria.com/legkovie/?page='
# for i in range(1, 11):
#     response = requests.get(url+str(i))
#     index = 1
#     if response.status_code == 200:
#         tree = html.fromstring(response.text)
#         names = []
#         prices = []
#         for idx in range(1, 11):
#             nPath = f'//*[@id="searchResults"]/section[{index}]/div[4]/div[2]/div[1]/div/a/span/text()'
#             xPath = f'//*[@id="searchResults"]/section[{index}]/div[4]/div[2]/div[2]/span/span[1]/text()'
#             name = tree.xpath(nPath)
#             price = tree.xpath(xPath)
#             if (len(name) > 0):
#                 names.append(name[0])
#                 prices.append(price[0])
#             else:
#                 print(name, price)
#             index += 1
#         for idx in range(len(prices)):
#             print(f'{str(idx + 1)}: {names[idx]}, price:{prices[idx]}$')

#Пример с использованием BeautifulSoup
# def get_carname():
#         receive = requests.get('https://auto.ria.com/legkovie/?page=1')
#         page = BeautifulSoup(receive.text, "html.parser")
#         findC = page.find_all('span', class_="blue bold")
#         carnames = []
#         count = 0
#         for text in findC:
#                 count+=1
#                 carnames.append(f'{count}: {(text.getText().strip())}')
#         return carnames
#
# def get_carprice():
#         receive = requests.get('https://auto.ria.com/legkovie/?page=1')
#         page = BeautifulSoup(receive.text, "html.parser")
#         findP = page.find_all('span', class_="size15")
#         carprice = []
#         for text in findP:
#             carprice.append(f'price: {(text.getText().strip())}')
#         return carprice
#
#
# carnames = get_carname()
# carprices = get_carprice()
# for idx in range(len(get_carname())):
#     print(carnames[idx] , '-' ,carprices[idx])








