from ConnectionDB import ConnectionDB

MyConnection = ConnectionDB()

MyCursor = MyConnection.cursor()
MyCursor.execute("""CREATE TABLE IF NOT EXISTS ServiceHistory(
    ServiceHistoryId INT AUTO_INCREMENT PRIMARY KEY,
    VehicleId INT,
    ServiceType VARCHAR(50),
    Cost VARCHAR(10),
    DateOfService DATE,
    DateOfReturn DATE,
    FOREIGN KEY (VehicleId) REFERENCES Vehicles(VehicleId)
    )""")

# print("Service history table created successfully!")

class ServiceHistory:
    def __init__(self, VehicleId, ServiceType, Cost, DateOfService, DateOfReturn):
        self.__VehicleId = VehicleId
        self.__ServiceType = ServiceType
        self.__Cost = Cost
        self.__DateOfService = DateOfService
        self.__DateOfReturn = DateOfReturn
        
    def SaveServiceHistory(self, cursor, connection):
        cursor.execute(
            "SELECT VehicleId FROM Vehicles WHERE VehicleId = %s",
            (self.__VehicleId,)
        )
        record = cursor.fetchone()
    
        if record is None:
            return False
    
        cursor.execute(
            """INSERT INTO ServiceHistory (VehicleId, ServiceType, Cost, DateOfService, DateOfReturn)
               VALUES (%s, %s, %s, %s, %s)""",
            (self.__VehicleId, self.__ServiceType, self.__Cost, self.__DateOfService, self.__DateOfReturn)
        )
        connection.commit()
        return True
    
    def UpdateServiceHistory(self, cursor, connection, ServiceHistoryId):
        cursor.execute(
            "SELECT * FROM ServiceHistory WHERE ServiceHistoryId = %s",
            (ServiceHistoryId,)
        )
        Record = cursor.fetchone()
    
        if Record is None:
            return False
        else:
            VehicleId = self.__VehicleId if self.__VehicleId != "" else Record[1]
            ServiceType = self.__ServiceType if self.__ServiceType != "" else Record[2]
            Cost = self.__Cost if self.__Cost != "" else Record[3]
            DateOfService = self.__DateOfService if self.__DateOfService != "" else Record[4]
            DateOfReturn = self.__DateOfReturn if self.__DateOfReturn != "" else Record[5]
    
            cursor.execute("SELECT VehicleId FROM Vehicles WHERE VehicleId = %s", (VehicleId,))
            if cursor.fetchone() is None:
                return False
    
            cursor.execute(
                """UPDATE ServiceHistory
                   SET VehicleId = %s, ServiceType = %s, Cost = %s, DateOfService = %s, DateOfReturn = %s
                   WHERE ServiceHistoryId = %s""",
                (VehicleId, ServiceType, Cost, DateOfService, DateOfReturn, ServiceHistoryId)
            )
            connection.commit()
            return True
        
    def DeleteServiceHistory(self, cursor, connection, ServiceHistoryId):
        cursor.execute(
            "DELETE FROM ServiceHistory WHERE ServiceHistoryId = %s",
            (ServiceHistoryId,)
        )
        connection.commit()
        return cursor.rowcount > 0
    
    def ViewServiceHistoryByVehicle(self, cursor, connection, VehicleModel):
        cursor.execute(
            """SELECT SH.ServiceHistoryId, 
                      V.Model, 
                      V.Make, 
                      SH.ServiceType, 
                      SH.Cost, 
                      SH.DateOfService, 
                      SH.DateOfReturn
               FROM ServiceHistory SH
               JOIN Vehicles V ON SH.VehicleId = V.VehicleId
               WHERE V.Model = %s""",
            (VehicleModel,)
        )
        records = cursor.fetchall()
        if not records:
            return False
        else:
            return records

    def ViewAllServiceHistories(self, cursor, connection):
        cursor.execute(
            """SELECT SH.ServiceHistoryId, 
                      V.Model, 
                      SH.ServiceType, 
                      SH.Cost, 
                      SH.DateOfService, 
                      SH.DateOfReturn
               FROM ServiceHistory SH
               JOIN Vehicles V ON SH.VehicleId = V.VehicleId"""
        )
        return cursor.fetchall()

    @property
    def VehicleId(self):
        return self.__VehicleId
    
    @VehicleId.setter
    def VehicleId(self, VehicleId):
        self.__VehicleId = VehicleId
        

    @property
    def ServiceType(self):
        return self.__ServiceType
    
    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self.__ServiceType = ServiceType
        

    @property
    def Cost(self):
        return self.__Cost
    
    @Cost.setter
    def Cost(self, Cost):
        self.__Cost = Cost
        

    @property
    def DateOfService(self):
        return self.__DateOfService
    
    @DateOfService.setter
    def DateOfService(self, DateOfService):
        self.__DateOfService = DateOfService
        

    @property
    def DateOfReturn(self):
        return self.__DateOfReturn
    
    @DateOfReturn.setter
    def DateOfReturn(self, DateOfReturn):
        self.__DateOfReturn = DateOfReturn
