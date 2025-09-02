from ConnectionDB import ConnectionDB

MyConnection = ConnectionDB()
MyCursor = MyConnection.cursor()

MyCursor.execute("""CREATE TABLE IF NOT EXISTS GearboxType(
    GearboxTypeId INT AUTO_INCREMENT PRIMARY KEY,
    GearboxTypeName VARCHAR(30)
)""")

# print("GearboxType table created successfully!")

class GearboxType:
    def __init__(self, Name):
        self.__Name = Name
        
    def SaveGearboxType(self, cursor, connection):
        cursor.execute(
            "INSERT INTO GearboxType (GearboxTypeName) VALUES (%s)",
            (self.__Name,)
        )
        connection.commit()

    def UpdateGearboxType(self, cursor, connection, GearboxTypeName, NewGearboxTypeName):
        cursor.execute(
            "SELECT * FROM GearboxType WHERE GearboxTypeName = %s",
            (GearboxTypeName,)
        )
        record = cursor.fetchone()
    
        if record is None:
            return False
        else:
            cursor.execute(
                "UPDATE GearboxType SET GearboxTypeName = %s WHERE GearboxTypeName = %s",
                (NewGearboxTypeName, GearboxTypeName)
            )
            connection.commit()
            return True
        
    def DeleteGearboxType(self, cursor, connection, GearboxTypeId):
        cursor.execute(
            "DELETE FROM GearboxType WHERE GearboxTypeId = %s",
            (GearboxTypeId,)
        )
        connection.commit()
        return cursor.rowcount > 0
    
    def ViewGearboxType(self, cursor, connection, GearboxTypeName):
        cursor.execute(
            "SELECT * FROM GearboxType WHERE GearboxTypeName = %s",
            (GearboxTypeName,)
        )
        record = cursor.fetchone()
        if record is None:
            return False
        else:
            return record

    def ViewAllGearboxTypes(self, cursor, connection):
        cursor.execute("SELECT * FROM GearboxType")
        return cursor.fetchall()
        
    @property
    def GearboxTypeName(self):
        return self.__Name
    
    @GearboxTypeName.setter
    def GearboxTypeName(self, Name):
        self.__Name = Name
