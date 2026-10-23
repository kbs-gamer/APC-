# Program 17: Identify consecutive repeated words in a sentence, ignoring case differences
import re

text = "This is is a test test sentence with with consecutive words. Go go forward!"

# Regex captures consecutive repeated words (case-insensitive)
matches = re.findall(r"\b(\w+)\s+\1\b", text, flags=re.IGNORECASE)

print("Original text:", text)
print("Consecutive repeated words found:", matches)
