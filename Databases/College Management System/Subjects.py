from ConnectionDB import ConnectionDB

MyConnection = ConnectionDB()

MyCursor = MyConnection.cursor()
MyCursor.execute("""CREATE TABLE IF NOT EXISTS Subjects(SubjectId INT AUTO_INCREMENT PRIMARY KEY,
                 SubjectName VARCHAR(30),
                 NumberOfCredits VARCHAR(20),
                 FacultyId INT,
                 FOREIGN KEY (FacultyId) REFERENCES Faculty(FacultyId)
                 )""")

# print("Subjects table created successfully!")

class Subjects:
    def __init__(self, Name, NumberOfCredits, FacultyId):
        self.__Name = Name
        self.__NumberOfCredits = NumberOfCredits
        self.__FacultyId = FacultyId

    def SaveSubject(self, cursor, connection):
        cursor.execute(
            "SELECT FacultyId FROM Faculty WHERE FacultyId = %s",
            (self.__FacultyId,)
        )
        Record = cursor.fetchone()

        if Record is None:
            return False  

        cursor.execute(
            """INSERT INTO Subjects (SubjectName, NumberOfCredits, FacultyId)
               VALUES (%s, %s, %s)""",
            (self.__Name, self.__NumberOfCredits, self.__FacultyId)
        )
        connection.commit()
        return True
    
    def UpdateSubject(self, Cursor, Connection, SubjectName):
        Cursor.execute(
            "SELECT * FROM Subjects WHERE SubjectName = %s",
            (SubjectName,)
        )
        Record = Cursor.fetchone()
    
        if Record is None:
            return False
        else:
            Name = self.__Name if self.__Name != "" else Record[1]
            NumberOfCredits = self.__NumberOfCredits if self.__NumberOfCredits != "" else Record[2]
            FacultyId = self.__FacultyId if self.__FacultyId != "" else Record[3]
    
            if self.__FacultyId != "":
                Cursor.execute(
                    "SELECT * FROM Faculty WHERE FacultyId = %s",
                    (self.__FacultyId,)
                )
                RecordFaculty = Cursor.fetchone()
                if RecordFaculty is None:
                    return False
    
            Cursor.execute(
                """UPDATE Subjects
                   SET SubjectName = %s, NumberOfCredits = %s, FacultyId = %s
                   WHERE SubjectName = %s""",
                (Name, NumberOfCredits, FacultyId, SubjectName)
            )
            Connection.commit()
            return True
        
    def DeleteSubject(self, cursor, connection, SubjectId):
        cursor.execute("SELECT * FROM Subjects WHERE SubjectId = %s", (SubjectId,))
        Record = cursor.fetchone()
    
        if Record is None:
            return False
        else:
            cursor.execute("DELETE FROM Subjects WHERE SubjectId = %s", (SubjectId,))
            connection.commit()
            return True
        
    def ViewSubject(self, cursor, connection, SubjectName):
        cursor.execute(
            "SELECT * FROM Subjects WHERE SubjectName = %s",
            (SubjectName,)
        )
        Record = cursor.fetchone()
        if Record is None:
            return False
        else:
            return Record
    
    def ViewAllSubjects(self, cursor, connection):
        cursor.execute("SELECT * FROM Subjects")
        Records = cursor.fetchall()
        if not Records:
            return False
        else:
            return Records

    @property
    def SubjectName(self):
        return self.__Name
    
    @SubjectName.setter
    def SubjectName(self, Name):
        self.__Name = Name
        
        
    @property
    def SubjectCredits(self):
        return self.__Credits
    
    @SubjectCredits.setter
    def SubjectCredits(self, Credits):
        self.__Credits = Credits