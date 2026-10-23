# 8. Create a dictionary and display: All keys, All values, All key-value pairs.

course_details = {
    "course_code": "CS501",
    "title": "Advanced Python Computing",
    "credits": 4,
    "instructor": "Dr. Sharma",
    "mode": "Offline"
}

print("1. All Keys:")
print("  ", list(course_details.keys()))

print()
print("2. All Values:")
print("  ", list(course_details.values()))

print()
print("3. All Key-Value Pairs:")
for k, v in course_details.items():
    print(f"   {k} -> {v}")
