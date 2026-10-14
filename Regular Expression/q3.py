import re

text = "Hello World"

vowels = re.findall(r"[aeiouAEIOU]", text)

print("Number of vowels:", len(vowels))