# Some of the characteristics of a book are the title, author(s), publisher, ISBN, price, and year of 
# publication. Design a class bookType that defines the book as an class.  Each object of the class 
# bookType can hold the following information about a book: title, up to four authors, publisher, ISBN, 
# price, and number of copies in stock. To keep track of the number of authors, add another member variable.
# Include the member functions to perform the various operations on objects of type bookType. For example, 
# the usual operations that can be performed on the title are to show the title, set the title, and check 
# whether a title is the same as the actual title of the book. Similarly, the typical operations that can 
# be performed on the number of copies in stock are to show the number of copies in stock, set the number 
# of copies in stock, update the number of copies in stock, and return the number of copies in stock. Add 
# operations for the publisher, ISBN, book price, and authors. Add the appropriate constructors.
# Next you will design a class memberType. Each object of memberType can hold the name of a person, member 
# ID, number of books bought, and amount spent. Include the member functions to perform the various 
# operations on the objects of memberType—for example, modify, set, and show a person’s name. Similarly, 
# update, modify, and show the number of books bought and the amount spent. Add the appropriate 
# constructors. Write the definitions of the member functions of memberType. Write a program to test 
# various operations of your class memberType. Using the above classes, write a program to simulate a 
# bookstore. The bookstore has two types of customers: those who are members of the bookstore and those 
# who buy books from the bookstore only occasionally. Each member has to pay a $10 yearly membership fee 
# and receives a 5% discount on each book purchased. For each member, the bookstore keeps track of the 
# number of books purchased and the total amount spent. For every eleventh book that a member buys, the 
# bookstore takes the average of the total amount of the last 10 books purchased, applies this amount as 
# a discount, and then resets the total amount spent to 0.  Write a program that can process up to 1000 
# book titles and 500 members. Your program should contain a menu that gives the user different choices 
# to effectively run the program; in other words, your program should be user driven.

class BookType:
    def __init__(self, Title, Authors, Publisher, ISBNCode, Price, YearOfPublication, Stock):
        self.__Title = Title
        self.__Authors = Authors 
        self.__NumAuthors = len(Authors)
        self.__Publisher = Publisher
        self.__ISBNCode = ISBNCode
        self.__Price = Price
        self.__YearOfPublication = YearOfPublication
        self.__Stock = Stock
        
    @property
    def BookTitle(self):
        return self.__Title
    
    @BookTitle.setter
    def BookTitle(self, Title):
        self.__Title = Title
        
    
    @property
    def BookAuthors(self):
        return self.__Authors
    
    @BookAuthors.setter
    def BookAuthors(self, Authors):
        self.__Authors = Authors
        
        
    @property
    def BookPublisher(self):
        return self.__Publisher
    
    @BookPublisher.setter
    def BookPublisher(self, Publisher):
        self.__Publisher = Publisher
        
        
    @property
    def BookISBNCode(self):
        return self.__ISBNCode
    
    @BookISBNCode.setter
    def BookISBNCode(self, ISBNCode):
        self.__ISBNCode = ISBNCode
        
        
    @property
    def BookPrice(self):
        return self.__Price
    
    @BookPrice.setter
    def BookPrice(self, Price):
        self.__Price = Price
        

    @property
    def BookYearOfPublication(self):
        return self.__YearOfPublication
    
    @BookYearOfPublication.setter
    def BookYearOfPublication(self, YearOfPublication):
        self.__YearOfPublication = YearOfPublication
        
        
    @property
    def CopiesInStock(self):
        return self.__Stock
    
    @CopiesInStock.setter
    def CopiesInStock(self, Stock):
        self.__Stock = Stock