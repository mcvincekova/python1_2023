import requests
import json


response = requests.get('https://api.kodim.cz/python-data/people')
data = json.loads(response.text)


print(len(data))
print(data[0])

males = [person for person in data if person["gender"] == "Male"]
females = [person for person in data if person["gender"] == "Female"]

print(len(males))
print(len(females))