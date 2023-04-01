import requests
from bs4 import BeautifulSoup 

site_info = requests.get('https://www.amazon.in/Automate-Boring-Stuff-Python-2nd/dp/1593279922')

soup = BeautifulSoup(site_info.content, 'html.parser')

# print(soup)

part = soup.find(class_="a-size-medium a-color-price header-price a-text-normal")

# print(price)

print(part.get_text())