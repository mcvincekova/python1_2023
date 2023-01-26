import requests
import json


response = requests.get('https://api.kodim.cz/python-data/people')
data = json.loads(response.text)

number_of_people = len(data)
print(f"V zozname je {number_of_people} ludi.")

print(data[0])

women_count = 0
male_count = 0
for item in data:
    if item['gender'] == "Female":
        women_count += 1
    else:
        male_count += 1

print(f"V zozname je {women_count} zien.")
print(f"V zozname je {male_count} muzov.")

women = [item for item in data if item['gender'] == "Female"]
women_count_2 = len(women)

print(women_count_2)