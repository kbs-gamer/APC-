# Exercise 52: Process words using map(), filter(), and sorted() with lambda expressions
# 1. Find the length of every word
# 2. Extract words having more than five characters
# 3. Sort words according to their length

words = ["sun", "planet", "galaxy", "universe", "star", "comet", "nebula", "sky"]

# 1. Length of every word using map()
word_lengths = list(map(lambda w: (w, len(w)), words))

# 2. Extract words having more than 5 characters using filter()
words_gt_5 = list(filter(lambda w: len(w) > 5, words))

# 3. Sort words according to their length using sorted()
sorted_words = sorted(words, key=lambda w: len(w))

print("Original Words:", words)

print("\n1. Word Lengths:")
for word, length in word_lengths:
    print(f"   '{word}': {length}")

print("\n2. Words with more than 5 characters:")
print("  ", words_gt_5)

print("\n3. Words sorted by length:")
print("  ", sorted_words)
