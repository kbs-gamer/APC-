import re

text = "Hello PYTHON World"

letters = re.findall(r"[A-Z]", text)

print(letters)