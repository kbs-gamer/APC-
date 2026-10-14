email = input("Enter email address: ")

valid = True
if email.count("@") != 1:
    valid = False
else:
    local, domain = email.split("@")
    if local == "" or domain == "" or "." not in domain or domain.startswith(".") or domain.endswith("."):
        valid = False

if valid:
    print(email, "is a valid email")
else:
    print(email, "is not a valid email")
