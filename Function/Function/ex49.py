# Exercise 49: Process student records using functions and lambda expressions
# 1. Calculate average marks
# 2. Filter students scoring above 75
# 3. Sort students according to marks

students = [
    {"name": "Amit", "marks": 82},
    {"name": "Bhavna", "marks": 68},
    {"name": "Chetan", "marks": 91},
    {"name": "Divya", "marks": 74},
    {"name": "Eshwar", "marks": 88}
]

# 1. Calculate average marks
total_marks = sum(map(lambda s: s["marks"], students))
avg_marks = total_marks / len(students)

# 2. Filter students scoring above 75
above_75 = list(filter(lambda s: s["marks"] > 75, students))

# 3. Sort students according to marks (descending)
sorted_students = sorted(students, key=lambda s: s["marks"], reverse=True)

print("--- All Students ---")
for s in students:
    print(f"  {s['name']}: {s['marks']}")

print(f"\nAverage Marks of Students: {avg_marks:.2f}")

print("\n--- Students Scoring Above 75 ---")
for s in above_75:
    print(f"  {s['name']}: {s['marks']}")

print("\n--- Students Sorted by Marks (Highest to Lowest) ---")
for s in sorted_students:
    print(f"  {s['name']}: {s['marks']}")
