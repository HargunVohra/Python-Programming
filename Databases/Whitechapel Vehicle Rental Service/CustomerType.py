from ConnectionDB import ConnectionDB

MyConnection = ConnectionDB()
MyCursor = MyConnection.cursor()

MyCursor.execute("""CREATE TABLE IF NOT EXISTS CustomerType(
    CustomerTypeId INT AUTO_INCREMENT PRIMARY KEY,
    CustomerTypeName VARCHAR(30)
)""")

# print("CustomerType table created successfully!")

class CustomerType:
    def __init__(self, Name):
        self.__Name = Name
        
    def SaveCustomerType(self, cursor, connection):
        cursor.execute(
            "INSERT INTO CustomerType (CustomerTypeName) VALUES (%s)",
            (self.__Name,)
        )
        connection.commit()

    def UpdateCustomerType(self, cursor, connection, CustomerTypeName, NewCustomerTypeName):
        cursor.execute(
            "SELECT * FROM CustomerType WHERE CustomerTypeName = %s",
            (CustomerTypeName,)
        )
        record = cursor.fetchone()

        if record is None:
            return False
        else:
            cursor.execute(
                "UPDATE CustomerType SET CustomerTypeName = %s WHERE CustomerTypeName = %s",
                (NewCustomerTypeName, CustomerTypeName)
            )
            connection.commit()
            return True
        
    def DeleteCustomerType(self, cursor, connection, CustomerTypeId):
        cursor.execute(
            "DELETE FROM CustomerType WHERE CustomerTypeId = %s",
            (CustomerTypeId,)
        )
        connection.commit()
        return cursor.rowcount > 0
    
    def ViewCustomerType(self, cursor, connection, CustomerTypeName):
        cursor.execute(
            "SELECT * FROM CustomerType WHERE CustomerTypeName = %s",
            (CustomerTypeName,)
        )
        record = cursor.fetchone()
        if record is None:
            return False
        else:
            return record

    def ViewAllCustomerTypes(self, cursor, connection):
        cursor.execute("SELECT * FROM CustomerType")
        return cursor.fetchall()
        
    @property
    def CustomerTypeName(self):
        return self.__Name
    
    @CustomerTypeName.setter
    def CustomerTypeName(self, Name):
        self.__Name = Name
