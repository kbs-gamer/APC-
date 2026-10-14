
import re

text = "Python is easy to learn"

words = re.findall(r"\b\w+\b", text)

print("Number of words:", len(words))