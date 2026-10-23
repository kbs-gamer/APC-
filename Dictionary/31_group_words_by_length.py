# 31. Take a list of words, create a dictionary where the key is the word length
# and the value is a list of words having that length.

words = ["apple", "cat", "banana", "dog", "elephant", "fish", "pear", "ant", "kiwi"]

grouped_by_len = {}
for w in words:
    l = len(w)
    if l not in grouped_by_len:
        grouped_by_len[l] = []
    grouped_by_len[l].append(w)

print("Word List:", words)
print("\nDictionary Grouped by Word Length:")
for length in sorted(grouped_by_len.keys()):
    print(f"  Length {length}: {grouped_by_len[length]}")
