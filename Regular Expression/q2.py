import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Karan"],
    "Department": ["CSE", "IT", "HR", "CSE", "IT"],
    "Salary": [45000, 60000, 55000, 75000, 50000],
    "Experience": [2, 5, 4, 7, 3]
}

df = pd.DataFrame(data)

print("Employees with salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nEmployee with highest experience:")
print(df.loc[df["Experience"].idxmax()])