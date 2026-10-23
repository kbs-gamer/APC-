# Exercise 45: Use filter() and lambda to find words having more than five characters

words = ["Python", "C", "Java", "Programming", "Data", "Science", "Algorithm", "Web"]

long_words = list(filter(lambda w: len(w) > 5, words))

print("Original word list:", words)
print("Words with more than 5 characters:", long_words)
