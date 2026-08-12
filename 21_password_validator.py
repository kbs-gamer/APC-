password = input("Enter password: ")

has_upper = has_lower = has_digit = has_special = False
special_chars = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_chars:
        has_special = True

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Password is valid")
else:
    print("Password is invalid")
