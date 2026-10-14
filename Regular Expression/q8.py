import re

text = "Ravi likes books and plays games"

words = re.findall(r"\b\w+s\b", text)

print(words)