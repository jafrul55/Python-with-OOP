import re
from wsgiref.util import is_hop_by_hop
import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/IPhone'
text = requests.get(url).text.encode('utf-8').decode('ascii','ignore')
# print(text)
soup = BeautifulSoup(text,'lxml')
table = soup.find('table',class_='wikitable')
# table = soup.find_all('table')[1]
# print(table)

iphone_price_dict = {}
rows = table.find_all('tr')
# print(rows)
for row in rows:
    data = row.find_all(['th','td'])
    # print(data)
    try:
        version_text = data[0].a.text.split(' ')[1]
        version = re.sub(r"\D","",version_text)
        # print(version)
        price_text = data[-1].text.split('/')[-1]
        price = re.sub(r"\D","",price_text)
        price = int(price)
        if version and price > 100:
        # print(version,price)
            iphone_price_dict[version] = price

    except:
        pass

print(iphone_price_dict)