# Program 18: Extract six-digit Indian PIN codes from a paragraph
import re

text = "Delivery addresses include Mumbai 400001, Pune 411001, Nagpur 440010, and invalid codes like 012345 or 12345."

# Indian PIN codes: 6 digits starting with non-zero (1-9)
pincodes = re.findall(r"\b[1-9][0-9]{5}\b", text)

print("Text:", text)
print("Extracted Indian PIN codes:", pincodes)
