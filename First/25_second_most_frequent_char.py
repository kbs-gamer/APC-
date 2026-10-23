s = input("Enter a string: ")

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

if len(sorted_items) >= 2:
    print("Second most frequent character:", sorted_items[1][0])
else:
    print("Not enough distinct characters")
