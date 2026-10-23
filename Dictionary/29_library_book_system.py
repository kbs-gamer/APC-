# 29. Create a dictionary containing book IDs and book names.
# Implement:
# 1. Add a book
# 2. Search a book
# 3. Remove a book
# 4. Display all books
# 5. Count total books

library_books = {
    101: "Introduction to Algorithms",
    102: "Python Crash Course",
    103: "Clean Code",
    104: "Design Patterns"
}

def add_book(book_id, title):
    library_books[book_id] = title
    print(f"Book added: [ID: {book_id}] '{title}'")

def search_book(book_id):
    if book_id in library_books:
        print(f"Found: [ID: {book_id}] '{library_books[book_id]}'")
    else:
        print(f"Book with ID {book_id} not found.")

def remove_book(book_id):
    if book_id in library_books:
        removed = library_books.pop(book_id)
        print(f"Removed: [ID: {book_id}] '{removed}'")
    else:
        print(f"Book with ID {book_id} not found.")

def display_all_books():
    print("\n--- Library Collection ---")
    for b_id, title in library_books.items():
        print(f"  ID {b_id}: {title}")

def count_books():
    print(f"Total Books in Library: {len(library_books)}")

print("Initial Library:", library_books)
add_book(105, "Artificial Intelligence: A Modern Approach")
search_book(102)
remove_book(103)
count_books()
display_all_books()
