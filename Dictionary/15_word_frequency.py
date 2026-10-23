# 15. Accept a sentence and create a dictionary containing each word and the number of times it occurs.

sentence = input("Enter a sentence (default 'data science is great and python data science is easy'): ").strip()
if not sentence:
    sentence = "data science is great and python data science is easy"

words = sentence.lower().split()
word_freq = {}
for w in words:
    word_freq[w] = word_freq.get(w, 0) + 1

print(f"Sentence: '{sentence}'")
print("Word Frequency Dictionary:")
for w, freq in word_freq.items():
    print(f"  '{w}': {freq}")
