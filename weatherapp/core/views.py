from django.shortcuts import render
import base64
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests

# Create your views here.

# def encode_keys(number):
#     api_key_string = number
#     api_key_string_bytes = api_key_string.encode("ascii")
#
#     api_key_base64_bytes = base64.b64encode(api_key_string_bytes)
#     api_key_base64_string = api_key_base64_bytes.decode("ascii")
#     #print(api_key_base64_string)
#     return api_key_base64_string




# def get_html_content(number):
#
#     USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
#     LANGUAGE = "en-US,en;q=0.5"
#     session = requests.Session()
#     session.headers['User-Agent'] = USER_AGENT
#     session.headers['Accept-Language'] = LANGUAGE
#     session.headers['Content-Language'] = LANGUAGE
#
#     api_key_string = number
#     api_key_string_bytes = api_key_string.encode("ascii")
#
#     api_key_base64_bytes = base64.b64encode(api_key_string_bytes)
#     number = api_key_base64_bytes.decode("ascii")
#
#     html_content = session.get(f'https://www.lbcexpress.com/track/{number}').text
#     return html_content








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
    print(content)
    return content

def home(request):

    if 'number' in request.GET:
        # Fetch weather data
        tracking = request.GET.get('number')
        data = crawl(tracking)

    return render(request, 'core/homes.html', {'status':data['status'], 'time':data['time']})









# def home(request):
#     tracking_data = None
#     if 'number' in request.GET:
#         number = request.GET.get('number')
#         api_key_string = str(number)
#         api_key_string_bytes = api_key_string.encode("ascii")
#
#         api_key_base64_bytes = base64.b64encode(api_key_string_bytes)
#         number = api_key_base64_bytes.decode("ascii")
#         url = f"https://www.lbcexpress.com/track/{number}"
#         page = requests.get(url)
#         soup = BeautifulSoup(page.content, 'html.parser')
#         tracking_data = dict()
#         tracking_data['status'] = soup.find('span', attrs={'class': 'status-tracking'})
#         tracking_data['datetime'] = soup.find('span', attrs={'class': 'date-track-a'})
#
#     return render(request, 'core/homes.html', {'tracking': tracking_data})






# def home(request):
#     number =
#     url = f"https://www.lbcexpress.com/track/{number}"
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     containers = soup.find('input', attrs={'id': 'inputTrackingSearchForm'})
#     print(containers)
#
#     return render(request, 'core/homes.html')
#
#
# def encode_keys(self):
#     api_key_string = number
#     api_key_string_bytes = api_key_string.encode("ascii")
#
#     api_key_base64_bytes = base64.b64encode(api_key_string_bytes)
#     api_key_base64_string = api_key_base64_bytes.decode("ascii")
#     # print(api_key_base64_string)
#     return api_key_base64_string