# 14. Accept a string from the user and create a dictionary containing each character and its frequency.

text = input("Enter a string (default 'programming'): ").strip() or "programming"

char_freq = {}
for ch in text:
    char_freq[ch] = char_freq.get(ch, 0) + 1

print(f"Input String: '{text}'")
print("Character Frequency Dictionary:")
for ch, freq in char_freq.items():
    print(f"  '{ch}': {freq}")
