#Implement a Book class with public attributes title and author, and a private attribute _is_checked_out to track its availability.

class Book:
    def __init__(self, title, author, _is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    #method to check out book

    def book_check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"The book {self.title} has beeb checked out")
        else:
            print(f"The book {self.title} has already been checked out")


    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"The book {self.title} has been returned")
        else:
            print(f"The book {self.title} was not checked out")


    def is_available(self):
        return not self._is_checked_out



class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        print(f"The book '{book.title}' by '{book.author}' has been added")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    return
                else:
                    print(f"The book {title} is already checked out")
                    return
        print(f"The book {title} is not available in the library")
    
    def list_available_books(self):
        available_books = []
        for book in self._books:
            if book.is_available():
                available_books.append(book)
                print(f"{book.title} by {book.author}")
            else:
                print("No books available")