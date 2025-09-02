from ConnectionDB import ConnectionDB

MyConnection = ConnectionDB()
MyCursor = MyConnection.cursor()

MyCursor.execute("""CREATE TABLE IF NOT EXISTS SignUpDetails(
    UserId INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(30),
    Password VARCHAR(30),
    FullName VARCHAR(50),
    Address VARCHAR(100),
    Email VARCHAR(50),
    PhoneNumber VARCHAR(15)
)""")

# print("Sign up details table created successfully!")


class SignUp:
    def __init__(self, Username, Password, FullName, Address, Email, PhoneNumber):
        self.__Username = Username
        self.__Password = Password
        self.__FullName = FullName
        self.__Address = Address
        self.__Email = Email
        self.__PhoneNumber = PhoneNumber
        
    def SaveSignUp(self, cursor, connection):
        cursor.execute(
            "INSERT INTO SignUpDetails (Username, Password, FullName, Address, Email, PhoneNumber) VALUES (%s, %s, %s, %s, %s, %s)",
            (self.__Username, self.__Password, self.__FullName, self.__Address, self.__Email, self.__PhoneNumber)
        )
        connection.commit()

    @property
    def SignUpUsername(self):
        return self.__Username

    @SignUpUsername.setter
    def SignUpUsername(self, Username):
        self.__Username = Username
        

    @property
    def SignUpPassword(self):
        return self.__Password

    @SignUpPassword.setter
    def SignUpPassword(self, Password):
        self.__Password = Password
        

    @property
    def SignUpFullName(self):
        return self.__FullName

    @SignUpFullName.setter
    def SignUpFullName(self, FullName):
        self.__FullName = FullName
        

    @property
    def SignUpAddress(self):
        return self.__Address

    @SignUpAddress.setter
    def SignUpAddress(self, Address):
        self.__Address = Address


    @property
    def SignUpEmail(self):
        return self.__Email

    @SignUpEmail.setter
    def SignUpEmail(self, Email):
        self.__Email = Email
        

    @property
    def SignUpPhoneNumber(self):
        return self.__PhoneNumber

    @SignUpPhoneNumber.setter
    def SignUpPhoneNumber(self, PhoneNumber):
        self.__PhoneNumber = PhoneNumber
