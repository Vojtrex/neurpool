from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import ScrapedData

# Create your views here.

import requests
from bs4 import BeautifulSoup

URL_SUTKA = 'https://www.sutka.eu/50m-plavecky-bazen'

page = requests.get(URL_SUTKA)
soup = BeautifulSoup(page.text, 'html.parser')

def scrape_url(request):

    numbers = [strong.get_text(strip=True) for strong in soup.select('div.header-info strong')]
    print(numbers)
    
    for entry in numbers:
        # Assuming a specific structure in the list elements
        percentage = numbers[1].rstrip('%')
        count_pool = numbers[2]
        count_aquapark = numbers[3]

        timestamp = datetime.now()

        ScrapedData.objects.create(percentage=percentage, count_pool=count_pool, count_aquapark=count_aquapark, timestamp=timestamp)

    return HttpResponse(numbers)
