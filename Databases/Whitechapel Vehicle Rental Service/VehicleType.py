from ConnectionDB import ConnectionDB

MyConnection = ConnectionDB()
MyCursor = MyConnection.cursor()

MyCursor.execute("""CREATE TABLE IF NOT EXISTS VehicleType(
    VehicleTypeId INT AUTO_INCREMENT PRIMARY KEY,
    VehicleTypeName VARCHAR(30)
)""")

# print("VehicleType table created successfully!")

class VehicleType:
    def __init__(self, Name):
        self.__Name = Name
        
    def SaveVehicleType(self, cursor, connection):
        cursor.execute(
            "INSERT INTO VehicleType (VehicleTypeName) VALUES (%s)",
            (self.__Name,)
        )
        connection.commit()

    def UpdateVehicleType(self, cursor, connection, VehicleTypeName, NewVehicleTypeName):
        cursor.execute(
            "SELECT * FROM VehicleType WHERE VehicleTypeName = %s",
            (VehicleTypeName,)
        )
        record = cursor.fetchone()
    
        if record is None:
            return False
        else:
            cursor.execute(
                "UPDATE VehicleType SET VehicleTypeName = %s WHERE VehicleTypeName = %s",
                (NewVehicleTypeName, VehicleTypeName)
            )
            connection.commit()
            return True
        
    def DeleteVehicleType(self, cursor, connection, VehicleTypeId):
        cursor.execute(
            "DELETE FROM VehicleType WHERE VehicleTypeId = %s",
            (VehicleTypeId,)
        )
        connection.commit()
        return cursor.rowcount > 0
    
    def ViewVehicleType(self, cursor, connection, VehicleTypeName):
        cursor.execute(
            "SELECT * FROM VehicleType WHERE VehicleTypeName = %s",
            (VehicleTypeName,)
        )
        record = cursor.fetchone()
        if record is None:
            return False
        else:
            return record

    def ViewAllVehicleTypes(self, cursor, connection):
        cursor.execute("SELECT * FROM VehicleType")
        return cursor.fetchall()
        
    @property
    def VehicleTypeName(self):
        return self.__Name
    
    @VehicleTypeName.setter
    def VehicleTypeName(self, Name):
        self.__Name = Name
