s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

a = sorted(s1.replace(" ", "").lower())
b = sorted(s2.replace(" ", "").lower())

if a == b:
    print(s1, "and", s2, "are anagrams")
else:
    print(s1, "and", s2, "are not anagrams")
