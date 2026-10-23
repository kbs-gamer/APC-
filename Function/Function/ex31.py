# Exercise 31: Check whether a string is a palindrome using recursion

def is_palindrome_recursive(s):
    # Base cases: empty or single char string is a palindrome
    if len(s) <= 1:
        return True
    # If first and last character don't match, not a palindrome
    if s[0].lower() != s[-1].lower():
        return False
    # Recursive call for substring excluding first and last characters
    return is_palindrome_recursive(s[1:-1])


text = input("Enter a string (press enter for default 'madam'): ").strip()
if not text:
    text = "madam"

if is_palindrome_recursive(text):
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")
