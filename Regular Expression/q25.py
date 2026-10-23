# Program 25: Given a paragraph containing student names, roll numbers, and marks, extract each field using regular expressions
import re

paragraph = """
Academic Records:
Student Name: Aarav Sharma, Roll Number: 101, Marks: 88.5
Student Name: Priya Patel, Roll Number: 102, Marks: 92
Student Name: Rohan Verma, Roll Number: 103, Marks: 76.0
Student Name: Sneha Kulkarni, Roll Number: 104, Marks: 85
"""

# Extract records with regex named groups
pattern = r"Student Name:\s*(?P<name>[A-Za-z ]+?),\s*Roll Number:\s*(?P<roll>\d+),\s*Marks:\s*(?P<marks>\d+(?:\.\d+)?)"

matches = re.finditer(pattern, paragraph)

records = []
print(f"{'Roll':<8} {'Name':<20} {'Marks':<10}")
print("-" * 38)
for match in matches:
    name = match.group("name").strip()
    roll = match.group("roll").strip()
    marks = match.group("marks").strip()
    records.append({"Roll": roll, "Name": name, "Marks": float(marks)})
    print(f"{roll:<8} {name:<20} {marks:<10}")

print("\nExtracted structured list of dicts:")
print(records)
