from ConnectionDB import ConnectionDB

MyConnection = ConnectionDB()

MyCursor = MyConnection.cursor()
MyCursor.execute("""CREATE TABLE IF NOT EXISTS Students(StudentId INT AUTO_INCREMENT PRIMARY KEY,
                 StudentName VARCHAR(30),
                 Address VARCHAR(100),
                 City VARCHAR(20),
                 State VARCHAR (20),
                 ZipCode INT(6),
                 MobileNumber VARCHAR(25),
                 Email VARCHAR(50),
                 DateOfBirth DATE,
                 Gender VARCHAR(10)
                 )""")

# print("Students table created successfully!")

class Student:
    def __init__(self, Name, Address, City, State, ZipCode, MobileNumber, Email, DateOfBirth, Gender):
        self.__Name = Name
        self.__Address = Address
        self.__City = City
        self.__State = State
        self.__ZipCode = ZipCode
        self.__MobileNumber = MobileNumber
        self.__Email = Email
        self.__DateOfBirth = DateOfBirth
        self.__Gender = Gender
        
    def SaveStudent(self, cursor, connection):
        cursor.execute(
            """INSERT INTO Students 
               (StudentName, Address, City, State, ZipCode, MobileNumber, Email, DateOfBirth, Gender)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (self.__Name, self.__Address, self.__City, self.__State, self.__ZipCode,
             self.__MobileNumber, self.__Email, self.__DateOfBirth, self.__Gender)
        )
        connection.commit()
        return True
    
    def UpdateStudent(self, cursor, connection, StudentName):
        cursor.execute(
            "SELECT * FROM Students WHERE StudentName = %s",
            (StudentName,)
        )
        Record = cursor.fetchone()
    
        if Record is None:
            return False
        else:
            Name = self.__Name if self.__Name != "" else Record[1]
            Address = self.__Address if self.__Address != "" else Record[2]
            City = self.__City if self.__City != "" else Record[3]
            State = self.__State if self.__State != "" else Record[4]
            ZipCode = self.__ZipCode if self.__ZipCode != "" else Record[5]
            MobileNumber = self.__MobileNumber if self.__MobileNumber != "" else Record[6]
            Email = self.__Email if self.__Email != "" else Record[7]
            DateOfBirth = self.__DateOfBirth if self.__DateOfBirth != "" else Record[8]
            Gender = self.__Gender if self.__Gender != "" else Record[9]
    
            cursor.execute(
                """UPDATE Students
                   SET StudentName = %s, Address = %s, City = %s, State = %s, 
                       ZipCode = %s, MobileNumber = %s, Email = %s, DateOfBirth = %s, Gender = %s
                   WHERE StudentName = %s""",
                (Name, Address, City, State, ZipCode, MobileNumber, Email, DateOfBirth, Gender, StudentName)
            )
            connection.commit()
            return True
    
    def DeleteStudent(self, cursor, connection, StudentId):
        cursor.execute(
            "SELECT * FROM Students WHERE StudentId = %s",
            (StudentId,)
        )
        Record = cursor.fetchone()
    
        if Record is None:
            return False
        else:
            cursor.execute(
                "DELETE FROM Students WHERE StudentId = %s",
                (StudentId,)
            )
            connection.commit()
            return True
        
    def ViewStudent(self, cursor, connection, StudentName):
        cursor.execute(
            "SELECT * FROM Students WHERE StudentName = %s",
            (StudentName,)
        )
        Record = cursor.fetchone()
        if Record is None:
            return False
        else:
            return Record

    def ViewAllStudents(self, cursor, connection):
        cursor.execute("SELECT * FROM Students")
        return cursor.fetchall()
    
    @property
    def StudentName(self):
        return self.__Name
    
    @StudentName.setter
    def StudentName(self, Name):
        self.__Name = Name
        
        
    @property
    def StudentAddress(self):
        return self.__Address
    
    @StudentAddress.setter
    def StudentAddress(self, Address):
        self.__Address = Address
        
        
    @property
    def StudentCity(self):
        return self.__City
    
    @StudentCity.setter
    def StudentCity(self, City):
        self.__City = City
        
              
    @property
    def StudentState(self):
        return self.__State
    
    @StudentState.setter
    def StudentState(self, State):
        self.__State = State
        
        
    @property
    def StudentZipCode(self):
        return self.__ZipCode
    
    @StudentZipCode.setter
    def StudentZipCode(self, ZipCode):
        self.__ZipCode = ZipCode
        
        
    @property
    def StudentMobileNumber(self):
        return self.__MobileNumber
    
    @StudentMobileNumber.setter
    def StudentMobileNumber(self, MobileNumber):
        self.__MobileNumber = MobileNumber
        
        
    @property
    def StudentEmail(self):
        return self.__Email
    
    @StudentEmail.setter
    def StudentEmail(self, Email):
        self.__Email = Email
        
              
    @property
    def StudentDateOfBirth(self):
        return self.__DateOfBirth
    
    @StudentDateOfBirth.setter
    def StudentDateOfBirth(self, DateOfBirth):
        self.__DateOfBirth = DateOfBirth
        
        
    @property
    def StudentGender(self):
        return self.__Gender
    
    @StudentGender.setter
    def StudentGender(self, Gender):
        self.__Gender = Gender