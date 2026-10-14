import re

text = "Hello     Python    World"

result = re.sub(r" +", " ", text)

print(result)