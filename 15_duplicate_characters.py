s = input("Enter a string: ")

seen = {}
for ch in s:
    seen[ch] = seen.get(ch, 0) + 1

duplicates = []
for ch, cnt in seen.items():
    if cnt > 1:
        duplicates.append(ch)

print("Duplicate characters:", duplicates)
