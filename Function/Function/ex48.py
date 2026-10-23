# Exercise 48: Sort employee records according to salary using lambda

employees = [
    {"name": "Ananya", "salary": 65000},
    {"name": "Rajesh", "salary": 45000},
    {"name": "Kavita", "salary": 85000},
    {"name": "Deepak", "salary": 52000},
    {"name": "Sunil", "salary": 38000}
]

# Sort by salary ascending and descending
sorted_by_salary = sorted(employees, key=lambda e: e["salary"])
sorted_by_salary_desc = sorted(employees, key=lambda e: e["salary"], reverse=True)

print("Original Employee List:")
for emp in employees:
    print(f"  {emp['name']}: Rs. {emp['salary']}")

print("\nSorted by Salary (Ascending):")
for emp in sorted_by_salary:
    print(f"  {emp['name']}: Rs. {emp['salary']}")

print("\nSorted by Salary (Descending):")
for emp in sorted_by_salary_desc:
    print(f"  {emp['name']}: Rs. {emp['salary']}")
