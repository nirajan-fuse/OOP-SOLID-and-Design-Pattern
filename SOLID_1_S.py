# [Single-Responsibility Principle (SRP)] Implement a simple program to interact with the library catalog system. Create a 
# Python class Book to represent a single book with attributes: Title, Author, ISBN, Genre, Availability (whether the book is 
# available for borrowing or not). Create another Python class LibraryCatalog to manage the collection of books with following 
# functionalities:
# Add books by storing each book objects (Hint: Create an empty list in constructor and store book objects)
# get book details and get all books from the list of objects

# Lets say, we need a book borrowing process (what books are borrowed and what books are available for borrowing). Implement 
# logics to integrate this requirement in the above system. Design the classes with a clear focus on adhering to the Single 
# Responsibility Principle(SRP) which represents that "A module should be responsible to one, and only one, actor."

class Book:
    def __init__(self, title, author, isbn, genre, availability=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.availability = availability

class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_all_books_detail(self):
        for book in self.books:
            print(f'Book_Name: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Genre: {book.genre}, Availability: {"Available" if book.availability==True else "Not Available"}')

    def single_book_detail(self, title):
        for book in self.books:
            if book.title == title:
                print(f'Book_Name: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Genre: {book.genre}, Availability: {"Available" if book.availability==True else "Not Available"}')
                break
            print('Book not found')

class BookBorrowing:
    def __init__(self, catalog):
        self.catalog = catalog
        self.borrowed_books = []

    def borrow_book(self, title):
        for book in self.catalog.books:
            if book.title == title and book.availability:
                book.availability = False
                self.borrowed_books.append(book)
                return f"{title} has been borrowed successfully."
        return "Book not available for borrowing."

    def return_book(self, title):
        for book in self.borrowed_books:
            if book.title == title:
                book.availability = True
                self.borrowed_books.remove(book)
                return f"{title} has been returned successfully."
        return "Book not found in borrowed list."
    

if __name__ == "__main__":
    book1 = Book("Harry Potter", "Ram", "1234567890", "Fantasy")
    book2 = Book("The Alchemist", "Shyam", "0987654321", "Mystery")
    book3 = Book("The Hobbit", "Hari", "9876543210", "Fantasy")

    catalog = LibraryCatalog()
    catalog.add_book(book1)
    catalog.add_book(book2)
    catalog.add_book(book3)

    catalog.get_all_books_detail()
    print()

    book_borrowing = BookBorrowing(catalog)
    print(book_borrowing.borrow_book("Harry Potter"))
    catalog.single_book_detail('Harry Potter')
    print()
    print(book_borrowing.return_book("Harry Potter"))
    catalog.single_book_detail('Harry Potter')

