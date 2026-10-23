s = input("Enter a string: ")

seen = set()
result = ""
for ch in s:
    if ch not in seen:
        seen.add(ch)
        result += ch

print("After removing duplicates:", result)
