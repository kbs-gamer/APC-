# 6. Create a dictionary of employee IDs and names. Ask the user for an employee ID and check whether it exists.

employees = {
    "E101": "Rajesh Kumar",
    "E102": "Sunita Verma",
    "E103": "Anil Deshmukh",
    "E104": "Meera Iyer"
}

emp_id = input("Enter Employee ID to check (default 'E102'): ").strip() or "E102"

if emp_id in employees:
    print(f"Employee ID {emp_id} exists! Name: {employees[emp_id]}")
else:
    print(f"Employee ID {emp_id} does not exist.")
