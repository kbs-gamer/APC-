import re

text = "Amit is an amazing and active student"

words = re.findall(r"\b[Aa]\w*", text)

print(words)