# 2. Create a dictionary containing employee information and display the value associated with a specified key.

employee = {
    "emp_id": "EMP204",
    "name": "Pooja Hegde",
    "designation": "Software Engineer",
    "department": "IT",
    "salary": 75000
}

key_to_search = input("Enter key to search (default 'name'): ").strip() or "name"

if key_to_search in employee:
    print(f"Value for '{key_to_search}': {employee[key_to_search]}")
else:
    print(f"Key '{key_to_search}' not found in employee details.")
