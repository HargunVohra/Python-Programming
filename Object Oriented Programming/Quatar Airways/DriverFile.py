import Customer
import Flight
from tabulate import tabulate
import pickle
import os

def SaveCustomers(Customers):
    FilePath = input("Enter directory path to save the Customers file: ")
    FileName = input("Enter Customers file name (without extension): ")
    SavePath = os.path.join(FilePath, FileName + ".bin")
    if os.path.exists(SavePath):
        with open(SavePath, "rb") as fr:
            ExistingCustomers = pickle.load(fr)
        ExistingCustomers.extend(Customers)
        Customers = ExistingCustomers
    with open(SavePath, "wb") as fw:
        pickle.dump(Customers, fw)
    print("Customers data saved successfully!")

def SaveFlights(Flights):
    FilePath = input("Enter directory path to save the Flights file: ")
    FileName = input("Enter Flights file name (without extension): ")
    SavePath = os.path.join(FilePath, FileName + ".bin")
    if os.path.exists(SavePath):
        with open(SavePath, "rb") as fr:
            ExistingFlights = pickle.load(fr)
        ExistingFlights.extend(Flights)
        Flights = ExistingFlights
    with open(SavePath, "wb") as fw:
        pickle.dump(Flights, fw)
    print("Flights data saved successfully!")

def SaveBookings(Bookings):
    FilePath = input("Enter directory path to save the Bookings file: ")
    FileName = input("Enter Bookings file name (without extension): ")
    SavePath = os.path.join(FilePath, FileName + ".bin")
    if os.path.exists(SavePath):
        with open(SavePath, "rb") as fr:
            ExistingBookings = pickle.load(fr)
        ExistingBookings.extend(Bookings)
        Bookings = ExistingBookings
    with open(SavePath, "wb") as fw:
        pickle.dump(Bookings, fw)
    print("Bookings data saved successfully!")

def LoadList(FileDescription):
    FilePath = input("Enter directory path where the " + FileDescription + " file is located: ")
    FileName = input("Enter " + FileDescription + " file name (without extension): ")
    FullPath = os.path.join(FilePath, FileName + ".bin")
    if os.path.exists(FullPath):
        with open(FullPath, "rb") as fr:
            DataList = pickle.load(fr)
        print(FileDescription + " data loaded successfully!")
        if len(DataList) > 0:
            if FileDescription == "Customers":
                table_data = [[cust.CustomerName, cust.Address, cust.PassengerCode, cust.MealPreference] for cust in DataList]
                print(tabulate(table_data, headers=["Customer Name", "Address", "Passenger Code", "Meal Preference"]))
            elif FileDescription == "Flights":
                table_data = [[fl.FlightNumber, fl.FlightName, fl.StartPoint, fl.EndPoint, fl.StartDateTime, fl.EndDateTime, fl.TotalSeats, fl.SeatsBooked] for fl in DataList]
                print(tabulate(table_data, headers=["Flight Number", "Flight Name", "Start Point", "End Point", "Start DateTime", "End DateTime", "Total Seats", "Seats Booked"]))
            elif FileDescription == "Bookings":
                table_data = [[bk["PassengerCode"], bk["FlightNumber"]] for bk in DataList]
                print(tabulate(table_data, headers=["Passenger Code", "Flight Number"]))
        else:
            print("No data found in file!")
        return DataList
    else:
        print("File does not exist!")
        return []

def main():
    Customers = []
    Flights = []
    Bookings = []
    
    while True:
        print()
        print("--------------- Welcome to Qatar Airways ----------------")
        print()
        print("1. Add Customer")
        print("2. Create Flight")
        print("3. Book Seat")
        print("4. Cancel Seat")
        print("5. View Flight Summary")       
        print("6. View Customer Bookings")    
        print("7. Load Data")                 
        print("8. Exit")
        Choice = int(input("Enter your choice (1 to 8): "))
        print()
        
        if Choice == 1:
            while True:
                while True:
                    CustomerName = input("Enter customer name: ")
                    if CustomerName == "":
                        print("Customer name cannot be empty!")
                    else:
                        break
                while True:
                    Address = input("Enter customer's address: ")
                    if Address == "":
                        print("Address cannot be empty!")
                    else:
                        break
                while True:
                    PassengerCode = input("Enter the 3-digit passenger code: ")
                    if PassengerCode == "":
                        print("Passenger code cannot be empty!")
                    elif int(PassengerCode) > 999:
                        print("Passenger code should be of 3-digits!")
                    elif int(PassengerCode) < 100:
                        print("Passenger code should be of atleast 3-digits and cannot start with 0")
                    else:
                        break
                while True:
                    HalalMeat = input("Do you want your meat to be halal? (Y/N): ")
                    if HalalMeat == "":
                        print("You have to tell us your meat preference!")
                    elif HalalMeat.lower() == "n":
                        MealPreference = "Non-Halal"
                        break
                    elif HalalMeat.lower() == "y":
                        MealPreference = "Halal"
                        break
                    else:
                        print("Please input Y or N!")
                CustomerObject = Customer.Customer(CustomerName, Address, PassengerCode, MealPreference)
                Customers.append(CustomerObject)
                print("Customer added successfully!")
                SaveCustomers(Customers)
                Question = input("Do you want to add another customer? (Y/N): ")
                if Question.lower() == "n":
                    break

        elif Choice == 2:
            while True:
                FlightNumber = input("Enter flight number (Ex: QA6784): ")
                if FlightNumber == "":
                    print("Flight number cannot be empty!")
                else:
                    break
            while True:
                FlightName = input("Enter flight name: ")
                if FlightName == "":
                    print("Flight name cannot be empty!")
                else:
                    break
            while True:
                StartPoint = input("Enter flight's start point: ")
                if StartPoint == "":
                    print("Start point cannot be empty!")
                else:
                    break
            while True:
                EndPoint = input("Enter flight's end point: ")
                if EndPoint == "":
                    print("End point cannot be empty!")
                else:
                    break
            while True:
                StartDateTime = input("Enter start date and time (YYYY-MM-DD HH:MM): ")
                if StartDateTime == "":
                    print("Start date/time cannot be empty!")
                else:
                    break
            while True:
                EndDateTime = input("Enter end date and time (YYYY-MM-DD HH:MM): ")
                if EndDateTime == "":
                    print("End date/time cannot be empty!")
                else:
                    break
            while True:
                TotalSeats = input("Enter total number of seats: ")
                if not TotalSeats.isdigit():
                    print("Total seats should be a number!")
                elif int(TotalSeats) <= 0:
                    print("Total seats must be greater than zero!")
                else:
                    TotalSeats = int(TotalSeats)
                    break
            SeatsBooked = 0
            FlightObject = Flight.Flight(FlightNumber, FlightName, StartPoint, EndPoint, StartDateTime, EndDateTime, TotalSeats, SeatsBooked, Bookings)
            Flights.append(FlightObject)
            print("Flight added successfully!")
            SaveFlights(Flights)
        
        elif Choice == 3:
            if len(Customers) == 0:
                print("No customers found! Please add a customer first.")
                continue
            if len(Flights) == 0:
                print("No flights found! Please create a flight first.")
                continue
            PassengerCode = input("Enter passenger code: ")
            CustExists = any(cust.PassengerCode == PassengerCode for cust in Customers)
            if not CustExists:
                print("Passenger code does not exist!")
                continue
            FlightNumber = input("Enter flight number: ")
            FlightObj = next((f for f in Flights if f.FlightNumber == FlightNumber), None)
            if not FlightObj:
                print("Flight number does not exist!")
                continue
            if any(b["PassengerCode"] == PassengerCode and b["FlightNumber"] == FlightNumber for b in Bookings):
                print("You are already booked for this flight!")
                continue
            if FlightObj.SeatsBooked < FlightObj.TotalSeats:
                FlightObj.SeatsBooked += 1
                Bookings.append({"PassengerCode": PassengerCode, "FlightNumber": FlightNumber})
                print("Booking done successfully!")
                SaveBookings(Bookings)
            else:
                print("No seats available for this flight!")

        elif Choice == 4:
            PassengerCode = input("Enter passenger code to cancel booking: ")
            FlightNumber = input("Enter flight number to cancel: ")
            BookingFound = False
            for b in Bookings:
                if b["PassengerCode"] == PassengerCode and b["FlightNumber"] == FlightNumber:
                    Bookings.remove(b)
                    for f in Flights:
                        if f.FlightNumber == FlightNumber:
                            f.SeatsBooked -= 1
                    BookingFound = True
                    print("Booking cancelled successfully!")
                    SaveBookings(Bookings)
                    break
            if not BookingFound:
                print("No booking found for given passenger and flight!")

        elif Choice == 5:
            if len(Flights) == 0:
                print("No flights found!")
            else:
                TableData = [[f.FlightNumber, f.FlightName, f.StartPoint, f.EndPoint, f.StartDateTime, f.EndDateTime, f.TotalSeats, f.SeatsBooked] for f in Flights]
                print(tabulate(TableData, headers=["Flight No", "Name", "Start", "End", "Start DateTime", "End DateTime", "Total Seats", "Booked"]))

        elif Choice == 6:
            PassengerCode = input("Enter passenger code to view bookings: ")
            BookingsFound = [b for b in Bookings if b["PassengerCode"] == PassengerCode]
            if not BookingsFound:
                print("No bookings found for the given passenger code!")
            else:
                TableData = []
                for b in BookingsFound:
                    FlightObj = next((f for f in Flights if f.FlightNumber == b["FlightNumber"]), None)
                    if FlightObj:
                        TableData.append([PassengerCode, FlightObj.FlightNumber, FlightObj.FlightName, FlightObj.StartPoint, FlightObj.EndPoint])
                print(tabulate(TableData, headers=["Passenger Code", "Flight No", "Flight Name", "Start", "End"]))

        elif Choice == 7:
            print("1. Load Customers")
            print("2. Load Flights")
            print("3. Load Bookings")
            SubChoice = int(input("Enter your choice (1 to 3): "))
            if SubChoice == 1:
                Customers = LoadList("Customers")
            elif SubChoice == 2:
                Flights = LoadList("Flights")
            elif SubChoice == 3:
                Bookings = LoadList("Bookings")

        elif Choice == 8:
            print("Exiting Application!")
            break

if __name__ == "__main__":
    main()
