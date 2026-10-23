# Exercise 47: Sort students according to their marks using lambda

students = [
    ("Aarav", 85),
    ("Priya", 92),
    ("Rohan", 67),
    ("Sneha", 78),
    ("Vikram", 95)
]

# Sort by marks (second element of tuple) descending
sorted_by_marks_desc = sorted(students, key=lambda s: s[1], reverse=True)
sorted_by_marks_asc = sorted(students, key=lambda s: s[1])

print("Original student records:", students)
print("Sorted by marks (Highest to Lowest):", sorted_by_marks_desc)
print("Sorted by marks (Lowest to Highest):", sorted_by_marks_asc)
