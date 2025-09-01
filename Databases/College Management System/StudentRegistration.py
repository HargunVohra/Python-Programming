from ConnectionDB import ConnectionDB

MyConnection = ConnectionDB()

MyCursor = MyConnection.cursor()
MyCursor.execute("""CREATE TABLE IF NOT EXISTS StudentRegistrations(RegistrationNumber INT PRIMARY KEY,
                 RegistrationDate DATE,
                 StudentId INT,
                 CourseId INT,
                 CourseFee INT(10),
                 FeePaid INT(10),
                 BalanceFee INT(10),
                 FOREIGN KEY (StudentId) REFERENCES Students(StudentId),
                 FOREIGN KEY (CourseId) REFERENCES Courses(CourseId)
                 )""")

# print("StudentRegistrations table created successfully!")

class StudentRegistration:
    def __init__(self, RegistrationNumber, RegistrationDate, StudentId, CourseId, CourseFee, FeePaid, BalanceFee):
        self.__RegistrationNumber = RegistrationNumber
        self.__RegistrationDate = RegistrationDate
        self.__StudentId = StudentId
        self.__CourseId = CourseId
        self.__CourseFee = CourseFee
        self.__FeePaid = FeePaid
        self.__BalanceFee = BalanceFee
        
    def RegisterStudent(self, cursor, connection):
        cursor.execute("SELECT * FROM Students WHERE StudentId = %s", (self.__StudentId,))
        StudentRecord = cursor.fetchone()
        if StudentRecord is None:
            return "Student"

        cursor.execute("SELECT * FROM Courses WHERE CourseId = %s", (self.__CourseId,))
        CourseRecord = cursor.fetchone()
        if CourseRecord is None:
            return "Course"

        cursor.execute(
            "SELECT * FROM StudentRegistrations WHERE StudentId = %s AND CourseId = %s",
            (self.__StudentId, self.__CourseId)
        )
        Duplicate = cursor.fetchone()
        if Duplicate:
            return "Duplicate"

        CourseFee = CourseRecord[5]
        BalanceFee = CourseFee - self.__FeePaid

        cursor.execute(
            """INSERT INTO StudentRegistrations
               (RegistrationNumber, RegistrationDate, StudentId, CourseId, CourseFee, FeePaid, BalanceFee)
               VALUES (%s, %s, %s, %s, %s, %s, %s)""",
            (self.__RegistrationNumber, self.__RegistrationDate, self.__StudentId, self.__CourseId,
             CourseFee, self.__FeePaid, BalanceFee)
        )
        connection.commit()
        return True
    
    def UpdateRegisteredStudent(self, cursor, connection, RegistrationNumber):
        cursor.execute("SELECT * FROM StudentRegistrations WHERE RegistrationNumber = %s", (RegistrationNumber,))
        record = cursor.fetchone()
        if record is None:
            return "Registration"
    
        NewRegistrationDate = self.__RegistrationDate if self.__RegistrationDate != "" else record[1]
        NewStudentId = self.__StudentId if self.__StudentId != "" else record[2]
        NewCourseId = self.__CourseId if self.__CourseId != "" else record[3]
        NewFeePaid = self.__FeePaid if self.__FeePaid != "" else record[5]
    
        cursor.execute("SELECT * FROM Students WHERE StudentId = %s", (NewStudentId,))
        if cursor.fetchone() is None:
            return "Student"
    
        cursor.execute("SELECT * FROM Courses WHERE CourseId = %s", (NewCourseId,))
        course_record = cursor.fetchone()
        if course_record is None:
            return "Course"
    
        CourseFee = course_record[5]   
        BalanceFee = CourseFee - int(NewFeePaid)
    
        cursor.execute("""
            UPDATE StudentRegistrations
            SET RegistrationDate = %s, StudentId = %s, CourseId = %s,
                CourseFee = %s, FeePaid = %s, BalanceFee = %s
            WHERE RegistrationNumber = %s
        """, (NewRegistrationDate, NewStudentId, NewCourseId,
              CourseFee, NewFeePaid, BalanceFee, RegistrationNumber))
        connection.commit()
    
        return True
    
    def UnregisterStudent(self, cursor, connection, RegistrationNumber):
        cursor.execute("SELECT * FROM StudentRegistrations WHERE RegistrationNumber = %s", (RegistrationNumber,))
        record = cursor.fetchone()
        if record is None:
            return False
    
        cursor.execute("DELETE FROM StudentRegistrations WHERE RegistrationNumber = %s", (RegistrationNumber,))
        connection.commit()
        return True
    
    def ViewRegistration(self, cursor, connection, RegistrationNumber):
        cursor.execute(
            """SELECT r.RegistrationNumber, r.RegistrationDate, s.StudentName, c.CourseName, 
                      r.CourseFee, r.FeePaid, r.BalanceFee
               FROM StudentRegistrations r
               INNER JOIN Students s ON r.StudentId = s.StudentId
               INNER JOIN Courses c ON r.CourseId = c.CourseId
               WHERE r.RegistrationNumber = %s""",
            (RegistrationNumber,)
        )
        record = cursor.fetchone()
        if record is None:
            return False
        else:
            return record
    
    def ViewAllRegistrations(self, cursor, connection):
        cursor.execute(
            """SELECT r.RegistrationNumber, r.RegistrationDate, s.StudentName, c.CourseName, 
                      r.CourseFee, r.FeePaid, r.BalanceFee
               FROM StudentRegistrations r
               INNER JOIN Students s ON r.StudentId = s.StudentId
               INNER JOIN Courses c ON r.CourseId = c.CourseId"""
        )
        return cursor.fetchall()
        
    @property
    def StudentRegistrationNumber(self):
        return self.__RegistrationNumber
    
    @StudentRegistrationNumber.setter
    def StudentRegistrationNumber(self, RegistrationNumber):
        self.__RegistrationNumber = RegistrationNumber
        
        
    @property
    def StudentRegistrationDate(self):
        return self.__RegistrationDate
    
    
    @StudentRegistrationDate.setter
    def StudentRegistrationDate(self, RegistrationDate):
        self.__RegistrationDate = RegistrationDate
        
        
    @property
    def StudentId(self):
        return self.__StudentId
    
    @StudentId.setter
    def StudentId(self, StudentId):
        self.__StudentId = StudentId
        
              
    @property
    def CourseId(self):
        return self.__CourseId
    
    @CourseId.setter
    def CourseId(self, CourseId):
        self.__CourseId = CourseId
        
    
    @property
    def CourseFee(self):
        return self.__CourseFee
    
    @CourseFee.setter
    def CourseFee(self, CourseFee):
        self.__CourseFee = CourseFee
        
        
    @property
    def StudentFeePaid(self):
        return self.__FeePaid
    
    @StudentFeePaid.setter
    def StudentFeePaid(self, FeePaid):
        self.__FeePaid = FeePaid
        
        
    @property
    def StudentBalanceFee(self):
        return self.__CourseFee - self.__FeePaid
    