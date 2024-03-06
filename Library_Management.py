from random import randint

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.ISBN = randint(100000, 999999)
        self.available = True
        self.borrower = None
    
    def show_info(self):
        print(f"Book Title: {self.title}")
        print(f"Book Author: {self.author}")
        print(f"Book ISBN: {self.ISBN}")

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                self.books.remove(book)
                print("Book removed successfully.")
                return
        print("Book not found.")
    
    def borrow_book(self, ISBN, borrower):
        for book in self.books:
            if book.ISBN == ISBN and book.available:
                book.available = False
                book.borrower = borrower
                print("Book borrowed successfully.")
                return
        print("Book is unavailable or not found.")
    
    def return_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN and not book.available:
                book.available = True
                book.borrower = None
                print("Book returned successfully.")
                return
        print("Book not found or already returned.")
    
    def list_books(self):
        print("Library Inventory:")
        for book in self.books:
            print(f"{book.title} by {book.author} ({book.ISBN}) - {'Available' if book.available else 'Borrowed by: ' + book.borrower}")

# Example usage:
library = Library()

book1 = Book("Python Programming", "by a to z")
book2 = Book("Data Structures", "Alice")

library.add_book(book1)
library.add_book(book2)

library.list_books()

library.borrow_book(book1.ISBN, "Prashant")

library.list_books()

library.return_book(book1.ISBN)

library.list_books()
