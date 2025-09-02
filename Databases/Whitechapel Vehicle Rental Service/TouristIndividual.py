from ConnectionDB import ConnectionDB

MyConnection = ConnectionDB()
MyCursor = MyConnection.cursor()

MyCursor.execute("""CREATE TABLE IF NOT EXISTS TouristIndividual(
    TouristIndividualId INT AUTO_INCREMENT PRIMARY KEY,
    CustomerTypeId INT,
    FullName VARCHAR(50),
    DrivingLicense VARCHAR(18),
    DateOfBirth DATE,
    Address VARCHAR(100),
    EmergencyContact VARCHAR(15),
    FOREIGN KEY (CustomerTypeId) REFERENCES CustomerType(CustomerTypeId)
)""")

# print("TouristIndividual table created successfully!")

class TouristIndividual:
    def __init__(self, CustomerTypeId, FullName, DrivingLicense, DateOfBirth, Address, EmergencyContact):
        self.__CustomerTypeId = CustomerTypeId
        self.__FullName = FullName
        self.__DrivingLicense = DrivingLicense
        self.__DateOfBirth = DateOfBirth
        self.__Address = Address
        self.__EmergencyContact = EmergencyContact

    def SaveTouristIndividual(self, cursor, connection):
        cursor.execute(
            "SELECT CustomerTypeId FROM CustomerType WHERE CustomerTypeId = %s",
            (self.__CustomerTypeId,)
        )
        if cursor.fetchone() is None:
            return False

        cursor.execute(
            """INSERT INTO TouristIndividual 
               (CustomerTypeId, FullName, DrivingLicense, DateOfBirth, Address, EmergencyContact)
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (self.__CustomerTypeId, self.__FullName, self.__DrivingLicense, self.__DateOfBirth,
             self.__Address, self.__EmergencyContact)
        )
        connection.commit()
        return True
    
    def UpdateTouristIndividual(self, cursor, connection, TouristIndividualId):
        cursor.execute(
            "SELECT * FROM TouristIndividual WHERE TouristIndividualId = %s",
            (TouristIndividualId,)
        )
        Record = cursor.fetchone()
    
        if Record is None:
            return False
        else:
            CustomerTypeId = self.__CustomerTypeId if self.__CustomerTypeId != "" else Record[1]
            FullName = self.__FullName if self.__FullName != "" else Record[2]
            DrivingLicense = self.__DrivingLicense if self.__DrivingLicense != "" else Record[3]
            DateOfBirth = self.__DateOfBirth if self.__DateOfBirth != "" else Record[4]
            Address = self.__Address if self.__Address != "" else Record[5]
            EmergencyContact = self.__EmergencyContact if self.__EmergencyContact != "" else Record[6]
    
            cursor.execute(
                """UPDATE TouristIndividual 
                   SET CustomerTypeId = %s, FullName = %s, DrivingLicense = %s, DateOfBirth = %s, 
                       Address = %s, EmergencyContact = %s
                   WHERE TouristIndividualId = %s""",
                (CustomerTypeId, FullName, DrivingLicense, DateOfBirth, Address, EmergencyContact, TouristIndividualId)
            )
            connection.commit()
            return True
        
    def DeleteTouristIndividual(self, cursor, connection, TouristIndividualId):
        cursor.execute(
            "SELECT * FROM TouristIndividual WHERE TouristIndividualId = %s",
            (TouristIndividualId,)
        )
        Record = cursor.fetchone()
    
        if Record is None:
            return False
    
        cursor.execute(
            "DELETE FROM TouristIndividual WHERE TouristIndividualId = %s",
            (TouristIndividualId,)
        )
        connection.commit()
        return True
    
    def ViewTouristIndividualById(self, cursor, connection, TouristIndividualId):
        cursor.execute(
            """SELECT TI.TouristIndividualId, CT.CustomerTypeName, TI.FullName, TI.DrivingLicense,
                      TI.DateOfBirth, TI.Address, TI.EmergencyContact
               FROM TouristIndividual TI
               JOIN CustomerType CT ON TI.CustomerTypeId = CT.CustomerTypeId
               WHERE TI.TouristIndividualId = %s""",
            (TouristIndividualId,)
        )
        Record = cursor.fetchone()
        return Record if Record else False
        
    def ViewAllTouristIndividuals(self, cursor, connection):
        cursor.execute(
            """SELECT TI.TouristIndividualId, CT.CustomerTypeName, TI.FullName, TI.DrivingLicense,
                      TI.DateOfBirth, TI.Address, TI.EmergencyContact
               FROM TouristIndividual TI
               JOIN CustomerType CT ON TI.CustomerTypeId = CT.CustomerTypeId"""
        )
        Records = cursor.fetchall()
        return Records if Records else False

    @property
    def CustomerTypeId(self):
        return self.__CustomerTypeId
    @CustomerTypeId.setter
    def CustomerTypeId(self, CustomerTypeId):
        self.__CustomerTypeId = CustomerTypeId

    @property
    def FullName(self):
        return self.__FullName
    @FullName.setter
    def FullName(self, FullName):
        self.__FullName = FullName

    @property
    def DrivingLicense(self):
        return self.__DrivingLicense
    @DrivingLicense.setter
    def DrivingLicense(self, DrivingLicense):
        self.__DrivingLicense = DrivingLicense

    @property
    def DateOfBirth(self):
        return self.__DateOfBirth
    @DateOfBirth.setter
    def DateOfBirth(self, DateOfBirth):
        self.__DateOfBirth = DateOfBirth

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address):
        self.__Address = Address

    @property
    def EmergencyContact(self):
        return self.__EmergencyContact
    @EmergencyContact.setter
    def EmergencyContact(self, EmergencyContact):
        self.__EmergencyContact = EmergencyContact
