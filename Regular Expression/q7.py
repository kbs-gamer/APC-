import re

text = "Hello world, these are great books"

words = re.findall(r"\b[A-Za-z]{5}\b", text)

print(words)