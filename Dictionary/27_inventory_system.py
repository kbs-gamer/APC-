# 27. Create a dictionary containing product names and quantities.
# Perform:
# 1. Add a product
# 2. Update quantity
# 3. Delete a product
# 4. Search for a product
# 5. Display products with quantity below 10

inventory = {
    "Notebook": 50,
    "Pen": 8,
    "Pencil": 5,
    "Eraser": 15,
    "Marker": 4
}

def add_product(name, qty):
    inventory[name] = qty
    print(f"Added product '{name}' with quantity {qty}")

def update_quantity(name, qty):
    if name in inventory:
        inventory[name] = qty
        print(f"Updated '{name}' quantity to {qty}")
    else:
        print(f"Product '{name}' not found.")

def delete_product(name):
    if name in inventory:
        del inventory[name]
        print(f"Deleted product '{name}'")
    else:
        print(f"Product '{name}' not found.")

def search_product(name):
    if name in inventory:
        print(f"Found: {name} has quantity {inventory[name]}")
    else:
        print(f"Product '{name}' not found.")

def display_low_stock():
    print("\nProducts with quantity below 10 (Low Stock Alert):")
    for name, qty in inventory.items():
        if qty < 10:
            print(f"  {name}: {qty} units left")

print("Initial Inventory:", inventory)
add_product("Ruler", 12)
update_quantity("Pen", 15)
search_product("Marker")
display_low_stock()
delete_product("Eraser")
print("Final Inventory:", inventory)
