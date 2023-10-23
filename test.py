# text = "@Test"
# text = text.replace("@", "")
# text = text[::-1]

# print(text)
 
# word = "Anna"
# new_word = ""
# word = word.lower()
# for i in range(len(word)):

#     new_word += str(word[-(i+1)])

# print(new_word)
# print(word==new_word)

# while text.find("@")!= -1:
#     first_index = text.find("@")
#     last_index = text[first_index:].find(" ")
#     word = text[first_index:last_index+first_index]
#     text = text[first_index+1:]
#     print(word)


# words = text.split(" ")

# firstIndex = text.find("@")
# word = text[firstIndex:]

# lastIndex = word.find[" "]


# word = word[0:lastIndex]

# lowerWord = word.lower()
# capsWord = word.upper()
# firstBigWord = word.title()


# print(text[firstIndex:lastIndex])



# for word in words:
#     if word[0] == "@":
#         print (word)







# numbers = [1,5,7,8,9]

# def min(array):
#     min = 1000
#     for number in array:
#         if(min>number):
#             min = number
#     return min

# def max(array):
#     max = 0
#     for number in array:
#         if(max<number):
#             max = number
#     return max

# print(min(numbers))
# print(max(numbers))


# dicty = {"a": 1, 'b': 2, "c": 3}


# def inverse_dict(dicty):
#     new_dicty = {}
#     values = dicty.values()
#     keys = dicty.keys()
#     for key, value in zip(keys, values):
#         new_dicty[value] = key
#     return new_dicty

# print(inverse_dict(dicty))



# arr1 = [1,3,5,7,8,4,10]
# arr2 = [4,3,2,4,6,8,8]

# arr_sum = set(arr1 + arr2) 

# for number in set(arr1 + arr2):
#     if not number in arr2 or not number in arr1:
#         arr_sum.remove(number)

# print(arr_sum)


# tupletik = (1,10)

# def swap_tuple(tupletik):
#     return tuple(reversed(tupletik))

# print(swap_tuple(tupletik))



# array_of_tupletiks = [(1,5),(2,10),(1,15),(2,5)]

# def count_elements(array_of_tupletiks):
#     dict_of_tupletiks = {}
#     for tupletik in array_of_tupletiks:
#         if tupletik[0] in dict_of_tupletiks.keys():
#            dict_of_tupletiks[tupletik[0]] += tupletik[1]
#         else:
#             dict_of_tupletiks[tupletik[0]] = tupletik[1]

#     return dict_of_tupletiks

# print(count_elements(array_of_tupletiks)) 




# def max(array):
#     max = 0
#     for number in array:
#         if(max<number):
#             max = number
#     return max


# def max_number(*params):
#     return max(params)

# print(max_number(1,5,7,8,3,4))
# print(max_number(90,123,5,6,3123))



# def about_me(**info):

#     for key, value in info.items():
#         print(f"{key}: {value}")

# about_me(name = "Grisha", age = 14)
# print("\n")
# about_me(name = "Vova", age = 9, hobby = "Computer games")




# factorial = lambda num : 1 if(num==1) else num*factorial(num-1)
# square = lambda num: num**2


# def calculate(func, number):
#     print(func(number))



# calculate(factorial, 3)
# calculate(square, 3)

# import time

# def cache(func):
#     cache = {}

#     def wrapper(*args, **kwargs):
#         key = (args, tuple(kwargs.items()))
#         if key in cache:
#             return cache[key]
#         result = func(*args, **kwargs)
#         cache[key] = result
#         return result
    
#     return wrapper


# def time_decorator_factory(parameter):

#     def time_decorator(func):

#         def inner(*args, **kwargs):
#             begin = time.time()

#             func(*args, **kwargs)

#             end = time.time()

#             if parameter=="milisecond":
#                 print(f"This func takes :{(end - begin)*1000}")
#             else:
#                 print(f"This func takes :{end - begin}")

#         return inner
#     return time_decorator


# @time_decorator_factory("milisecond")
# @cache
# def calculate(func, number):
#     print(func(number))

# calculate(factorial, 10)











class Book:

    def __init__(self, name, author, year, isbn):
        self.__name = name
        self.__author = author
        self.__year = year
        self.__isbn = isbn

    def __str__(self):
        return 'Book({},{},{},{})'.format(self.__name, self.__author, self.__year, self.__isbn)
    
    def get_info(self):
        return {"name": self.__name,
                "author": self.__author,
                "year": self.__year,
                "ISBNumber": self.__isbn}


class Reader:
    def __init__(self, name, phone_number, number_of_reader_ticket):
        self.__name = name
        self.__phone_number = phone_number
        self.__number_of_reader_ticket = number_of_reader_ticket

    def __str__(self):
        return "Reader({},{},{})".format(self.__name, self.__phone_number, self.__number_of_reader_ticket)
    
    def get_info(self):
        return {"name": self.__name,
                "phone_number": self.__phone_number,
                "number_of_reader_ticket": self.__number_of_reader_ticket}

class Catalog:
    def __init__(self):
        self.__books = []
    
    def add_book(self, book):
        if isinstance(book, Book):
            self.__books.append(book)
    
    def remove_book(self, isbn):
        for book in self.__books:
            if book.get_info()["ISBNumber"]==isbn:
                self.__books.remove(book)

    def find_book_by_name(self, name):
        found_books = [book for book in self.__books if book.get_info()["name"] == name]
        if found_books:
            return found_books
        return None
    
    def find_book_by_author(self, author):
        found_books = [book for book in self.__books if book.get_info()["author"] == author]
        if found_books:
            return found_books
        return None

class Borrowing:
    def __init__(self):
        self.__reader