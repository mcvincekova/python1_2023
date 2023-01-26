file_name = "sloh.txt"

with open(file_name, "r") as f:
    content = f.read()


content = content.replace("\n", " ")
words = content.split(" ")

print(words)