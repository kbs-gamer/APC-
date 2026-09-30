"""Q2. Employees: salary > 50000, average, highest salary, highest experience"""
import pandas as pd

emp = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105],
    "Employee_Name": ["Anil", "Priya", "Suresh", "Neha", "Vikas"],
    "Department": ["IT", "HR", "IT", "Finance", "Sales"],
    "Salary": [60000, 45000, 75000, 52000, 40000],
    "Experience": [5, 3, 8, 6, 2],
})
print("Salary > 50,000:\n", emp[emp["Salary"] > 50000])
print("\nAverage salary :", emp["Salary"].mean())
print("Highest salary :", emp["Salary"].max())
print("\nEmployee with highest experience:\n", emp.loc[emp["Experience"].idxmax()])
