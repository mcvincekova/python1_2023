import json 

with open("absolventi.json") as f:
    data = f.read()

data_dict = json.loads(data)

print(type(data_dict[0]))