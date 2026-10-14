import re

text = "Hello@Python#123!"

result = re.sub(r"[^A-Za-z0-9 ]", "", text)

print(result)