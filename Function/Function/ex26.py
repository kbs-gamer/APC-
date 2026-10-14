def calculate_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 500 + (units - 100) * 7
    else:
        bill = 1200 + (units - 200) * 10

    fixed_charge = 100
    tax = bill * 0.05

    final_bill = bill + fixed_charge + tax

    return final_bill


units = int(input("Enter units consumed: "))

print("Final Electricity Bill =", calculate_bill(units))