from ConnectionDB import ConnectionDB

MyConnection = ConnectionDB()

MyCursor = MyConnection.cursor()
MyCursor.execute("""CREATE TABLE IF NOT EXISTS StudentCourseMarks(
                StudentId INT,
                CourseId INT,
                SubjectId INT,
                Marks INT,
                FOREIGN KEY (StudentId) REFERENCES Students(StudentId),
                FOREIGN KEY (CourseId) REFERENCES Courses(CourseId),
                FOREIGN KEY (SubjectId) REFERENCES Subjects(SubjectId)
                 )""")

# print("SubjectCourseMarks table created successfully!")

class StudentCourseMarks:
    def __init__(self, StudentId, CourseId, SubjectId, Marks):
        self.__StudentId = StudentId
        self.__CourseId = CourseId
        self.__SubjectId = SubjectId
        self.__Marks = Marks

    def GetAssignedSubjects(self, cursor, connection, CourseId):
        cursor.execute(
            """SELECT s.SubjectId, s.SubjectName
               FROM CourseSubject cs
               INNER JOIN Subjects s ON cs.SubjectId = s.SubjectId
               WHERE cs.CourseId = %s""",
            (CourseId,)
        )
        return cursor.fetchall()

    def SaveStudentCourseMarks(self, cursor, connection, StudentId, CourseId, MarksList):
        cursor.execute("SELECT * FROM Students WHERE StudentId = %s", (StudentId,))
        if cursor.fetchone() is None:
            return "Student"

        cursor.execute("SELECT * FROM Courses WHERE CourseId = %s", (CourseId,))
        if cursor.fetchone() is None:
            return "Course"

        cursor.execute(
            "SELECT * FROM StudentRegistrations WHERE StudentId = %s AND CourseId = %s",
            (StudentId, CourseId)
        )
        if cursor.fetchone() is None:
            return "Registration"

        AssignedSubjects = self.GetAssignedSubjects(cursor, connection, CourseId)
        if not AssignedSubjects:
            return "NoSubjects"

        if len(MarksList) != len(AssignedSubjects):
            return "Mismatch"

        SubjectCounter = 0
        for Subject in AssignedSubjects:
            SubjectId, SubjectName = Subject
            Marks = MarksList[SubjectCounter]

            cursor.execute(
                """SELECT * FROM StudentCourseMarks
                   WHERE StudentId = %s AND CourseId = %s AND SubjectId = %s""",
                (StudentId, CourseId, SubjectId)
            )
            if cursor.fetchone() is not None:
                return "Duplicate"

            cursor.execute(
                """INSERT INTO StudentCourseMarks(StudentId, CourseId, SubjectId, Marks)
                   VALUES(%s, %s, %s, %s)""",
                (StudentId, CourseId, SubjectId, Marks)
            )
            
            SubjectCounter = SubjectCounter + 1

        connection.commit()
        return True
    
    def UpdateStudentCourseMarks(self, cursor, connection, StudentId, CourseId, MarksList):
        cursor.execute("SELECT * FROM Students WHERE StudentId = %s", (StudentId,))
        if cursor.fetchone() is None:
            return "Student"
    
        cursor.execute("SELECT * FROM Courses WHERE CourseId = %s", (CourseId,))
        if cursor.fetchone() is None:
            return "Course"
    
        cursor.execute(
            "SELECT * FROM StudentRegistrations WHERE StudentId = %s AND CourseId = %s",
            (StudentId, CourseId)
        )
        if cursor.fetchone() is None:
            return "Registration"
    
        AssignedSubjects = self.GetAssignedSubjects(cursor, connection, CourseId)
        if not AssignedSubjects:
            return "NoSubjects"
    
        if len(MarksList) != len(AssignedSubjects):
            return "Mismatch"
    
        SubjectCounter = 0
        for Subject in AssignedSubjects:
            SubjectId, SubjectName = Subject
            NewMarks = MarksList[SubjectCounter]
    
            cursor.execute(
                """SELECT Marks FROM StudentCourseMarks
                   WHERE StudentId = %s AND CourseId = %s AND SubjectId = %s""",
                (StudentId, CourseId, SubjectId)
            )
            record = cursor.fetchone()
            if record is None:
                return "NoMarks"
    
            OldMarks = record[0]
            FinalMarks = NewMarks if NewMarks != "" else OldMarks
    
            cursor.execute(
                """UPDATE StudentCourseMarks
                   SET Marks = %s
                   WHERE StudentId = %s AND CourseId = %s AND SubjectId = %s""",
                (FinalMarks, StudentId, CourseId, SubjectId)
            )
            SubjectCounter += 1
    
        connection.commit()
        return True

    def DeleteStudentCourseMarks(self, cursor, connection, StudentId, CourseId):
        cursor.execute("SELECT * FROM Students WHERE StudentId = %s", (StudentId,))
        if cursor.fetchone() is None:
            cursor.fetchall()
            return "Student"
        cursor.fetchall()
    
        cursor.execute("SELECT * FROM Courses WHERE CourseId = %s", (CourseId,))
        if cursor.fetchone() is None:
            cursor.fetchall()
            return "Course"
        cursor.fetchall()
    
        cursor.execute(
            "SELECT * FROM StudentRegistrations WHERE StudentId = %s AND CourseId = %s",
            (StudentId, CourseId)
        )
        if cursor.fetchone() is None:
            cursor.fetchall()
            return "Registration"
        cursor.fetchall()
    
        cursor.execute(
            "SELECT * FROM StudentCourseMarks WHERE StudentId = %s AND CourseId = %s",
            (StudentId, CourseId)
        )
        if cursor.fetchone() is None:
            cursor.fetchall()
            return "NoMarks"
        cursor.fetchall()
    
        cursor.execute(
            "DELETE FROM StudentCourseMarks WHERE StudentId = %s AND CourseId = %s",
            (StudentId, CourseId)
        )
        connection.commit()
        return True
    
    def ViewStudentCourseMarks(self, cursor, connection, StudentId, CourseId):
        cursor.execute(
            """SELECT st.StudentName, c.CourseName, s.SubjectName, scm.Marks
               FROM StudentCourseMarks scm
               INNER JOIN Students st ON scm.StudentId = st.StudentId
               INNER JOIN Courses c ON scm.CourseId = c.CourseId
               INNER JOIN Subjects s ON scm.SubjectId = s.SubjectId
               WHERE scm.StudentId = %s AND scm.CourseId = %s""",
            (StudentId, CourseId)
        )
        Records = cursor.fetchall()
        if not Records:
            return False
        else:
            return Records
        
    def ViewAllStudentCourseMarks(self, cursor, connection):
        cursor.execute(
            """SELECT s.StudentName, c.CourseName, sub.SubjectName, m.Marks
               FROM StudentCourseMarks m
               INNER JOIN Students s ON m.StudentId = s.StudentId
               INNER JOIN Courses c ON m.CourseId = c.CourseId
               INNER JOIN Subjects sub ON m.SubjectId = sub.SubjectId"""
        )
        return cursor.fetchall()

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
    def SubjectId(self):
        return self.__SubjectId
    
    @SubjectId.setter
    def SubjectId(self, SubjectId):
        self.__SubjectId = SubjectId
        
        
    @property
    def StudentMarks(self):
        return self.__Marks
    
    @StudentMarks.setter
    def StudentMarks(self, Marks):
        self.__Marks = Marks