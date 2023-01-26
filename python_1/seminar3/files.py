file_name = "mereni.txt"

with open(file_name, encoding='utf-8') as file:
    lines = file.readlines()

lines_tab_split = [line.split("\t") for line in lines]
lines_parsed = [[line[0], float(line[1])] for line in lines_tab_split]
print(lines_parsed)
