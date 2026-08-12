text = input("Enter text: ")
shift = int(input("Enter shift value (e.g. 3): "))
mode = input("Encrypt or Decrypt? (e/d): ").strip().lower()

if mode == "d":
    shift = -shift

result = ""
for ch in text:
    if ch.isupper():
        result += chr((ord(ch) - 65 + shift) % 26 + 65)
    elif ch.islower():
        result += chr((ord(ch) - 97 + shift) % 26 + 97)
    else:
        result += ch

print("Result:", result)
