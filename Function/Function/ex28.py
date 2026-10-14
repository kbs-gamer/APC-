def invoice(price, quantity):
    subtotal = price * quantity

    discount = subtotal * 0.10
    amount = subtotal - discount

    gst = amount * 0.18
    final_amount = amount + gst

    return final_amount


price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

print("Final Invoice =", invoice(price, quantity))