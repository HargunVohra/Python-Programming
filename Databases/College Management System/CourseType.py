from ConnectionDB import ConnectionDB

MyConnection = ConnectionDB()

MyCursor = MyConnection.cursor()

MyCursor.execute("""CREATE TABLE IF NOT EXISTS CourseType(CourseTypeId INT AUTO_INCREMENT PRIMARY KEY,
                 CourseTypeName VARCHAR(30)
                 )""")
# print("CourseType table created successfully!")

class CourseType:
    def __init__(self, Name):
        self.__Name = Name
        
    def SaveCourseType(self, cursor, connection):
        cursor.execute(
            "INSERT INTO CourseType (CourseTypeName) VALUES (%s)",
            (self.__Name,)
        )
        connection.commit()

    def UpdateCourseType(self, cursor, connection, CourseTypeName):
        cursor.execute(
            "SELECT * FROM CourseType WHERE CourseTypeName = %s",
            (CourseTypeName,)
        )
        record = cursor.fetchone()
    
        if record is None:
            return False  
        else:
            cursor.execute(
                "UPDATE CourseType SET CourseTypeName = %s WHERE CourseTypeName = %s",
                (self.__Name, CourseTypeName)
            )
            connection.commit()
            return True  
        
    def DeleteCourseType(self, cursor, connection, CourseTypeId):
        cursor.execute(
            "DELETE FROM CourseType WHERE CourseTypeId = %s",
            (CourseTypeId,)
        )
        connection.commit()
        return cursor.rowcount > 0
    
    def ViewCourseType(self, cursor, connection, CourseTypeName):
        cursor.execute(
            "SELECT * FROM CourseType WHERE CourseTypeName = %s",
            (CourseTypeName,)
        )
        record = cursor.fetchone()
        if record is None:
            return False
        else:
            return record

    def ViewAllCourseTypes(self, cursor, connection):
        cursor.execute("SELECT * FROM CourseType")
        return cursor.fetchall()
        
    @property
    def CourseTypeName(self):
        return self.__Name
    
    @CourseTypeName.setter
    def CourseTypeName(self, Name):
        self.__Name = Name