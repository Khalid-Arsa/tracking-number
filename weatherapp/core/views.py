from django.shortcuts import render
import base64
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests

def crawl(tracking):
    content = list()
    if tracking is not None:
        b64 = base64.b64encode(tracking.encode('ascii')).decode('ascii')
        response = requests.get(f"https://www.lbcexpress.com/track/{b64}").content
        soup = BeautifulSoup(response, "html.parser")
        status = [x.get_text() for x in soup.find_all(class_='status-tracking')]
        time = [z.get_text() for z in soup.find_all(class_='date-track-a')]
        content.append({'status': status, 'time': time})
    else:
        content.append({'status': "", 'time': ""})
    return content


def home(request):
    data = list({'status': 'Null', 'time': 'Null'})
    if 'number' in request.GET:
        # Fetch weather data
        tracking = request.GET.get('number')
        data = crawl(tracking)
    return render(request, 'core/homes.html', {'data': data[0]})
