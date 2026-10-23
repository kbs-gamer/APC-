# Exercise 51: Product records processing using lambda expressions
# 1. Calculate total value of each product (Price * Quantity)
# 2. Filter products costing more than Rs. 1,000
# 3. Sort products according to total value

products = [
    {"name": "Mouse", "price": 450, "quantity": 10},
    {"name": "Keyboard", "price": 1200, "quantity": 5},
    {"name": "Monitor", "price": 8500, "quantity": 2},
    {"name": "USB Cable", "price": 250, "quantity": 20},
    {"name": "Headphones", "price": 1800, "quantity": 4}
]

# 1. Calculate total value of each product using map()
products_with_total = list(map(
    lambda p: {**p, "total_value": p["price"] * p["quantity"]},
    products
))

# 2. Filter products costing (price) more than Rs. 1,000
costly_products = list(filter(lambda p: p["price"] > 1000, products))

# 3. Sort products according to total value (descending)
sorted_by_total = sorted(products_with_total, key=lambda p: p["total_value"], reverse=True)

print("--- Products with Total Value (Price x Quantity) ---")
for p in products_with_total:
    print(f"  {p['name']}: Price = Rs. {p['price']}, Qty = {p['quantity']}, Total Value = Rs. {p['total_value']}")

print("\n--- Products Costing More than Rs. 1,000 ---")
for p in costly_products:
    print(f"  {p['name']}: Price = Rs. {p['price']}")

print("\n--- Products Sorted by Total Value (Highest to Lowest) ---")
for p in sorted_by_total:
    print(f"  {p['name']}: Total Value = Rs. {p['total_value']}")
