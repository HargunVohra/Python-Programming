from ConnectionDB import ConnectionDB

MyConnection = ConnectionDB()

MyCursor = MyConnection.cursor()
MyCursor.execute("CREATE DATABASE IF NOT EXISTS CollegeManagementSystem")
# print("Database created successfully!")

MyCursor.execute("""CREATE TABLE IF NOT EXISTS Courses(CourseId INT AUTO_INCREMENT PRIMARY KEY, 
                 CourseName VARCHAR(20), 
                 CourseTypeId INT, 
                 CourseDuration VARCHAR(30), 
                 StartDate DATE, 
                 CourseFee INT(10),
                 FOREIGN KEY (CourseTypeId) REFERENCES CourseType(CourseTypeId)
                 )""")
# print("Courses table created successfully!")

class Courses:
    def __init__(self,Name, CourseTypeId, Duration, StartDate, Fee):
        self.__Name = Name
        self.__CourseTypeId = CourseTypeId
        self.__Duration = Duration
        self.__StartDate = StartDate
        self.__Fee = Fee
        
    def SaveCourse(self, cursor, connection):
        cursor.execute(
            "SELECT CourseTypeId FROM CourseType WHERE CourseTypeId = %s",
            (self.__CourseTypeId,)
        )
        record = cursor.fetchone()
    
        if record is None:
            return False  
    
        cursor.execute(
            """INSERT INTO Courses (CourseName, CourseTypeId, CourseDuration, StartDate, CourseFee)
               VALUES (%s, %s, %s, %s, %s)""",
            (self.__Name, self.__CourseTypeId, self.__Duration, self.__StartDate, self.__Fee)
            )
        connection.commit()
        return True
    
    def UpdateCourse(self, cursor, connection, CourseName):
        cursor.execute(
            "SELECT * FROM Courses WHERE CourseName = %s",
            (CourseName,)
        )
        Record = cursor.fetchone()
    
        if Record is None:
            return False
        else:
            Name = self.__Name if self.__Name != "" else Record[1]
            CourseTypeId = self.__CourseTypeId if self.__CourseTypeId != "" else Record[2]
            Duration = self.__Duration if self.__Duration != "" else Record[3]
            StartDate = self.__StartDate if self.__StartDate != "" else Record[4]
            Fee = self.__Fee if self.__Fee != "" else Record[5]
    
            if self.__CourseTypeId != "":
                cursor.execute(
                    "SELECT * FROM CourseType WHERE CourseTypeId = %s",
                    (self.__CourseTypeId,)
                )
                RecordType = cursor.fetchone()
                if RecordType is None:
                    return False
    
            cursor.execute(
                """UPDATE Courses 
                   SET CourseName = %s, CourseTypeId = %s, CourseDuration = %s, StartDate = %s, CourseFee = %s
                   WHERE CourseName = %s""",
                (Name, CourseTypeId, Duration, StartDate, Fee, CourseName)
            )
            connection.commit()
            return True
        
    def DeleteCourse(self, cursor, connection, CourseId):
        cursor.execute(
            "SELECT * FROM Courses WHERE CourseId = %s",
            (CourseId,)
        )
        record = cursor.fetchone()
    
        if record is None:
            return False
        else:
            cursor.execute(
                "DELETE FROM Courses WHERE CourseId = %s",
                (CourseId,)
            )
            connection.commit()
            return True
        
    def ViewCourse(self, cursor, connection, CourseName):
        cursor.execute(
            "SELECT * FROM Courses WHERE CourseName = %s",
            (CourseName,)
        )
        record = cursor.fetchone()
        if record is None:
            return False
        else:
            return record
    
    def ViewAllCourses(self, cursor, connection):
        cursor.execute("SELECT * FROM Courses")
        return cursor.fetchall()

    @property
    def CourseName(self):
        return self.__Name
    
    @CourseName.setter
    def CourseName(self, Name):
        self.__Name = Name
        
        
    @property
    def CourseType(self):
        return self.__CourseTypeId
    
    @CourseType.setter
    def CourseType(self, CourseTypeId):
        self.__CourseTypeId = CourseTypeId
        
        
    @property
    def CourseDuration(self):
        return self.__Duration
    
    @CourseDuration.setter
    def CourseDuration(self, Duration):
        self.__Duration = Duration
        
        
    @property
    def CourseStartDate(self):
        return self.__StartDate
    
    @CourseStartDate.setter
    def CourseStartDate(self, StartDate):
        self.__StartDate = StartDate
        
        
    @property
    def CourseFee(self):
        return self.__Fee
    
    @CourseFee.setter
    def CourseFee(self, Fee):
        self.__Fee = Fee
        
        
    @property
    def CourseTypeId(self):
        return self.__CourseTypeId
    
    @CourseTypeId.setter
    def CourseTypeId(self, CourseTypeId):
        self.__CourseTypeId = CourseTypeId