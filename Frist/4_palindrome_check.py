s = input("Enter a string: ")

reversed_str = s[::-1]

if s == reversed_str:
    print(s, "is a palindrome")
else:
    print(s, "is not a palindrome")
