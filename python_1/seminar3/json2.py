import requests
import json


response = requests.get('https://svatky.adresa.info/json')
data = json.loads(response.text)
print(data)