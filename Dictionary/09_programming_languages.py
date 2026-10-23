# 9. Create a dictionary of programming languages and their creators. Display each key and value using a loop.

languages = {
    "Python": "Guido van Rossum",
    "C": "Dennis Ritchie",
    "C++": "Bjarne Stroustrup",
    "Java": "James Gosling",
    "JavaScript": "Brendan Eich"
}

print("Programming Languages and Creators:")
for lang, creator in languages.items():
    print(f"  {lang} was created by {creator}")
