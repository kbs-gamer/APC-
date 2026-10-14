import re

text = "My roll number is 123 and my age is 20"

digits = re.findall(r"\d", text)

print(digits)