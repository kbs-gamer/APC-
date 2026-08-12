s = input("Enter a string: ")

freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

most_char = ""
most_count = 0
for ch, cnt in freq.items():
    if cnt > most_count:
        most_count = cnt
        most_char = ch

print("Most frequent character:", most_char, "(", most_count, "times )")
