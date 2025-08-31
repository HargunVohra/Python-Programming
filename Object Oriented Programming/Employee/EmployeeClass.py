# Q3) Employee Class

# Write a class named Employee that holds the following data about an employee in 
# attributes:

# name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects 
# to hold the following data:

# Name 		        IDNumber		Department 		JobTitle
# Susan Meyers 	    47899			Accounting 		Vice President
# Mark Jones 	    39119 			IT 			    Programmer
# Joy Rogers 	    81774 			Manufacturing   Engineer

# The program should store this data in the three objects, then display the data for
# each employee on the screen.

# This exercise assumes you have created the Employee class. Create a program that 
# stores Employee objects in a dictionary. Use the employeeID numberas the key. The 
# program should present a menu that lets the user perform the followingactions:

# • Look up an employee in the dictionary
# • Add a new employee to the dictionary
# • Change an existing employee’s name, department, and job title in the dictionary
# • Delete an employee from the dictionary
# • Quit the program

# When the program ends, it should pickle the dictionary and save it to a file. Each 
# time theprogram starts, it should try to load the pickled dictionary from the file. 
# If the file does notexist, the program should start with an empty dictionary.

class Employee:
    def __init__(self, EmployeeName, EmployeeId, Department, JobTitle):
        self.__EmployeeName = EmployeeName
        self.__EmployeeId = EmployeeId
        self.__Department = Department
        self.__JobTitle = JobTitle
        
    def GetEmployeeName(self):
        return self.__EmployeeName
    
    def GetEmployeeId(self):
        return self.__EmployeeId
    
    def GetDepartment(self):
        return self.__Department
    
    def GetJobTitle(self):
        return self.__JobTitle
    
    def SetEmployeeName(self, EmployeeName):
        self.__EmployeeName = EmployeeName
        
    def SetEmployeeId(self, EmployeeId):
        self.__EmployeeId = EmployeeId
    
    def SetDepartment(self, Department):
        self.__Department = Department
        
    def SetJobTitle(self, JobTitle):
        self.__JobTitle = JobTitle
