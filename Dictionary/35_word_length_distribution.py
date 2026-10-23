# 35. Accept a paragraph and create a dictionary where:
# Key = word length
# Value = number of words having that length.
import re

paragraph = input("Enter a paragraph (press enter for default): ").strip()
if not paragraph:
    paragraph = "Data science and artificial intelligence are transforming modern computing and machine learning systems worldwide."

words = re.findall(r"\b\w+\b", paragraph)

length_distribution = {}
for w in words:
    l = len(w)
    length_distribution[l] = length_distribution.get(l, 0) + 1

print("\nParagraph:", paragraph)
print(f"Total Words Extracted: {len(words)}")
print("\nWord Length Distribution:")
for length in sorted(length_distribution.keys()):
    print(f"  Length {length:2d}: {length_distribution[length]} word(s)")
