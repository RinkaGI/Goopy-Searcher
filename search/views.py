from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        url = 'https://www.ask.com/web?q='+search
        res = requests.get(url)
        soup = bs(res.text, 'lxml')
        result = soup.find_all('div', {'class': 'PartialSearchResults-item'})

        final_result = []

        for resultt in result:
            resultTitle = resultt.find(class_='PartialSearchResults-item-title').text
            resultUrl = resultt.find('a').get('href')
            resultDesc = resultt.find(class_='PartialSearchResults-item-abstract').text

            final_result.append((resultTitle, resultUrl, resultDesc))

        context = {
            'final_result': final_result
        }

        return render(request, 'search.html', context)

    else:
        return render(request, 'search.html')