#Implement a Book class with public attributes title and author, and a private attribute _is_checked_out to track its availability.

class Book:
    def __init__(self, title, author, _is_checked_out):
        """ 
        Constructor for Book class. Sets title and author attributes from arguments, and sets _is_checked_out to False.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    #method to check out book

    def book_check_out(self):
        """
        Checks out a book if it is available.

        If the book has not been checked out, it will be marked as checked out and
        a message will be printed to the user.

        If the book has already been checked out, a message will be printed to the
        user indicating that the book has already been checked out.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"The book {self.title} has beeb checked out")
        else:
            print(f"The book {self.title} has already been checked out")


    def return_book(self):
        """
        Returns a book if it has been checked out.

        If the book has been checked out, it will be marked as returned and
        a message will be printed to the user.

        If the book has not been checked out, a message will be printed to the
        user indicating that the book was not checked out.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"The book {self.title} has been returned")
        else:
            print(f"The book {self.title} was not checked out")


    def is_available(self):
        """
        Returns True if the book is available to be checked out, False otherwise
        """
        return not self._is_checked_out



class Library:
    def __init__(self):
        """
        Initializes an empty library. The library is represented as a list of
        Book objects.
        """

        # Initialize an empty list of books
        self._books = []

    def add_book(self, book):
        """
        Adds a book to the library.

        The book is added to the internal list of books. A message is printed
        to the user indicating that the book has been added.

        Args:
            book (Book): The book to be added.
        """
        self._books.append(book)
        print(f"The book '{book.title}' by '{book.author}' has been added")

    def check_out_book(self, title):
        """
        Checks out a book with a given title from the library.

        The method iterates through the list of books in the library and checks
        if the book is available. If the book is available, it calls the
        Book.check_out() method to mark the book as checked out. If the book
        is already checked out, a message is printed to the user. If the book
        is not in the library, a message is printed to the user indicating that
        the book is not available.

        Args:
            title (str): The title of the book to be checked out.
        """
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
        """
        Lists all available books in the library.

        The method iterates through the list of books in the library and checks
        if the book is available. If the book is available, it is added to a list
        of available books and printed to the user with its title and author.
        If the book is not available, a message is printed to the user indicating
        that there are no books available.

        Returns:
            None
        """
        available_books = []
        for book in self._books:
            if book.is_available():
                available_books.append(book)
                print(f"{book.title} by {book.author}")
            else:
                print("No books available")