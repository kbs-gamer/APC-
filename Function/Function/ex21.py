def total_bill(price, quantity):
    total = price * quantity

    if total >= 1000:
        discount = total * 0.10
    else:
        discount = 0

    return total - discount


price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

print("Final Bill =", total_bill(price, quantity))