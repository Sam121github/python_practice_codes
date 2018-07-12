import requests
from bs4 import BeautifulSoup

def info_pages(max_pages):
    page=2
    while page < max_pages:
        url = 'https://mrantifun.net/index.php?forums/trainers.2/page-' + str(page)
        source_code=requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'id': 'js-XFUniqueId'}):
            href = link.get('href')
            print(href)
        page += 1

info_pages(1)




