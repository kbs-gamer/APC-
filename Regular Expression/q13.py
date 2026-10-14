import re

text = "Exam dates are 15-10-2026 and 20-12-2026"

dates = re.findall(r"\b\d{2}-\d{2}-\d{4}\b", text)

print(dates)