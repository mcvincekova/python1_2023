import json


file_name = 'absolventi.json'

with open(file_name) as f:
    data = f.read()

seznam_slovniku = json.loads(data)
print(seznam_slovniku[0]['jmeno'])