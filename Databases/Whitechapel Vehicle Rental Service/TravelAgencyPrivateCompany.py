from ConnectionDB import ConnectionDB

MyConnection = ConnectionDB()
MyCursor = MyConnection.cursor()

MyCursor.execute("""CREATE TABLE IF NOT EXISTS TravelAgencyPrivateCompany(
    TravelAgencyPrivateCompanyId INT AUTO_INCREMENT PRIMARY KEY,
    CustomerTypeId INT,
    CompanyName VARCHAR(70),
    Address VARCHAR(100),
    ContactNumber VARCHAR(15),
    ContactPerson VARCHAR(30),
    FOREIGN KEY (CustomerTypeId) REFERENCES CustomerType(CustomerTypeId)
)""")

# print("TravelAgencyPrivateCompany table created successfully!")

class TravelAgencyPrivateCompany:
    def __init__(self, CustomerTypeId, CompanyName, Address, ContactNumber, ContactPerson):
        self.__CustomerTypeId = CustomerTypeId
        self.__CompanyName = CompanyName
        self.__Address = Address
        self.__ContactNumber = ContactNumber
        self.__ContactPerson = ContactPerson

    def SaveTravelAgencyPrivateCompany(self, cursor, connection):
        cursor.execute(
            "SELECT CustomerTypeId FROM CustomerType WHERE CustomerTypeId = %s",
            (self.__CustomerTypeId,)
        )
        if cursor.fetchone() is None:
            return False

        cursor.execute(
            """INSERT INTO TravelAgencyPrivateCompany 
               (CustomerTypeId, CompanyName, Address, ContactNumber, ContactPerson)
               VALUES (%s, %s, %s, %s, %s)""",
            (self.__CustomerTypeId, self.__CompanyName, self.__Address, self.__ContactNumber, self.__ContactPerson)
        )
        connection.commit()
        return True

    def UpdateTravelAgencyPrivateCompany(self, cursor, connection, TravelAgencyPrivateCompanyId):
        cursor.execute(
            "SELECT * FROM TravelAgencyPrivateCompany WHERE TravelAgencyPrivateCompanyId = %s",
            (TravelAgencyPrivateCompanyId,)
        )
        Record = cursor.fetchone()

        if Record is None:
            return False
        else:
            CustomerTypeId = self.__CustomerTypeId if self.__CustomerTypeId != "" else Record[1]
            CompanyName = self.__CompanyName if self.__CompanyName != "" else Record[2]
            Address = self.__Address if self.__Address != "" else Record[3]
            ContactNumber = self.__ContactNumber if self.__ContactNumber != "" else Record[4]
            ContactPerson = self.__ContactPerson if self.__ContactPerson != "" else Record[5]

            cursor.execute(
                """UPDATE TravelAgencyPrivateCompany
                   SET CustomerTypeId = %s, CompanyName = %s, Address = %s,
                       ContactNumber = %s, ContactPerson = %s
                   WHERE TravelAgencyPrivateCompanyId = %s""",
                (CustomerTypeId, CompanyName, Address, ContactNumber, ContactPerson, TravelAgencyPrivateCompanyId)
            )
            connection.commit()
            return True

    def DeleteTravelAgencyPrivateCompany(self, cursor, connection, TravelAgencyPrivateCompanyId):
        cursor.execute(
            "SELECT * FROM TravelAgencyPrivateCompany WHERE TravelAgencyPrivateCompanyId = %s",
            (TravelAgencyPrivateCompanyId,)
        )
        Record = cursor.fetchone()

        if Record is None:
            return False

        cursor.execute(
            "DELETE FROM TravelAgencyPrivateCompany WHERE TravelAgencyPrivateCompanyId = %s",
            (TravelAgencyPrivateCompanyId,)
        )
        connection.commit()
        return True

    def ViewTravelAgencyPrivateCompanyById(self, cursor, connection, TravelAgencyPrivateCompanyId):
        cursor.execute(
            """SELECT TAPC.TravelAgencyPrivateCompanyId, CT.CustomerTypeName, TAPC.CompanyName, 
                      TAPC.Address, TAPC.ContactNumber, TAPC.ContactPerson
               FROM TravelAgencyPrivateCompany TAPC
               JOIN CustomerType CT ON TAPC.CustomerTypeId = CT.CustomerTypeId
               WHERE TAPC.TravelAgencyPrivateCompanyId = %s""",
            (TravelAgencyPrivateCompanyId,)
        )
        Record = cursor.fetchone()
        return Record if Record else False

    def ViewAllTravelAgencyPrivateCompanies(self, cursor, connection):
        cursor.execute(
            """SELECT TAPC.TravelAgencyPrivateCompanyId, CT.CustomerTypeName, TAPC.CompanyName, 
                      TAPC.Address, TAPC.ContactNumber, TAPC.ContactPerson
               FROM TravelAgencyPrivateCompany TAPC
               JOIN CustomerType CT ON TAPC.CustomerTypeId = CT.CustomerTypeId"""
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
    def CompanyName(self):
        return self.__CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self.__CompanyName = CompanyName
        

    @property
    def Address(self):
        return self.__Address

    @Address.setter
    def Address(self, Address):
        self.__Address = Address
        

    @property
    def ContactNumber(self):
        return self.__ContactNumber

    @ContactNumber.setter
    def ContactNumber(self, ContactNumber):
        self.__ContactNumber = ContactNumber
        

    @property
    def ContactPerson(self):
        return self.__ContactPerson

    @ContactPerson.setter
    def ContactPerson(self, ContactPerson):
        self.__ContactPerson = ContactPerson
