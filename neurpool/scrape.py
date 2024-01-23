import requests
from bs4 import BeautifulSoup

URL_SUTKA = 'https://www.sutka.eu/50m-plavecky-bazen'

page = requests.get(URL_SUTKA)
soup = BeautifulSoup(page.text, 'html.parser')


numbers = [strong.get_text(strip=True) for strong in soup.select('div.header-info strong')]
print(numbers)


f = open('output.html','w', encoding="utf-8")
f.write(page.text)

# print(page.text)