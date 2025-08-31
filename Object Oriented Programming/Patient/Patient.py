# Q4) Patient Charges
# Write a class named Patient that has attributes for the following data:

# • First name, middle name, and last name
# • Address, city, state, and ZIP code
# • Phone number
# • Name and phone number of emergency contact

# The Patient class’s _ _init_ _ method should accept an argument for each 
# attribute. The Patient class should also have accessor and mutator methods for 
# each attribute. Next, write a class named Procedure that represents a medical 
# procedure that has been performed on a patient. The Procedure class should have 
# attributes for the following data:
# • Name of the procedure
# • Date of the procedure
# • Name of the practitioner who performed the procedure
# • Charges for the procedure

# The Procedure class’s _ _init_ _ method should accept an argument for each 
# attribute. The Procedure class should also have accessor and mutator methods 
# for each attribute. Next, write a program that creates an instance of the 
# Patient class, initialized with sample data. Then, create three instances of 
# the Procedure class, initialized with the following data:

# Procedure #1: 							
# Procedure name: Physical Exam
# Date: Today’s date
# Practitioner: Dr. Irvine
# Charge: 250.00

# Procedure #2:
# Procedure name: X-ray
# Date: Today’s date
# Practitioner: Dr. Jamison
# Charge: 500.00

# Procedure #3:
# Procedure name: Blood test
# Date: Today’s date
# Practitioner: Dr. Smith
# Charge: 200.00

# The program should display the patient’s information, information about all 
# three of the procedures, and the total charges of the three procedures.

class Patient:
    def __init__(self, FirstName, MiddleName, LastName, Address, City, State, PinCode, PhoneNumber, EmergencyContactName, EmergencyContactNumber):
        self.__FirstName = FirstName
        self.__MiddleName = MiddleName
        self.__LastName = LastName
        self.__Address = Address
        self.__City = City
        self.__State = State
        self.__PinCode = PinCode
        self.__PhoneNumber = PhoneNumber
        self.__EmergencyContactName = EmergencyContactName
        self.__EmergencyContactNumber = EmergencyContactNumber
        
        
    def GetFirstName(self):
        return self.__FirstName
    
    def GetMiddleName(self):
        return self.__MiddleName
    
    def GetLastName(self):
        return self.__LastName
    
    def GetAddress(self):
        return self.__Address
    
    def GetCity(self):
        return self.__City
    
    def GetState(self):
        return self.__State
    
    def GetPinCode(self):
        return self.__PinCode
    
    def GetPhoneNumer(self):
        return self.__PhoneNumber
    
    def GetEmergencyContactName(self):
        return self.__EmergencyContactName
    
    def GetEmergencyContactNumber(self):
        return self.__EmergencyContactNumber
    
    
    def SetFirstName(self, FirstName):
        self.__FirstName = FirstName
        
    def SetMiddleName(self, MiddleName):
        self.__MiddleName = MiddleName
        
    def SetLastName(self, LastName):
        self.__LastName = LastName
        
    def SetAddress(self, Address):
        self.__Address = Address
        
    def SetCity(self, City):
        self.__City = City
        
    def SetState(self, State):
        self.__State = State
        
    def SetPinCode(self, PinCode):
        self.__PinCode = PinCode
        
    def SetPhoneNumber(self, PhoneNumber):
        self.__PhoneNumber = PhoneNumber
        
    def SetEmergencyContactName(self, EmergencyContactName):
        self.__EmergencyContactName = EmergencyContactName
        
    def SetEmergencyContactNumber(self, EmergencyContactNumber):
        self.__EmergencyContactNumber = EmergencyContactNumber