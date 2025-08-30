# Q) Your program will be used by the staff who work for an airline company, e.g. Qantas Airways. 
# The airline has a range of flights between various cities each day. Customers can book to fly on a 
# flight, and if circumstances change, they can cancel their booking at a later time, but not when it is 
# less than 2 hours until the flight. The client want you to make a program that can be used to store the 
# booking information, and the check-in information of the people on a flight.
# The program should allow staff to:
# 1. Create customer details – Name, Address, 3 digit passenger code that does not start with zeros 
# (e.g. 100 is the smallest acceptable value), whether the customer can only eat halal meat (e.g. Muslim 
# passengers)
# 2. Customers should be able to book seats on a flight, only one seat on a flight per customer. They may 
# however book a seat on a different flight.
# 3. Cancel a booking – only permitted 2 hours before the flight
# 4. Summary Information
# a. The source and destination places.
# b. The number of seats that are booked.
# c. The number of seats that are available.
# d. The number of passengers booked on the flight that need a halal meal.
# 5. Customer and flight information must persist
# Advanced Tasks
# 1. Create a new flight
# 2. Full validation of all input
# 3. Ask user to choose file name and path to save the file (Assumption is that the directory/folder 
# already exists)
# 4. Report on a customer’s booking

class Customer:
    def __init__(self, CustomerName, Address, PassengerCode, MealPreference):
        self.__CustomerName = CustomerName
        self.__Address = Address
        self.__PassengerCode = PassengerCode
        self.__MealPreference = MealPreference
        
    @property
    def CustomerName(self):
        return self.__CustomerName
    
    @CustomerName.setter
    def CustomerName(self, CustomerName):
        self.__CustomerName = CustomerName
        
    
    @property
    def Address(self):
        return self.__Address
    
    @Address.setter
    def Address(self, Address):
        self.__Address = Address
    
    
    @property
    def PassengerCode(self):
        return self.__PassengerCode
    
    @PassengerCode.setter
    def PassengerCode(self, PassengerCode):
        self.__PassengerCode = PassengerCode
        
    
    @property
    def MealPreference(self):
        return self.__MealPreference
    
    @MealPreference.setter
    def MealPreference(self, value):
        self.__MealPreference = value
        
    