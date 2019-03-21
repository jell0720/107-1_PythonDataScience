import requests
from bs4 import BeautifulSoup
result = requests.get('https://www.ptt.cc/bbs/Food/index.html')
soup = BeautifulSoup(result.text, 'lxml')

soup

selector = "div.title"

tags = soup.select(selector) # 取得一組 bs4.element.Tag 的 list

for tag in tags:
    print(type(tag))
    help(tag)
