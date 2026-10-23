# Program 19: Check whether input matches common Indian vehicle registration format (e.g., MH12AB1234)
import re

pattern = r"^[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}$"

vehicles = ["MH12AB1234", "DL01A9999", "KA05MB123", "MH141234", "GJ01XY5678"]

for plate in vehicles:
    if re.match(pattern, plate):
        print(f"'{plate}' -> Valid Indian vehicle number")
    else:
        print(f"'{plate}' -> Invalid vehicle number format")
