# 34. Take a string, use a dictionary to find the first character that occurs more than once.

def first_repeating_char(s):
    seen = {}
    for ch in s:
        if ch in seen:
            return ch
        seen[ch] = True
    return None

test_strings = ["abcdefa", "python", "interview", "mississippi"]

for s in test_strings:
    ch = first_repeating_char(s)
    if ch:
        print(f"String '{s}' -> First repeating character: '{ch}'")
    else:
        print(f"String '{s}' -> All characters are unique.")
