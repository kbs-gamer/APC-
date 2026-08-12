s = input("Enter a string: ")

result = ""
count = 1
prev = s[0]

for ch in s[1:]:
    if ch == prev:
        count += 1
    else:
        result += prev + str(count)
        prev = ch
        count = 1

result += prev + str(count)
print("Encoded string:", result)
