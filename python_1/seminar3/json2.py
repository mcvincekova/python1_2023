import requests
import json


url = "https://svatky.adresa.info/json?date="
date = input("Zadaj datum vo formate DDMM: ")

url_with_date = url + date
print(f"Url: {url_with_date}")


response = requests.get(url_with_date)
data = json.loads(response.text)

# [{'date': '0307', 'name': 'Radomír'}]
name = data[0]['name']

print(f"Meno: {name}")