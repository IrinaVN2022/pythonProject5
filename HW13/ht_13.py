import time
from pprint import pprint
import requests
import datetime

exchange_rate = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
response = requests.get(exchange_rate)
response_json = response.json()
#pprint(response_json)

try:
    result = requests.request(method='GET', url=exchange_rate)
except:
    result = None
print(result.status_code)
print(result.headers['Content-Type'])
print(result.content)

try:
    response_json = result.json()
except:
    response_json = None

time_now = datetime.datetime.now(tz=None)
print('"'+time.strftime('%y.%m.%d')+'"', sep='')
count = 1
for currency_name in response_json:
    print(f"{count }. {currency_name['txt']} to UA: {currency_name['rate']}")
    count += 1
