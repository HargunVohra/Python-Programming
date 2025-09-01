from ConnectionDB import ConnectionDB

MyConnection = ConnectionDB()

MyCursor = MyConnection.cursor()
MyCursor.execute("""CREATE TABLE IF NOT EXISTS CourseSubject(CourseId INT,
                 SubjectId INT,
                 FOREIGN KEY (CourseId) REFERENCES Courses(CourseId),
                 FOREIGN KEY (SubjectId) REFERENCES Subjects(SubjectId)
                 )""")

# print("CourseSubject table created successfully!")

class CourseSubject:
    def __init__(self, CourseId, SubjectId):
        self.__CourseId = CourseId
        self.__SubjectId = SubjectId
    
    def AssignSubjectToCourse(self, cursor, connection):
        cursor.execute("SELECT * FROM Courses WHERE CourseId = %s", (self.__CourseId,))
        CourseRecord = cursor.fetchone()
        if CourseRecord is None:
            return "Course"

        cursor.execute("SELECT * FROM Subjects WHERE SubjectId = %s", (self.__SubjectId,))
        SubjectRecord = cursor.fetchone()
        if SubjectRecord is None:
            return "Subject"

        cursor.execute(
            "INSERT INTO CourseSubject (CourseId, SubjectId) VALUES (%s, %s)",
            (self.__CourseId, self.__SubjectId)
        )
        connection.commit()
        return "Success"
    
    def UpdateAssignedSubject(self, cursor, connection, CourseId, SubjectId):
        cursor.execute(
            "SELECT * FROM CourseSubject WHERE CourseId = %s AND SubjectId = %s",
            (CourseId, SubjectId)
        )
        Record = cursor.fetchone()
        cursor.fetchall()
    
        if Record is None:
            return "Assignment"
    
        NewCourseId = self.__CourseId if self.__CourseId != "" else Record[0]
        NewSubjectId = self.__SubjectId if self.__SubjectId != "" else Record[1]
    
        cursor.execute("SELECT * FROM Courses WHERE CourseId = %s", (NewCourseId,))
        CourseRecord = cursor.fetchone()
        cursor.fetchall() 
        if CourseRecord is None:
            return "Course"
    
        cursor.execute("SELECT * FROM Subjects WHERE SubjectId = %s", (NewSubjectId,))
        SubjectRecord = cursor.fetchone()
        cursor.fetchall() 
        if SubjectRecord is None:
            return "Subject"
    
        cursor.execute(
            """UPDATE CourseSubject
               SET CourseId = %s, SubjectId = %s
               WHERE CourseId = %s AND SubjectId = %s""",
            (NewCourseId, NewSubjectId, CourseId, SubjectId)
        )
        connection.commit()
        return True
    
    def DismissAssignedSubject(self, cursor, connection, CourseId, SubjectId):
        cursor.execute(
            "SELECT * FROM CourseSubject WHERE CourseId = %s AND SubjectId = %s",
            (CourseId, SubjectId)
        )
        record = cursor.fetchone()
    
        if record is None:
            return "Assignment"
        else:
            cursor.execute(
                "DELETE FROM CourseSubject WHERE CourseId = %s AND SubjectId = %s",
                (CourseId, SubjectId)
            )
            connection.commit()
            return True
        
    def ViewAssignedSubjectsByName(self, cursor, connection, CourseId):
        cursor.execute(
            """SELECT cs.CourseId, cs.SubjectId, s.SubjectName
               FROM CourseSubject cs
               INNER JOIN Subjects s ON cs.SubjectId = s.SubjectId
               WHERE cs.CourseId = %s""",
            (CourseId,)
        )
        return cursor.fetchall()
    
    
    def ViewAllAssignedSubjects(self, cursor, connection):
        cursor.execute(
            """SELECT cs.CourseId, c.CourseName, cs.SubjectId, s.SubjectName
               FROM CourseSubject cs
               INNER JOIN Courses c ON cs.CourseId = c.CourseId
               INNER JOIN Subjects s ON cs.SubjectId = s.SubjectId"""
        )
        return cursor.fetchall()

    @property
    def CourseSubjectCourseId(self):
        return self.__CourseId
    
    @CourseSubjectCourseId.setter
    def CourseSubjectCourseId(self, CourseId):
        self.__CourseId = CourseId
        
    
    @property
    def CourseSubjectSubjectId(self):
        return self.__SubjectId
    
    
    @CourseSubjectSubjectId.setter
    def CourseSubjectSubjectId(self, SubjectId):
        self.__SubjectId = SubjectId