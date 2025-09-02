from ConnectionDB import ConnectionDB

MyConnection = ConnectionDB()
MyCursor = MyConnection.cursor()

MyCursor.execute("""CREATE TABLE IF NOT EXISTS Vehicles(
    VehicleId INT AUTO_INCREMENT PRIMARY KEY,
    VehicleTypeName VARCHAR(30),
    GearboxTypeId INT,
    FuelTypeId INT,
    RegistrationNumber VARCHAR(15),
    EngineSize VARCHAR(20),
    Colour VARCHAR(20),
    Model VARCHAR(30),
    Make VARCHAR(20),
    CurrentMileage VARCHAR(20),
    NumberOfDoors VARCHAR (10),
    SafetyInformation VARCHAR(200),
    Length VARCHAR(10),
    Width VARCHAR(10),
    Height VARCHAR(10),
    OnService VARCHAR(5),
    IsReserved VARCHAR(5),
    IsRented VARCHAR(5),
    FOREIGN KEY (VehicleTypeId) REFERENCES VehicleType(VehicleTypeId),
    FOREIGN KEY (GearboxTypeId) REFERENCES GearboxType(GearboxTypeId),
    FOREIGN KEY (FuelTypeId) REFERENCES FuelType(FuelTypeId)
    )""")

# print("Vehicle table created successfully!")

class Vehicle:
    def __init__(self, VehicleTypeId, GearboxTypeId, FuelTypeId, RegistrationNumber, EngineSize, Colour, Model, Make, CurrentMileage, NumberOfDoors, SafetyInformation, Length, Width, Height, OnService, IsReserved, IsRented):
        self.__VehicleTypeId = VehicleTypeId
        self.__GearboxTypeId = GearboxTypeId
        self.__FuelTypeId = FuelTypeId
        self.__RegistrationNumber = RegistrationNumber
        self.__EngineSize = EngineSize
        self.__Colour = Colour
        self.__Model = Model
        self.__Make = Make
        self.__CurrentMileage = CurrentMileage
        self.__NumberOfDoors = NumberOfDoors
        self.__SafetyInformation = SafetyInformation
        self.__Length = Length
        self.__Width = Width
        self.__Height = Height
        self.__OnService = OnService
        self.__IsReserved = IsReserved
        self.__IsRented = IsRented
        
    def SaveVehicle(self, cursor, connection):
        cursor.execute("SELECT VehicleTypeId FROM VehicleType WHERE VehicleTypeId = %s", (self.__VehicleTypeId,))
        record = cursor.fetchone()
        if record is None:
            return False
        
        cursor.execute("SELECT GearboxTypeId FROM GearboxType WHERE GearboxTypeId = %s", (self.__GearboxTypeId,))
        record = cursor.fetchone()
        if record is None:
            return False
        
        cursor.execute("SELECT FuelTypeId FROM FuelType WHERE FuelTypeId = %s", (self.__FuelTypeId,))
        record = cursor.fetchone()
        if record is None:
            return False

        IsReserved = 'N' if self.__OnService == 'Y' else self.__IsReserved
        IsRented = 'N' if self.__OnService == 'Y' else self.__IsRented
        
        cursor.execute(
            """INSERT INTO Vehicles 
               (VehicleTypeId, GearboxTypeId, FuelTypeId, RegistrationNumber, EngineSize, Colour, Model, Make, CurrentMileage, NumberOfDoors, SafetyInformation, Length, Width, Height, OnService, IsReserved, IsRented)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (self.__VehicleTypeId, self.__GearboxTypeId, self.__FuelTypeId, self.__RegistrationNumber, self.__EngineSize, self.__Colour, self.__Model, self.__Make, self.__CurrentMileage, self.__NumberOfDoors, self.__SafetyInformation, self.__Length, self.__Width, self.__Height, self.__OnService, IsReserved, IsRented)
        )
        connection.commit()
        return True
    
    def UpdateVehicle(self, cursor, connection, RegistrationNumber):
        cursor.execute("SELECT * FROM Vehicles WHERE RegistrationNumber = %s", (RegistrationNumber,))
        Record = cursor.fetchone()
    
        if Record is None:
            return False
        else:
            VehicleTypeId = self.__VehicleTypeId if self.__VehicleTypeId != "" else Record[1]
            GearboxTypeId = self.__GearboxTypeId if self.__GearboxTypeId != "" else Record[2]
            FuelTypeId = self.__FuelTypeId if self.__FuelTypeId != "" else Record[3]
            EngineSize = self.__EngineSize if self.__EngineSize != "" else Record[5]
            Colour = self.__Colour if self.__Colour != "" else Record[6]
            Model = self.__Model if self.__Model != "" else Record[7]
            Make = self.__Make if self.__Make != "" else Record[8]
            CurrentMileage = self.__CurrentMileage if self.__CurrentMileage != "" else Record[9]
            NumberOfDoors = self.__NumberOfDoors if self.__NumberOfDoors != "" else Record[10]
            SafetyInformation = self.__SafetyInformation if self.__SafetyInformation != "" else Record[11]
            Length = self.__Length if self.__Length != "" else Record[12]
            Width = self.__Width if self.__Width != "" else Record[13]
            Height = self.__Height if self.__Height != "" else Record[14]
            OnService = self.__OnService if self.__OnService != "" else Record[15]

            if OnService == 'Y':
                IsReserved = 'N'
                IsRented = 'N'
            else:
                IsReserved = self.__IsReserved if self.__IsReserved != "" else Record[16]
                IsRented = self.__IsRented if self.__IsRented != "" else Record[17]
    
            cursor.execute("SELECT VehicleTypeId FROM VehicleType WHERE VehicleTypeId = %s", (VehicleTypeId,))
            if cursor.fetchone() is None:
                return False
    
            cursor.execute("SELECT GearboxTypeId FROM GearboxType WHERE GearboxTypeId = %s", (GearboxTypeId,))
            if cursor.fetchone() is None:
                return False
    
            cursor.execute("SELECT FuelTypeId FROM FuelType WHERE FuelTypeId = %s", (FuelTypeId,))
            if cursor.fetchone() is None:
                return False
    
            cursor.execute(
                """UPDATE Vehicles
                   SET VehicleTypeId = %s, GearboxTypeId = %s, FuelTypeId = %s, EngineSize = %s,
                       Colour = %s, Model = %s, Make = %s, CurrentMileage = %s, NumberOfDoors = %s,
                       SafetyInformation = %s, Length = %s, Width = %s, Height = %s,
                       OnService = %s, IsReserved = %s, IsRented = %s
                   WHERE RegistrationNumber = %s""",
                (VehicleTypeId, GearboxTypeId, FuelTypeId, EngineSize, Colour, Model, Make,
                 CurrentMileage, NumberOfDoors, SafetyInformation, Length, Width, Height,
                 OnService, IsReserved, IsRented, RegistrationNumber)
            )
            connection.commit()
            return True
            
    def DeleteVehicle(self, cursor, connection, VehicleId):
        cursor.execute("SELECT * FROM Vehicles WHERE VehicleId = %s", (VehicleId,))
        record = cursor.fetchone()
        if record is None:
            return False
        cursor.execute("DELETE FROM Vehicles WHERE VehicleId = %s", (VehicleId,))
        connection.commit()
        return True
    
    def ViewVehicleById(self, cursor, connection, VehicleId):
        cursor.execute(
            """SELECT V.VehicleId, 
                      VT.VehicleTypeName, 
                      GT.GearboxTypeName, 
                      FT.FuelTypeName, 
                      V.RegistrationNumber, 
                      V.EngineSize, 
                      V.Colour, 
                      V.Model, 
                      V.Make, 
                      V.CurrentMileage, 
                      V.NumberOfDoors, 
                      V.SafetyInformation, 
                      V.Length, 
                      V.Width, 
                      V.Height, 
                      V.OnService,
                      V.IsReserved, 
                      V.IsRented
               FROM Vehicles V
               JOIN VehicleType VT ON V.VehicleTypeId = VT.VehicleTypeId
               JOIN GearboxType GT ON V.GearboxTypeId = GT.GearboxTypeId
               JOIN FuelType FT ON V.FuelTypeId = FT.FuelTypeId
               WHERE V.VehicleId = %s""",
            (VehicleId,)
        )
        record = cursor.fetchone()
        if record is None:
            return False
        else:
            return record

    def ViewAllVehicles(self, cursor, connection):
        cursor.execute(
            """SELECT V.VehicleId, 
                      VT.VehicleTypeName, 
                      GT.GearboxTypeName, 
                      FT.FuelTypeName, 
                      V.RegistrationNumber, 
                      V.EngineSize, 
                      V.Colour, 
                      V.Model, 
                      V.Make, 
                      V.CurrentMileage, 
                      V.NumberOfDoors, 
                      V.SafetyInformation, 
                      V.Length, 
                      V.Width, 
                      V.Height, 
                      V.OnService,
                      V.IsReserved, 
                      V.IsRented
               FROM Vehicles V
               JOIN VehicleType VT ON V.VehicleTypeId = VT.VehicleTypeId
               JOIN GearboxType GT ON V.GearboxTypeId = GT.GearboxTypeId
               JOIN FuelType FT ON V.FuelTypeId = FT.FuelTypeId"""
        )
        return cursor.fetchall()
        
    @property
    def VehicleTypeId(self):
        return self.__VehicleTypeId
    
    @VehicleTypeId.setter
    def VehicleTypeId(self, VehicleTypeId):
        self.__VehicleTypeId = VehicleTypeId
        
        
    @property
    def GearboxTypeId(self):
        return self.__GearboxTypeId
    
    @GearboxTypeId.setter
    def GearboxTypeId(self, GearboxTypeId):
        self.__GearboxTypeId = GearboxTypeId
        
        
    @property
    def FuelTypeId(self):
        return self.__FuelTypeId
    
    @FuelTypeId.setter
    def FuelTypeId(self, FuelTypeId):
        self.__FuelTypeId = FuelTypeId
        
        
    @property
    def RegistrationNumber(self):
        return self.__RegistrationNumber
    
    @RegistrationNumber.setter
    def RegistrationNumber(self, RegistrationNumber):
        self.__RegistrationNumber = RegistrationNumber
        
        
    @property
    def EngineSize(self):
        return self.__EngineSize
    
    @EngineSize.setter
    def EngineSize(self, EngineSize):
        self.__EngineSize = EngineSize
        
        
    @property
    def Colour(self):
        return self.__Colour
    
    @Colour.setter
    def Colour(self, Colour):
        self.__Colour = Colour
        
        
    @property
    def Model(self):
        return self.__Model
    
    @Model.setter
    def Model(self, Model):
        self.__Model = Model
        
        
    @property
    def Make(self):
        return self.__Make
    
    @Make.setter
    def Make(self, Make):
        self.__Make = Make
        
        
    @property
    def CurrentMileage(self):
        return self.__CurrentMileage
    
    @CurrentMileage.setter
    def CurrentMileage(self, CurrentMileage):
        self.__CurrentMileage = CurrentMileage
        
        
    @property
    def NumberOfDoors(self):
        return self.__NumberOfDoors
    
    @NumberOfDoors.setter
    def NumberOfDoors(self, NumberOfDoors):
        self.__NumberOfDoors = NumberOfDoors
        
        
    @property
    def SafetyInformation(self):
        return self.__SafetyInformation
    
    @SafetyInformation.setter
    def SafetyInformation(self, SafetyInformation):
        self.__SafetyInformation = SafetyInformation
        
        
    @property
    def Length(self):
        return self.__Length
    
    @Length.setter
    def Length(self, Length):
        self.__Length = Length
        
        
    @property
    def Width(self):
        return self.__Width
    
    @Width.setter
    def Width(self, Width):
        self.__Width = Width
        
        
    @property
    def Height(self):
        return self.__Height
    
    @Height.setter
    def Height(self, Height):
        self.__Height = Height
        
        
    @property
    def OnService(self):
        return self.__OnService
    
    @OnService.setter
    def OnService(self, OnService):
        self.__OnService = OnService
        
        
    @property
    def IsReserved(self):
        return self.__IsReserved
    
    @IsReserved.setter
    def IsReserved(self, IsReserved):
        self.__IsReserved = IsReserved
        
        
    @property
    def IsRented(self):
        return self.__IsRented
    
    @IsRented.setter
    def IsRented(self, IsRented):
        self.__IsRented = IsRented
