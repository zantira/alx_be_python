 #Python scripts: library_system.py and main.py. In library_system.py, you’ll define a base class Book and two derived classes, EBook and PrintBook, showcasing inheritance. Additionally, implement a Library class demonstrating composition by managing a collection of books.

#Base class
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

#derive classes
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size
    

class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

#composing a class using Bool, Ebook and Printbook

class Library:
    def __init__(self):
        # if books is None:
        #     books = []
        self.books = []
    def __str__(self):
        return f"{self.books}"

    def add_book(self, book):
        return self.books.append(book)
    

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"Ebook - Title: {book.title}, by {book.author}, File Size: {book.file_size}MB")
            elif isinstance(book, PrintBook):
                print(f"Printbook - Title: {book.title}, by {book.author}, Page count: {book.page_count} pages")
            else:
                print(f"Book - Title: {book.title}, by {book.author}")