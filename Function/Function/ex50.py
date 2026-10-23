# Exercise 50: Employee records processing using filter(), map(), and sorted() with lambda
# 1. Find employees earning more than Rs. 50,000
# 2. Increase salaries by 10%
# 3. Sort employees according to salary

employees = [
    {"name": "Alice", "dept": "HR", "salary": 45000},
    {"name": "Bob", "dept": "IT", "salary": 62000},
    {"name": "Charlie", "dept": "Finance", "salary": 51000},
    {"name": "Diana", "dept": "IT", "salary": 75000},
    {"name": "Ethan", "dept": "Marketing", "salary": 48000}
]

# 1. Filter employees earning more than Rs. 50,000
high_earners = list(filter(lambda e: e["salary"] > 50000, employees))

# 2. Increase salaries by 10% using map()
updated_salaries = list(map(
    lambda e: {**e, "salary": round(e["salary"] * 1.10, 2)},
    employees
))

# 3. Sort employees according to salary (ascending)
sorted_employees = sorted(employees, key=lambda e: e["salary"])

print("--- Original Employees ---")
for e in employees:
    print(f"  {e['name']} ({e['dept']}): Rs. {e['salary']}")

print("\n--- Employees Earning More than Rs. 50,000 ---")
for e in high_earners:
    print(f"  {e['name']} ({e['dept']}): Rs. {e['salary']}")

print("\n--- Employees with 10% Salary Increment ---")
for e in updated_salaries:
    print(f"  {e['name']} ({e['dept']}): Rs. {e['salary']}")

print("\n--- Employees Sorted by Salary (Ascending) ---")
for e in sorted_employees:
    print(f"  {e['name']} ({e['dept']}): Rs. {e['salary']}")
