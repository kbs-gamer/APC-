def palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False


text = input("Enter a string or number: ")

if palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")