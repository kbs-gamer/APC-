import re

text = "Hello World\tPython\nProgramming"

characters = re.findall(r"[ \t\n]", text)

print(characters)
print("Total:", len(characters))