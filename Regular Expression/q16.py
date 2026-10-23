# Program 16: Check whether password contains at least 8 characters, one uppercase, one lowercase, one digit, and one special character
import re

def validate_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$"
    if re.match(pattern, password):
        return True
    return False

passwords = ["Pass123", "Password@123", "weakpass", "Admin#2026", "NoSpecial123"]

for pwd in passwords:
    result = "Valid" if validate_password(pwd) else "Invalid"
    print(f"Password '{pwd}' -> {result}")
