from ConnectionDB import ConnectionDB

MyConnection = ConnectionDB()
MyCursor = MyConnection.cursor()

MyCursor.execute("""CREATE TABLE IF NOT EXISTS FuelType(
    FuelTypeId INT AUTO_INCREMENT PRIMARY KEY,
    FuelTypeName VARCHAR(30)
)""")

# print("FuelType table created successfully!")

class FuelType:
    def __init__(self, Name):
        self.__Name = Name
        
    def SaveFuelType(self, cursor, connection):
        cursor.execute(
            "INSERT INTO FuelType (FuelTypeName) VALUES (%s)",
            (self.__Name,)
        )
        connection.commit()

    def UpdateFuelType(self, cursor, connection, FuelTypeName, NewFuelTypeName):
        cursor.execute(
            "SELECT * FROM FuelType WHERE FuelTypeName = %s",
            (FuelTypeName,)
        )
        record = cursor.fetchone()

        if record is None:
            return False
        else:
            cursor.execute(
                "UPDATE FuelType SET FuelTypeName = %s WHERE FuelTypeName = %s",
                (NewFuelTypeName, FuelTypeName)
            )
            connection.commit()
            return True
        
    def DeleteFuelType(self, cursor, connection, FuelTypeId):
        cursor.execute(
            "DELETE FROM FuelType WHERE FuelTypeId = %s",
            (FuelTypeId,)
        )
        connection.commit()
        return cursor.rowcount > 0
    
    def ViewFuelType(self, cursor, connection, FuelTypeName):
        cursor.execute(
            "SELECT * FROM FuelType WHERE FuelTypeName = %s",
            (FuelTypeName,)
        )
        record = cursor.fetchone()
        if record is None:
            return False
        else:
            return record

    def ViewAllFuelTypes(self, cursor, connection):
        cursor.execute("SELECT * FROM FuelType")
        return cursor.fetchall()
        
    @property
    def FuelTypeName(self):
        return self.__Name
    
    @FuelTypeName.setter
    def FuelTypeName(self, Name):
        self.__Name = Name
