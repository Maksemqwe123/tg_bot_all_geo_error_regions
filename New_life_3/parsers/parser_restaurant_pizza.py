from bs4 import BeautifulSoup
import requests

headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0'
}

pizza_urls = []
pizza_title = []
pizza_address = []
pizza_time_work = []


def restaurant():
    url = 'https://www.relax.by/cat/ent/restorans/gomel/'

    response = requests.get(url=url, headers=headers)

    pages_info = BeautifulSoup(response.text, 'html.parser')

    restaurant_pizza = pages_info.find_all('div', class_='Place__headerContent')

    for pizza in restaurant_pizza:
        urls = pizza.find('div', class_='Place__titleWrapper').find('div', class_='Place__mainTitle').find('a').get('href')
        title = pizza.find('div', class_='Place__titleWrapper').find('div', class_='Place__mainTitle').find('a', title=True).text
        address = pizza.find('div', class_='Panel Place__content Place__content--address').find('div', class_='Place__content-inner').find('div', class_='Place__meta').find('span').text
        time_work = pizza.find('div', class_='Panel Place__content Place__content--address').find('div', class_='Place__content-inner').find('div', class_='Place__meta').find('span', class_='Place__time Place__contentSub Place__time--clickable Link').find('span').text

        pizza_urls.append(urls)
        pizza_title.append(title)
        pizza_address.append(address.strip())
        pizza_time_work.append(time_work.strip())

    return pizza_urls, pizza_title, pizza_address, pizza_time_work


restaurant()

all_pizza = list(zip(pizza_title, pizza_urls, pizza_address, pizza_time_work))
