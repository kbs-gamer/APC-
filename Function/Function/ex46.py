# Exercise 46: Sort a list of words according to their length using lambda

words = ["elephant", "cat", "hippopotamus", "dog", "tiger", "ox", "giraffe"]

# Sort by length using lambda key
sorted_words = sorted(words, key=lambda w: len(w))

print("Original words:", words)
print("Sorted by length (ascending):", sorted_words)
