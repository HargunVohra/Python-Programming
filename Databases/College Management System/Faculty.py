from ConnectionDB import ConnectionDB

MyConnection = ConnectionDB()

MyCursor = MyConnection.cursor()
MyCursor.execute("""CREATE TABLE IF NOT EXISTS Faculty(FacultyId INT AUTO_INCREMENT PRIMARY KEY,
                 FacultyName VARCHAR(30),
                 RoomNumber VARCHAR(10),
                 MobileNumber VARCHAR(25),
                 Email VARCHAR(50)
                 )""")

# print("Faculty table created successfully!")

class Faculty:
    def __init__(self, Name, RoomNumber, MobileNumber, Email):
        self.__Name = Name
        self.__RoomNumber = RoomNumber
        self.__MobileNumber = MobileNumber
        self.__Email = Email
        
    def SaveFaculty(self, cursor, connection):
        cursor.execute(
            "INSERT INTO Faculty (FacultyName, RoomNumber, MobileNumber, Email) VALUES (%s, %s, %s, %s)",
            (self.__Name, self.__RoomNumber, self.__MobileNumber, self.__Email)
        )
        connection.commit()
        
    def UpdateFaculty(self, cursor, connection, FacultyName):
        cursor.execute(
            "SELECT * FROM Faculty WHERE FacultyName = %s",
            (FacultyName,)
        )
        Record = cursor.fetchone()
    
        if Record is None:
            return False  
        else:
            Name = self.__Name if self.__Name != "" else Record[1]
            RoomNumber = self.__RoomNumber if self.__RoomNumber != "" else Record[2]
            MobileNumber = self.__MobileNumber if self.__MobileNumber != "" else Record[3]
            Email = self.__Email if self.__Email != "" else Record[4]
    
            cursor.execute(
                """UPDATE Faculty 
                   SET FacultyName = %s, RoomNumber = %s, MobileNumber = %s, Email = %s
                   WHERE FacultyName = %s""",
                (Name, RoomNumber, MobileNumber, Email, FacultyName)
            )
            connection.commit()
            return True
        
    def DeleteFaculty(self, cursor, connection, FacultyId):
        cursor.execute("SELECT * FROM Faculty WHERE FacultyId = %s", (FacultyId,))
        Record = cursor.fetchone()
    
        if Record is None:
            return False
        else:
            cursor.execute("DELETE FROM Faculty WHERE FacultyId = %s", (FacultyId,))
            connection.commit()
            return True
        
    def ViewFaculty(self, cursor, connection, FacultyName):
        cursor.execute(
            "SELECT * FROM Faculty WHERE FacultyName = %s",
            (FacultyName,)
        )
        record = cursor.fetchone()
        if record is None:
            return False
        else:
            return record
    
    def ViewAllFaculties(self, cursor, connection):
        cursor.execute("SELECT * FROM Faculty")
        return cursor.fetchall()
    
    @property
    def FacultyName(self):
        return self.__Name
    
    @FacultyName.setter
    def FacultyName(self, Name):
        self.__Name = Name
        
        
    @property
    def FacultyRoomNumber(self):
        return self.__RoomNumber
    
    @FacultyRoomNumber.setter
    def FacultyRoomNumber(self, RoomNumber):
        self.__RoomNumber = RoomNumber
        
        
    @property
    def FacultyMobileNumber(self):
        return self.__MobileNumber
    
    @FacultyMobileNumber.setter
    def FacultyMobileNumber(self, MobileNumber):
        self.__MobileNumber = MobileNumber
        
        
    @property
    def FacultyEmail(self):
        return self.__Email
    
    @FacultyEmail.setter
    def FacultyEmail(self, Email):
        self.__Email = Email