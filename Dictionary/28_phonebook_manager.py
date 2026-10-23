# 28. Create a dictionary containing names and phone numbers.
# Implement:
# 1. Add contact
# 2. Search contact
# 3. Update contact
# 4. Delete contact
# 5. Display all contacts

phonebook = {
    "Aarav": "9876543210",
    "Diya": "9123456780",
    "Kabir": "9988776655"
}

def add_contact(name, phone):
    phonebook[name] = phone
    print(f"Added contact {name}: {phone}")

def search_contact(name):
    if name in phonebook:
        print(f"Found {name}: {phonebook[name]}")
    else:
        print(f"Contact '{name}' not found.")

def update_contact(name, new_phone):
    if name in phonebook:
        phonebook[name] = new_phone
        print(f"Updated contact {name}: {new_phone}")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print(f"Deleted contact {name}")
    else:
        print(f"Contact '{name}' not found.")

def display_all_contacts():
    print("\n--- Phonebook Directory ---")
    for name, phone in phonebook.items():
        print(f"  {name:<10}: {phone}")

print("Initial Phonebook:", phonebook)
add_contact("Meera", "9811223344")
search_contact("Diya")
update_contact("Aarav", "9899001122")
delete_contact("Kabir")
display_all_contacts()
