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

import BookType
import MemberType
from tabulate import tabulate

def main():
    print()
    print("-------------------- Book Details --------------------")
    print()
    
    Books = []
    Members = []
    
    while True:
        print("1. ADD Books")
        print("2. UPDATE Books")
        print("3. VIEW a Book")
        print("4. VIEW all books")
        print("5. DELETE book")
        print("6. ADD Members")
        print("7. UPDATE Members")
        print("8. VIEW member By Id")
        print("9. VIEW all members")
        print("10. DELETE member")
        print("11. PURCHASE Book")
        print("12. EXIT")
        Choice = int(input("Enter your choice (1 to 12): "))
        print()
        if Choice == 1:
            while True:
                BookTitle = input("Enter book title: ")
                if BookTitle == "":
                    print("Book title cannot be empty!")
                else:
                    break
                
            BookAuthors = []
            while len(BookAuthors) < 4:
                Author = input("Enter book's author (press Enter to stop): ")
                if Author == "":
                    break
                BookAuthors.append(Author)
                
            while True:
                BookPublisher = input("Enter book's publisher: ")
                if BookPublisher == "":
                    print("Publisher cannot be empty!")
                else:
                    break
              
            while True:
                ISBNNumber = input("Enter book's ISBN number: ")
                if ISBNNumber == "":
                    print("ISBN number cannot be empty!")
                elif len(ISBNNumber) != 13:
                    print("ISBN number should be exactly 13 digits!")
                else:
                    ISBNNumber = int(ISBNNumber)
                    break
            
            while True:
                BookPrice = float(input("Enter book's price (in Rs): "))
                if str(BookPrice) == "":
                    print("Book price cannot be empty!")
                elif BookPrice < 0:
                    print("Book price cannot be negative!")
                else:
                    break
                
            while True:
                YearOfPublication = int(input("Enter year of publication: "))
                if str(YearOfPublication) == "":
                    print("Year of publication cannot be empty!")
                else:
                    break
                
            while True:
                Stock = int(input("Enter stock of your book: "))
                if str(Stock) == "":
                    print("Stock cannot be empty!")
                else:
                    break
                
            BookObj = BookType.BookType(BookTitle, BookAuthors, BookPublisher, ISBNNumber, BookPrice, YearOfPublication, Stock)
            Books.append(BookObj)
            print()
            print("Book", BookTitle, "added successfully!")
            print()
            
        elif Choice == 2:        
            BookTitle = input("Enter the book title you want to update (leave blank to keep current): ")
        
            Flag = False
        
            for Book in Books:
                if Book.BookTitle == BookTitle:
                    Index = Books.index(Book)
                    Flag = True
                    break
        
            if Flag == False:
                print("No such book exists!")
                print()
            else:
                while True:
                    Title = input("Enter book title: ")
                    if Title == "":
                        Title = Books[Index].BookTitle
                    break
        
                NewAuthors = []
                print("Enter authors (press Enter to stop, leave blank to keep current): ")
                for i in range(4):
                    Author = input("Enter book's author(s): ")
                    if Author == "":
                        break
                    NewAuthors.append(Author)
                if len(NewAuthors) == 0:
                    NewAuthors = Books[Index].BookAuthors
        
                while True:
                    Publisher = input("Enter publisher (leave blank to keep current): ")
                    if Publisher == "":
                        Publisher = Books[Index].BookPublisher
                    break
        
                while True:
                    ISBNCode = input("Enter ISBN (13 digits), (leave blank to keep current): ")
                    if ISBNCode == "":
                        ISBNCode = Books[Index].BookISBNCode
                    else:
                        if len(ISBNCode) != 13 or not ISBNCode.isdigit():
                            print("ISBN must be 13 digits!")
                            continue
                    break
        
                while True:
                    Price = input("Enter price (Rs), (leave blank to keep current): ")
                    if Price == "":
                        Price = Books[Index].BookPrice
                    else:
                        Price = float(Price)
                    break
        
                while True:
                    Year = input("Enter year of publication (leave blank to keep current): ")
                    if Year == "":
                        Year = Books[Index].BookYearOfPublication
                    else:
                        Year = int(Year)
                    break
        
                while True:
                    Stock = input("Enter stock (leave blank to keep current): ")
                    if Stock == "":
                        Stock = Books[Index].CopiesInStock
                    else:
                        Stock = int(Stock)
                    break
        
                UpdatedBook = BookType.BookType(Title, NewAuthors, Publisher, ISBNCode, Price, Year, Stock)
                Books[Index] = UpdatedBook
        
                print("Book updated successfully!")
                
        elif Choice == 3:      
            BookTitle = input("Enter the book's title you want to view: ")
        
            Flag = False
            for Book in Books:
                if Book.BookTitle == BookTitle:
                    Flag = True
                    print()
                    print("------------- Book Details -------------")
                    print()
                    print("Title: ", Book.BookTitle)
                    print("Authors: ", ", ".join(Book.BookAuthors))
                    print("Publisher: ", Book.BookPublisher)
                    print("ISBN Code: ", Book.BookISBNCode)
                    print("Price: Rs.", Book.BookPrice)
                    print("Year of Publication: ", Book.BookYearOfPublication)
                    print("Copies in Stock: ", Book.CopiesInStock)
                    print()
                    break
            
            if Flag == False:
                print("No such book exists!")
                print()
                    
        elif Choice == 4:
            if len(Books) == 0:
                print("No books available!")
            else:
                print()
                print("---------- All Books ----------")
                print()
        
                TableData = []
                for Book in Books:
                    TableData.append([
                        Book.BookTitle,
                        ", ".join(Book.BookAuthors),
                        Book.BookPublisher,
                        Book.BookISBNCode,
                        Book.BookPrice,
                        Book.BookYearOfPublication,
                        Book.CopiesInStock
                    ])
        
                print(tabulate(
                    TableData,
                    headers=["Title", "Authors", "Publisher", "ISBN", "Price (Rs)", "Year", "Stock"]
                ))
                
        elif Choice == 5:
            BookTitle = input("Enter the book's title you want to delete: ")
        
            Flag = False
            for i in range(len(Books)):
                if Books[i].BookTitle == BookTitle:
                    DeletedBook = Books.pop(i)
                    print("Book titled", DeletedBook.BookTitle, "has been deleted successfully!")
                    Flag = True
                    break
        
            if Flag == False:
                print("No book record with that title found!")
                
        elif Choice == 6:
            while True:
                MemberName = input("Enter member's name: ")
                if MemberName == "":
                    print("Member name cannot be empty!")
                else:
                    break
        
            while True:
                MemberID = input("Enter member's id: ")
                if MemberID == "":
                    print("Member ID cannot be blank!")
                else:
                    break
        
            while True:
                BooksBought = input("Enter number of books bought: ")
                if BooksBought == "":
                    print("Number of books bought cannot be empty!")
                elif int(BooksBought) < 0:
                    print("Number of books bought cannot be negative!")
                else:
                    BooksBought = int(BooksBought)
                    break
        
            while True:
                AmountSpent = input("Enter total amount spent: ")
                if AmountSpent == "":
                    print("Amount spent cannot be empty!")
                elif float(AmountSpent) < 0:
                    print("Amount spent cannot be negative!")
                else:
                    AmountSpent = float(AmountSpent)
                    break
    
            MemberObj = MemberType.MemberType(MemberName, MemberID, BooksBought, AmountSpent)
            Members.append(MemberObj)
        
            print("Member", MemberName, "added successfully!")

        elif Choice == 7:
            MemberID = input("Enter member id you want to update: ")
            Flag = False
            
            for Member in Members:
                if Member.MemberID == MemberID:
                    Index = Members.index(Member)
                    Flag = True
                    break
            
            if Flag == False:
                print("No member found with the given ID!")
            else:
                while True:
                    MemberName = input("Enter member name (leave blank to keep current): ")
                    if MemberName == "":
                        MemberName = Members[Index].MemberName
                    break
        
                while True:
                    BooksBought = input("Enter number of books bought (leave blank to keep current): ")
                    if BooksBought == "":
                        BooksBought = Members[Index].BooksBought
                    else:
                        BooksBought = int(BooksBought)
                    break
        
                while True:
                    AmountSpent = input("Enter amount spent (Rs) (leave blank to keep current): ")
                    if AmountSpent == "":
                        AmountSpent = Members[Index].AmountSpent
                    else:
                        AmountSpent = float(AmountSpent)
                    break
        
                Members[Index].MemberName = MemberName
                Members[Index].BooksBought = BooksBought
                Members[Index].AmountSpent = AmountSpent
        
                print("Member updated successfully!")
            
            
        elif Choice == 8:
            MemberID = input("Enter member id you want to view: ")
            Flag = False
            
            for Member in Members:
                if Member.MemberID == MemberID:
                    print("------------- Member Details -------------")
                    print("Member Name        :", Member.MemberName)
                    print("Member ID          :", Member.MemberID)
                    print("Books Bought       :", Member.BooksBought)
                    print("Amount Spent (Rs.) :", Member.AmountSpent)
                    Flag = True
                    break
            
            if Flag == False:
                print("No member found with the given ID!")
                
        elif Choice == 9:
            if len(Members) == 0:
                print("No members available!")
            else:
                print()
                print("---------- All Members ----------")
                print()
                from tabulate import tabulate
                
                MemberList = []
                for Member in Members:
                    MemberList.append([
                        Member.MemberID,
                        Member.MemberName,
                        Member.BooksBought,
                        Member.AmountSpent
                    ])
                
                print(tabulate(
                    MemberList,
                    headers=["Member ID", "Name", "Books Bought", "Amount Spent (Rs)"]
                ))

        elif Choice == 10:
            MemberID = input("Enter member ID you want to delete: ")
            
            Flag = False
            for i in range(len(Members)):
                if Members[i].MemberID == MemberID:
                    DeletedMember = Members.pop(i)
                    print("Member ID", DeletedMember.MemberID, "has been deleted successfully!")
                    Flag = True
                    break
        
            if Flag == False:
                print("No member record with the given ID found!")

        elif Choice == 11:
            MemberID = input("Enter member ID: ")
            BookTitle = input("Enter book title you want to purchase: ")
        
            BookFound = None
            for Book in Books:
                if Book.BookTitle == BookTitle:
                    BookFound = Book
                    break
        
            if BookFound is None:
                print("Book not found!")
            else:
                if BookFound.CopiesInStock <= 0:
                    print("Sorry, the book is out of stock!")
                else:
                    Quantity = int(input("Enter quantity to purchase: "))
        
                    if Quantity > BookFound.CopiesInStock:
                        print("Not enough stock available!")
                    else:
                        FinalPrice = BookFound.BookPrice * Quantity
        
                        if MemberID != "":
                            MemberFound = None
                            for Member in Members:
                                if Member.MemberID == MemberID:
                                    MemberFound = Member
                                    break
        
                            if MemberFound is None:
                                print("No such member exists! Proceeding as guest!")
                            else:
                                FinalPrice *= 0.95  
        
                                MemberFound.BooksBought += Quantity
                                MemberFound.AmountSpent += FinalPrice
        
                                if MemberFound.BooksBought % 11 == 0:
                                    AvgDiscount = MemberFound.AmountSpent / 10
                                    FinalPrice -= AvgDiscount
                                    MemberFound.AmountSpent = 0
                                    print("Special reward applied! Avg of last 10 purchases discounted.")
        
                        BookFound.CopiesInStock -= Quantity
        
                        print("Purchase successful!")
                        print("Book:", BookFound.BookTitle)
                        print("Quantity:", Quantity)
                        print("Final Price: Rs.", round(FinalPrice, 2))

        
        elif Choice == 12:
            print("Exiting application!")
            break
        
if __name__ == "__main__":
    main()