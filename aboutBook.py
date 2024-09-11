from datetime import  date, timedelta

class Book:

    def __init__(self, name, author, year, isbn):
        self.__name = name
        self.__author = author
        self.__year = year
        self.__isbn = isbn

    def __str__(self):
        return 'Book({},{},{},{})'.format(self.__name, self.__author, self.__year, self.__isbn)
    

    def get_name(self):
        return self.__name
    
    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn
    
class IllustratedBook(Book):
    def __init__(self, name, author, year, isbn, illustrator, count_of_illustrations):
        self.__name = name
        self.__author = author
        self.__year = year
        self.__isbn = isbn
        self.__illustartor = illustrator
        self.__count_of_illustrations = count_of_illustrations
    
    def __str__(self):
        return 'IllustartedBook({},{},{},{},{},{})'.format(self.__name, self.__author, self.__year, self.__isbn, self.__illustartor, self.__count_of_illustrations)
    
    def get_name(self):
        return self.__name
    
    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn


class Reader:
    def __init__(self, name, phone_number, number_of_reader_ticket):
        self.__name = name
        self.__phone_number = phone_number
        self.__number_of_reader_ticket = number_of_reader_ticket

    def __str__(self):
        return "Reader({},{},{})".format(self.__name, self.__phone_number, self.__number_of_reader_ticket)

class Catalog:
    def __init__(self):
        self.__books = []
    
    def add_book(self, book):
        if isinstance(book, Book):
            self.__books.append(book)
    
    def remove_book(self, isbn):
        for book in self.__books:
            if book.get_isbn()==isbn:
                self.__books.remove(book)

    def find_book_by_name(self, name):
        found_books = [book for book in self.__books if book.get_name() == name]
        if found_books:
            return found_books
        return None
    
    def find_book_by_author(self, author):
        found_books = [book for book in self.__books if book.get_author() == author]
        if found_books:
            return found_books
        return None

class Borrowing:
    def __init__(self, reader, book):
        self.__reader = reader
        self.__book = book
        self.__date_of_take = date.today()
        self.__date_of_take_back = self.__date_of_take + timedelta(days=10)

    def __str__(self):
        return 'Borrowing({},{},{},{})'.format(self.__reader.__str__(), self.__book.__str__(), self.__date_of_take, self.__date_of_take_back)
    


book1 = IllustratedBook("Harry Potter", "Joan Roaling", 1997, 1234567890987, "Jim Key", 25)
book2 = Book("Kobzar", "Taras Shevchenko", 1840, 1657483910473)
    
reader1 = Reader("Grisha", "+380676688996", 1)
reader2 = Reader("Dmytro", "+380123456789", 2)

catalog = Catalog()

catalog.add_book(book1)
catalog.add_book(book2)

print([print(book.__str__()) for book in catalog.find_book_by_author("Joan Roaling")])
catalog.remove_book(1234567890987)
print(catalog.find_book_by_name("Harry Potter"))

borowing1 = Borrowing(reader1, book1)
print(borowing1.__str__())
