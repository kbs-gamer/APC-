# 26. Create a dictionary containing employee names and salaries.
# Find:
# 1. Highest salary
# 2. Lowest salary
# 3. Average salary
# 4. Employees earning more than Rs. 50,000

employees = {
    "Amit": 45000,
    "Priya": 62000,
    "Rohan": 55000,
    "Sneha": 48000,
    "Vikram": 75000,
    "Kavita": 51000
}

highest_emp = max(employees, key=employees.get)
lowest_emp = min(employees, key=employees.get)
avg_salary = sum(employees.values()) / len(employees)
above_50k = {k: v for k, v in employees.items() if v > 50000}

print("Employee Salaries:", employees)
print(f"1. Highest Salary: {highest_emp} (Rs. {employees[highest_emp]})")
print(f"2. Lowest Salary: {lowest_emp} (Rs. {employees[lowest_emp]})")
print(f"3. Average Salary: Rs. {avg_salary:.2f}")
print("4. Employees Earning More than Rs. 50,000:")
for emp, sal in above_50k.items():
    print(f"   {emp}: Rs. {sal}")
