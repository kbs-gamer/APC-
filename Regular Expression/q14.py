import re

text = "Visit https://google.com and http://example.com"

urls = re.findall(r"https?://[^\s]+", text)

print(urls)