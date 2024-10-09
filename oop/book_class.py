# Python script named book_class.py. In this script, define a Book class that uses specific magic methods to enhance its functionality. This class will model a book with attributes for the title, author, and publication year.

class Book:
    def __init__(self, title, author, year):
        self.title = str(title)
        self.author = str(author)
        self.year = int(year)
        self.is_checked_out = False


    def __str__(self):
        return f"{self.title} by {self.author} published in {self.year}"
    

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
    

    def __del__(self):
        print("Deleting ", self.title)




from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(my_book)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(my_book))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del my_book

if __name__ == "__main__":
    main()