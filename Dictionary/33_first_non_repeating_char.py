# 33. Take a string, use a dictionary to find the first character that occurs only once.

def first_non_repeating_char(s):
    counts = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in s:
        if counts[ch] == 1:
            return ch
    return None

test_strings = ["swiss", "programming", "aabbcc", "teeter"]

for s in test_strings:
    ch = first_non_repeating_char(s)
    if ch:
        print(f"String '{s}' -> First non-repeating character: '{ch}'")
    else:
        print(f"String '{s}' -> No non-repeating character found.")
