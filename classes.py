# Q1 Base class

class Book:
    def __init__(self, title, author, isbn, num_pages, price):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.num_pages = num_pages
        self.price = price 

#  Q2 Derieved class
        
        class ReferenceBook(Book):
         def _init_(self, title, author, isbn, num_pages, price, reference_type):
        # Call the constructor of the base class (Book)
          super()._init_(title, author, isbn, num_pages, price)
        
        # Add the additional attribute specific to ReferenceBook
        self.reference_type = reference_type

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Number of Pages: {self.num_pages}")
        print(f"Price: ${self.price}")
        print(f"Reference Type: {self.reference_type}")
        print("\n")

    # Q3 Derieved class 

        class FictionBook(Book):
         def _init_(self, title, author, isbn, num_pages, price, genre):
          super()._init_(title, author, isbn, num_pages, price)
        self.genre = genre

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Number of Pages: {self.num_pages}")
        print(f"Price: ${self.price}")
        print(f"Genre: {self.genre}")
        print("\n")

 # Q5 Base class
        
        class Library:
         def _init_(self):
        # Initialize an empty dictionary to store books
          self._books = {}

    def add_book(self, book):
        # Add a book to the library dictionary with its title as the key
        self._books[book._title] = book
        print(f"Book '{book._title}' added to the library.")

    def display_all_books(self):
        if not self._books:
            print("The library is empty.")
        else:
            print("Details of all books in the library:")
            for book_title, book in self._books.items():
                book.display_details()

    def search_book_by_title(self, title):
        # Search for a book by title in the library
        if title in self._books:
            print(f"Book '{title}' found in the library.")
            self._books[title].display_details()
        else:
            print(f"Book '{title}' not found in the library.")

    def remove_book(self, title):
        # Remove a book from the library by its title
        if title in self._books:
            del self._books[title]
            print(f"Book '{title}' removed from the library.")
        else:
            print(f"Book '{title}' not found in the library.")


# Q6 Creating instances/ Testing implementaion
            
 # Testing the implementation
reference_book = ReferenceBook("The Notebook", "Various",  2192, 149.99, "Dictionary")
fiction_book = FictionBook("Mr.Chips", "James Hilton",  454, 12.99, "Mystery")

# Creating an instance of the Library
library = Library()

library.add_book(reference_book)
library.add_book(fiction_book)

library.display_all_books()

library.search_book_by_title("The Notebook")

library.remove_book("Mr.Chips")

library.display_all_books()





