# 3. Create a dictionary of five products and their prices. Add a new product and price to the dictionary.

products = {
    "Laptop": 55000,
    "Smartphone": 25000,
    "Headphones": 2500,
    "Monitor": 12000,
    "Keyboard": 1500
}

print("Initial Products:", products)

# Add new product
new_product = "Mouse"
new_price = 800
products[new_product] = new_price

print(f"Added {new_product} priced at Rs. {new_price}")
print("Updated Products:", products)
