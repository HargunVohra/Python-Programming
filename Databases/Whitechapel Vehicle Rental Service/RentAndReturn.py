import datetime
import random
from ConnectionDB import ConnectionDB

MyConnection = ConnectionDB()
MyCursor = MyConnection.cursor()

MyCursor.execute("""CREATE TABLE IF NOT EXISTS RentAndReturn(
    RentAndReturnId INT AUTO_INCREMENT PRIMARY KEY,
    CustomerTypeId INT,
    CustomerName VARCHAR(70),
    Address VARCHAR(200),
    VehicleId INT,
    RentalDate DATE,
    ReturnDate DATE,
    NoOfDays VARCHAR(20),
    Rate INT,
    VAT INT,
    RentalServiceCost INT,
    RepairCost INT,
    Amount INT,
    AmountPaid INT,
    TotalDueAmount INT,
    PaymentConfirmation VARCHAR(10),
    PaymentMethod VARCHAR(20),
    InvoiceNo VARCHAR(30),
    ReceiptNo VARCHAR(30),
    FOREIGN KEY (CustomerTypeId) REFERENCES CustomerType(CustomerTypeId),
    FOREIGN KEY (VehicleId) REFERENCES Vehicles(VehicleId)
)""")

class RentAndReturn:
    def __init__(self, CustomerTypeId, CustomerName, Address, VehicleId, RentalDate, ReturnDate, NoOfDays, Rate, VAT, RentalServiceCost, RepairCost, Amount, AmountPaid, TotalDueAmount, PaymentConfirmation, PaymentMethod, InvoiceNo, ReceiptNo):
        self.__CustomerTypeId = CustomerTypeId
        self.__CustomerName = CustomerName
        self.__Address = Address
        self.__VehicleId = VehicleId
        self.__RentalDate = RentalDate
        self.__ReturnDate = ReturnDate
        self.__NoOfDays = NoOfDays
        self.__Rate = Rate
        self.__VAT = VAT
        self.__RentalServiceCost = RentalServiceCost
        self.__RepairCost = RepairCost
        self.__Amount = Amount
        self.__AmountPaid = AmountPaid
        self.__TotalDueAmount = TotalDueAmount
        self.__PaymentConfirmation = PaymentConfirmation
        self.__PaymentMethod = PaymentMethod
        self.__InvoiceNo = InvoiceNo
        self.__ReceiptNo = ReceiptNo

    def SaveRentAndReturn(self, cursor, connection, ReserveOnly="N"):
        cursor.execute("SELECT * FROM Vehicles WHERE VehicleId = %s", (self.__VehicleId,))
        Vehicle = cursor.fetchone()
        if Vehicle is None:
            return "InvalidVehicle"
        if Vehicle[16] == 'Y' or Vehicle[17] == 'Y':
            return "VehicleUnavailable"
    
        Number = str(random.randint(100000, 999999))
        if self.__CustomerTypeId in ["1", "2"]:
            self.__ReceiptNo = "REC-" + Number
            self.__InvoiceNo = None
        else:
            self.__InvoiceNo = "INV-" + Number
            self.__ReceiptNo = None
    
        cursor.execute(
            """INSERT INTO RentAndReturn 
               (CustomerTypeId, CustomerName, Address, VehicleId, RentalDate, ReturnDate, NoOfDays, Rate, VAT, RentalServiceCost, RepairCost, Amount, AmountPaid, TotalDueAmount, PaymentConfirmation, PaymentMethod, InvoiceNo, ReceiptNo)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (self.__CustomerTypeId, self.__CustomerName, self.__Address, self.__VehicleId,
             self.__RentalDate, self.__ReturnDate, self.__NoOfDays, self.__Rate, self.__VAT,
             self.__RentalServiceCost, self.__RepairCost, self.__Amount, self.__AmountPaid,
             self.__TotalDueAmount, self.__PaymentConfirmation, self.__PaymentMethod,
             self.__InvoiceNo, self.__ReceiptNo)
        )
    
        if self.__CustomerTypeId in ["3", "4"] and ReserveOnly == "Y":
            cursor.execute("UPDATE Vehicles SET IsReserved = 'Y' WHERE VehicleId = %s", (self.__VehicleId,))
        else:
            cursor.execute("UPDATE Vehicles SET IsRented = 'Y', IsReserved = 'N' WHERE VehicleId = %s", (self.__VehicleId,))
    
        connection.commit()
        return True

    def AutoReturnVehicle(self, cursor, connection):
        Today = datetime.date.today()
        cursor.execute("SELECT RentAndReturnId, VehicleId, ReturnDate FROM RentAndReturn")
        Records = cursor.fetchall()
        for Record in Records:
            if Record[2] and Record[2] <= Today:
                cursor.execute("UPDATE Vehicles SET IsRented = 'N', IsReserved = 'N' WHERE VehicleId = %s", (int(Record[1]),))
        connection.commit()
        
    def UpdateRentAndReturn(self, cursor, connection, RentAndReturnId):
        cursor.execute("SELECT * FROM RentAndReturn WHERE RentAndReturnId = %s", (RentAndReturnId,))
        Record = cursor.fetchone()
    
        if Record is None:
            return False
        else:
            CustomerTypeId = self.__CustomerTypeId if self.__CustomerTypeId != "" else Record[1]
            CustomerName = self.__CustomerName if self.__CustomerName != "" else Record[2]
            Address = self.__Address if self.__Address != "" else Record[3]
            VehicleId = self.__VehicleId if self.__VehicleId != "" else Record[4]
            RentalDate = self.__RentalDate if self.__RentalDate != "" else Record[5]
            ReturnDate = self.__ReturnDate if self.__ReturnDate != "" else Record[6]
            NoOfDays = self.__NoOfDays if self.__NoOfDays != "" else Record[7]
            Rate = self.__Rate if self.__Rate != "" else Record[8]
            VAT = self.__VAT if self.__VAT != "" else Record[9]
            RentalServiceCost = self.__RentalServiceCost if self.__RentalServiceCost != "" else Record[10]
            RepairCost = self.__RepairCost if self.__RepairCost != "" else Record[11]
            Amount = self.__Amount if self.__Amount != "" else Record[12]
            AmountPaid = self.__AmountPaid if self.__AmountPaid != "" else Record[13]
            TotalDueAmount = self.__TotalDueAmount if self.__TotalDueAmount != "" else Record[14]
            PaymentConfirmation = self.__PaymentConfirmation if self.__PaymentConfirmation != "" else Record[15]
            PaymentMethod = self.__PaymentMethod if self.__PaymentMethod != "" else Record[16]
            InvoiceNo = self.__InvoiceNo if self.__InvoiceNo != "" else Record[17]
            ReceiptNo = self.__ReceiptNo if self.__ReceiptNo != "" else Record[18]
    
            if RentalDate != "" and ReturnDate != "":
                Days = (datetime.datetime.strptime(str(ReturnDate), "%Y-%m-%d") -
                        datetime.datetime.strptime(str(RentalDate), "%Y-%m-%d")).days
                NoOfDays = str(Days)
                Amount = (int(Rate) * Days) + int(VAT) + int(RentalServiceCost) + int(RepairCost)
                TotalDueAmount = int(Amount) - int(AmountPaid)
    
            cursor.execute(
                """UPDATE RentAndReturn
                   SET CustomerTypeId = %s, CustomerName = %s, Address = %s, VehicleId = %s,
                       RentalDate = %s, ReturnDate = %s, NoOfDays = %s, Rate = %s, VAT = %s,
                       RentalServiceCost = %s, RepairCost = %s, Amount = %s, AmountPaid = %s,
                       TotalDueAmount = %s, PaymentConfirmation = %s, PaymentMethod = %s,
                       InvoiceNo = %s, ReceiptNo = %s
                   WHERE RentAndReturnId = %s""",
                (CustomerTypeId, CustomerName, Address, VehicleId, RentalDate, ReturnDate,
                 NoOfDays, Rate, VAT, RentalServiceCost, RepairCost, Amount, AmountPaid,
                 TotalDueAmount, PaymentConfirmation, PaymentMethod, InvoiceNo, ReceiptNo, RentAndReturnId)
            )
            connection.commit()
            return True
        
    def DeleteRentAndReturn(self, cursor, connection, RentAndReturnId):
        cursor.execute("SELECT * FROM RentAndReturn WHERE RentAndReturnId = %s", (RentAndReturnId,))
        record = cursor.fetchone()
        if record is None:
            return False

        cursor.execute("DELETE FROM RentAndReturn WHERE RentAndReturnId = %s", (RentAndReturnId,))
        connection.commit()
        return True


    def ViewRentAndReturnById(self, cursor, connection, RentAndReturnId):
        cursor.execute(
            """SELECT R.RentAndReturnId,
                      C.CustomerTypeName,
                      R.CustomerName,
                      R.Address,
                      V.RegistrationNumber,
                      R.RentalDate,
                      R.ReturnDate,
                      R.NoOfDays,
                      R.Rate,
                      R.VAT,
                      R.RentalServiceCost,
                      R.RepairCost,
                      R.Amount,
                      R.AmountPaid,
                      R.TotalDueAmount,
                      R.PaymentConfirmation,
                      R.PaymentMethod,
                      R.InvoiceNo,
                      R.ReceiptNo
               FROM RentAndReturn R
               JOIN CustomerType C ON R.CustomerTypeId = C.CustomerTypeId
               JOIN Vehicles V ON R.VehicleId = V.VehicleId
               WHERE R.RentAndReturnId = %s""",
            (RentAndReturnId,)
        )
        record = cursor.fetchone()
        return record if record else False


    def ViewAllRentAndReturn(self, cursor, connection):
        cursor.execute(
            """SELECT R.RentAndReturnId,
                      C.CustomerTypeName,
                      R.CustomerName,
                      R.Address,
                      V.RegistrationNumber,
                      R.RentalDate,
                      R.ReturnDate,
                      R.NoOfDays,
                      R.Rate,
                      R.VAT,
                      R.RentalServiceCost,
                      R.RepairCost,
                      R.Amount,
                      R.AmountPaid,
                      R.TotalDueAmount,
                      R.PaymentConfirmation,
                      R.PaymentMethod,
                      R.InvoiceNo,
                      R.ReceiptNo
               FROM RentAndReturn R
               JOIN CustomerType C ON R.CustomerTypeId = C.CustomerTypeId
               JOIN Vehicles V ON R.VehicleId = V.VehicleId"""
        )
        return cursor.fetchall()
    
    def PrintReceiptInvoice(self, cursor, RentAndReturnId):
        cursor.execute(
            """SELECT RentAndReturnId, CustomerTypeId, CustomerName, Address, VehicleId,
                      RentalDate, ReturnDate, NoOfDays, Rate, VAT, RentalServiceCost,
                      RepairCost, Amount, AmountPaid, TotalDueAmount, PaymentMethod,
                      InvoiceNo, ReceiptNo
               FROM RentAndReturn
               WHERE RentAndReturnId = %s""",
            (RentAndReturnId,)
        )
        Record = cursor.fetchone()
        if Record is None:
            return None
    
        return {
            "RentAndReturnId": Record[0],
            "CustomerTypeId": Record[1],
            "CustomerName": Record[2],
            "Address": Record[3],
            "VehicleId": Record[4],
            "RentalDate": Record[5],
            "ReturnDate": Record[6],
            "NoOfDays": Record[7],
            "Rate": Record[8],
            "VAT": Record[9],
            "RentalServiceCost": Record[10],
            "RepairCost": Record[11],
            "Amount": Record[12],
            "AmountPaid": Record[13],
            "TotalDueAmount": Record[14],
            "PaymentMethod": Record[15],
            "InvoiceNo": Record[16],
            "ReceiptNo": Record[17],
        }

    @property
    def CustomerTypeId(self):
        return self.__CustomerTypeId
    
    @CustomerTypeId.setter
    def CustomerTypeId(self, CustomerTypeId):
        self.__CustomerTypeId = CustomerTypeId
        

    @property
    def CustomerName(self):
        return self.__CustomerName
    
    @CustomerName.setter
    def CustomerName(self, CustomerName):
        self.__CustomerName = CustomerName
        

    @property
    def Address(self):
        return self.__Address
    
    @Address.setter
    def Address(self, Address):
        self.__Address = Address
        

    @property
    def VehicleTypeId(self):
        return self.__VehicleTypeId
    
    @VehicleTypeId.setter
    def VehicleTypeId(self, VehicleTypeId):
        self.__VehicleTypeId = VehicleTypeId
        
        
    @property
    def RentalDate(self):
        return self.__RentalDate
    
    @RentalDate.setter
    def RentalDate(self, RentalDate):
        self.__RentalDate = RentalDate
        

    @property
    def ReturnDate(self):
        return self.__ReturnDate
    
    @ReturnDate.setter
    def ReturnDate(self, ReturnDate):
        self.__ReturnDate = ReturnDate
        

    @property
    def NoOfDays(self):
        return self.__NoOfDays
    
    @NoOfDays.setter
    def NoOfDays(self, NoOfDays):
        self.__NoOfDays = NoOfDays
        

    @property
    def Rate(self):
        return self.__Rate
    
    @Rate.setter
    def Rate(self, Rate):
        self.__Rate = Rate
        

    @property
    def VAT(self):
        return self.__VAT
    
    @VAT.setter
    def VAT(self, VAT):
        self.__VAT = VAT
        

    @property
    def RentalServiceCost(self):
        return self.__RentalServiceCost
    
    @RentalServiceCost.setter
    def RentalServiceCost(self, RentalServiceCost):
        self.__RentalServiceCost = RentalServiceCost
        

    @property
    def RepairCost(self):
        return self.__RepairCost
    
    @RepairCost.setter
    def RepairCost(self, RepairCost):
        self.__RepairCost = RepairCost
        

    @property
    def Amount(self):
        return self.__Amount
    
    @Amount.setter
    def Amount(self, Amount):
        self.__Amount = Amount
        

    @property
    def AmountPaid(self):
        return self.__AmountPaid
    
    @AmountPaid.setter
    def AmountPaid(self, AmountPaid):
        self.__AmountPaid = AmountPaid
        

    @property
    def TotalDueAmount(self):
        return self.__TotalDueAmount
    
    @TotalDueAmount.setter
    def TotalDueAmount(self, TotalDueAmount):
        self.__TotalDueAmount = TotalDueAmount
        

    @property
    def PaymentConfirmation(self):
        return self.__PaymentConfirmation
    
    @PaymentConfirmation.setter
    def PaymentConfirmation(self, PaymentConfirmation):
        self.__PaymentConfirmation = PaymentConfirmation
        

    @property
    def PaymentMethod(self):
        return self.__PaymentMethod
    
    @PaymentMethod.setter
    def PaymentMethod(self, PaymentMethod):
        self.__PaymentMethod = PaymentMethod
        

    @property
    def InvoiceNo(self):
        return self.__InvoiceNo
    
    @InvoiceNo.setter
    def InvoiceNo(self, InvoiceNo):
        self.__InvoiceNo = InvoiceNo
        

    @property
    def ReceiptNo(self):
        return self.__ReceiptNo
    
    @ReceiptNo.setter
    def ReceiptNo(self, ReceiptNo):
        self.__ReceiptNo = ReceiptNo
