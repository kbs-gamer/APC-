# Program 24: Validate product codes following the pattern ABC-1234-XY
# 3 uppercase letters, hyphen, 4 digits, hyphen, 2 uppercase letters
import re

pattern = r"^[A-Z]{3}-\d{4}-[A-Z]{2}$"

test_codes = ["ABC-1234-XY", "PRD-9876-AB", "abc-1234-xy", "AB-1234-XYZ", "XYZ-12A4-PQ", "MNO-0001-ZZ"]

print(f"Pattern required: ABC-1234-XY\n")
for code in test_codes:
    if re.match(pattern, code):
        print(f"'{code}' -> Valid product code")
    else:
        print(f"'{code}' -> Invalid product code")
