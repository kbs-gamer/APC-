# Program 23: Identify single-line comments in Python source code.
# Discuss why regular expressions alone may not correctly handle every string literal or multiline case.
import re

python_code = """
# This is a full-line comment
x = 10  # Inline comment
name = "# This is a string, not a comment!"
multiline_str = '''
# This is inside a multiline docstring
'''
print(x) # Final print
"""

# Regex to identify lines containing single line comments starting with '#'
# A basic pattern searches for '#' and matches to end of line:
comments = re.findall(r"#.*$", python_code, flags=re.MULTILINE)

print("Identified comment matches:")
for c in comments:
    print(" -", c)

print("\n--- Discussion: Limitations of Regular Expressions for Code Comments ---")
print("1. String Literals:")
print("   A simple regex like '#.*$' cannot reliably distinguish between a real comment")
print("   and a '#' character inside a string literal, e.g., url = 'http://example.com#section'")
print("   or text = '#not_a_comment'.")
print("2. Multiline Docstrings / Triple Quotes:")
print("   Hash symbols placed inside triple-quoted strings (''' or \"\"\") are string data,")
print("   not executable comments, but regex will mistakenly match them.")
print("3. Proper Solution:")
print("   Python's built-in 'tokenize' module or AST parser should be used for full syntax")
print("   analysis instead of pure regular expressions.")
