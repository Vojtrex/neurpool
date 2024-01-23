from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

import requests
from bs4 import BeautifulSoup

URL_SUTKA = 'https://www.sutka.eu/50m-plavecky-bazen'

page = requests.get(URL_SUTKA)
soup = BeautifulSoup(page.text, 'html.parser')

def scrape_url(request):

    numbers = [strong.get_text(strip=True) for strong in soup.select('div.header-info strong')]
    print(numbers)
    

    return HttpResponse(numbers)

# print(page.text)