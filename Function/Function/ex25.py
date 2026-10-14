books = {
    "Python": True,
    "Java": True,
    "C++": True
}


def display_books():
    for book, available in books.items():
        if available:
            print(book)


def issue_book(book):
    if book in books and books[book]:
        books[book] = False
        print("Book issued")
    else:
        print("Book not available")


def return_book(book):
    if book in books:
        books[book] = True
        print("Book returned")
    else:
        print("Book not found")


while True:
    print("\n1. Display Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        display_books()

    elif choice == 2:
        book = input("Enter book name: ")
        issue_book(book)

    elif choice == 3:
        book = input("Enter book name: ")
        return_book(book)

    elif choice == 4:
        break

    else:
        print("Invalid choice")