import pickle
import os
import tabulate

EventList = []
CustomerList = []

def SaveEvents():
    global EventList
    with open("events.bin", "wb") as fw:
        pickle.dump(EventList, fw)

def LoadEvents():
    global EventList
    if os.path.exists("events.bin"):
        with open("events.bin", "rb") as fr:
            EventList = pickle.load(fr)
            
def SaveCustomers():
    global CustomerList
    with open("customers.bin", "wb") as fw:
        pickle.dump(CustomerList, fw)

def LoadCustomers():
    global CustomerList
    if os.path.exists("customers.bin"):
        with open("customers.bin", "rb") as fr:
            CustomerList = pickle.load(fr)
            
def CheckEventId(Eid):
    Flag = False
    for Event in EventList:
        if (Event[0] == Eid):
            Flag = True
            break
    return Flag
    
def CheckCustomerId(Cid):
    global CustomerList
    Flag = False
    for Customer in CustomerList:
        if (Customer[0] == Cid):
            Flag = True
            break
    return Flag
    
def AddEvent():
    Event = []
    
    while True:
        EventId = input("Enter event's id: ")
        if EventId == "":
            print("Event id cannot be blank!")
        elif CheckEventId(EventId) == True:
            print("Event id already exists!")
        else:
            break
    
    while True:
        EventName = input("Enter event's name: ")
        if EventName == "":
            print("Event name cannot be blank!")
        else:
            break
    
    while True:
        EventDescription = input("Enter event's description: ")
        if EventDescription == "":
            print("Event description cannot be blank!")
        else:
            break
    
    while True:
        VenueName = input("Enter venue's name: ")
        if VenueName == "":
            print("Venue name cannot be blank!")
        else:
            break
    
    while True:
        Date = input("Enter event date (dd/mm/yyyy): ")
        if Date == "":
            print("Date cannot be blank!")
        else:
            break
    
    while True:
        Time = input("Enter event time: ")
        if Time == "":
            print("Time cannot be blank!")
        else:
            break
        
    while True:
        TotalSeats = int(input("Enter total number of seats: "))
        if TotalSeats == "":
            print("Total seats cannot be blank!")
        else:
            break
    
    BookedSeats  = 0
    AvailableSeats = TotalSeats - BookedSeats
    CustList = []
    Event.append(EventId)
    Event.append(EventName)
    Event.append(EventDescription)
    Event.append(VenueName)
    Event.append(Date)
    Event.append(Time)
    Event.append(TotalSeats)
    Event.append(BookedSeats)
    Event.append(AvailableSeats)
    Event.append(CustList)
    
    EventList.append(Event)
    
    SaveEvents()
    
    print("Event created successfully!")
    
def EditEvent():
    
    UpdateEventList = []
    
    EventId = input("Enter event id you want to edit: ")
    
    Flag = False
    
    for Event in EventList:
        if Event[0] == EventId:
            Index = EventList.index(Event)
            Flag = True
            break
    
    if Flag == False:
        print("No such event id exists!")
    else:
        while True:
            EventName = input("Enter event name: ")
            if EventName == "":
                EventName = EventList[Index][1]
            break

        while True:
            EventDescription = input("Enter event description: ")
            if EventDescription == "":
                EventDescription = EventList[Index][2]
            break

        while True:
            VenueName = input("Enter venue name: ")
            if VenueName == "":
                VenueName = EventList[Index][3]
            break

        while True:
            Date = input("Enter date (dd/mm/yyyy): ")
            if Date == "":
                Date = EventList[Index][4]
            break

        while True:
            Time = input("Enter time: ")
            if Time == "":
                Time = EventList[Index][5]
            break

        while True:
            TotalSeats = input("Enter total number of seats: ")
            if TotalSeats == "":
                TotalSeats = EventList[Index][6]
            else:
                TotalSeats = int(TotalSeats)
            break

        BookedSeats = EventList[Index][7]
        AvailableSeats = TotalSeats - BookedSeats
        CustList = EventList[Index][9]

        UpdateEventList.append(EventId)
        UpdateEventList.append(EventName)
        UpdateEventList.append(EventDescription)
        UpdateEventList.append(VenueName)
        UpdateEventList.append(Date)
        UpdateEventList.append(Time)
        UpdateEventList.append(TotalSeats)
        UpdateEventList.append(BookedSeats)
        UpdateEventList.append(AvailableSeats)
        UpdateEventList.append(CustList)

        EventList[Index] = UpdateEventList
        
        SaveEvents()
        
        print("Event updated successfully!")
        
def DeleteEvent():
    EventId = input("Enter event id of the record you want to delete: ")
    
    Flag = False
    for i in range(len(EventList)):
        if EventList[i][0] == EventId:
            DeletedEvent = EventList.pop(i)
            print("Event id", DeletedEvent[0], "has been deleted successfully!")
            Flag = True
            break
    if Flag == False:
        print("No event record with the id found!")
        
    SaveEvents()
    
def ViewEventById():
    EventId = input("Enter event id you want to view: ")
    
    Flag = False
    for Event in EventList:
        if Event[0] == EventId:
            print("----------- Event Details -----------")
            print("Event ID:", Event[0])
            print("Event Name:", Event[1])
            print("Description:", Event[2])
            print("Venue:", Event[3])
            print("Date:", Event[4])
            print("Time:", Event[5])
            print("Total Seats:", Event[6])
            print("Booked Seats:", Event[7])
            print("Available Seats:", Event[8])
            print("Customer List:", Event[9])
            Flag = True
            break
    
    if Flag == False:
        print("No event found with the entered id!")

def ViewAllEvents():
    if len(EventList) == 0:
        print("No events available!")
    else:
        print()
        print("---------- All events ----------")
        print()
        print(tabulate(
            EventList,
            headers=["Event ID", "Event Name", "Description", "Venue", "Date", "Time",
                     "Total Seats", "Booked Seats", "Available Seats", "Customer List"]
        ))
    
def AddCustomer():
    Customer = []
    
    while True:
        CustomerId = input("Enter customer id: ")
        if CustomerId == "":
            print("Customer id cannot be blank!")
        elif CheckCustomerId(CustomerId) == True:
            print("Customer id already exists!")
        else:
            break
        
    while True:
        CustomerName = input("Enter customer name: ")
        if CustomerName == "":
            print("Customer name cannot be blank!")
        else:
            break
        
    while True:
        Type = input("Enter your type (Adult/Child): ")
        if Type == "":
            print("Type cannot be blank!")
        else:
            break
    
    while True:
        PhoneNumber = input("Enter your phone number: ")
        if PhoneNumber == "":
            print("Phone number cannot be blank!")
        elif PhoneNumber.isnumeric and len(PhoneNumber) == 10:
            break
        else:
            print("Invalid phone number!")
    
    while True:
        Email = input("Enter your email: ")
        if Email == "":
            input("Email cannot be blank!")
        elif "@" in Email:
            break
        else:
            print("Invalid email format!")
        
    Customer.append(CustomerId)
    Customer.append(CustomerName)
    Customer.append(Type)
    Customer.append(PhoneNumber)
    Customer.append(Email)
    
    CustomerList.append(Customer)
    
    SaveCustomers()
    
    print("Customer added successfully!")
    
def EditCustomer():
    
    UpdateCustomerList = []
    
    CustomerId = input("Enter customer id you want to edit: ")
    
    Flag = False
    
    for Customer in CustomerList:
        if Customer[0] == CustomerId:
            Index = CustomerList.index(Customer)
            Flag = True
            break
        
    if Flag == False:
        print("No such customer id exists!")
    else:
        while True:
            CustomerName = input("Enter customer name: ")
            if CustomerName == "":
                CustomerName = CustomerList[Index][1]
            break

        while True:
            Type = input("Enter type (Adult/Child): ")
            if Type == "":
                Type = CustomerList[Index][2]
            break

        while True:
            PhoneNumber = input("Enter phone number: ")
            if PhoneNumber == "":
                PhoneNumber = CustomerList[Index][3]
            break

        while True:
            Email = input("Enter email id: ")
            if Email == "":
                Email = CustomerList[Index][4]
            break

        UpdateCustomerList.append(CustomerId)
        UpdateCustomerList.append(CustomerName)
        UpdateCustomerList.append(Type)
        UpdateCustomerList.append(PhoneNumber)
        UpdateCustomerList.append(Email)
        
        CustomerList[Index] = UpdateCustomerList
        
        SaveCustomers()
        
        print("Customer updated successfully!")
        
def DeleteCustomer():
    CustomerId = input("Enter customer id of the record you want to delete: ")
    
    Flag = False
    for i in range(len(CustomerList)):
        if CustomerList[i][0] == CustomerId:
            DeletedEvent = CustomerList.pop(i)
            print("Customer id", DeletedEvent[0], "has been deleted successfully!")
            Flag = True
            break
    if Flag == False:
        print("No event record with the id found!")
        
    SaveEvents()
    
def ViewCustomerById():
    CustomerId = input("Enter customer id you want to view: ")
    
    Flag = False
    for Customer in CustomerList:
        if Customer[0] == CustomerId:
            print("----------- Event Details -----------")
            print("Customer ID:", Customer[0])
            print("Customer Name:", Customer[1])
            print("Type:", Customer[2])
            print("PhoneNumber:", Customer[3])
            print("Email:", Customer[4])
            Flag = True
            break
    
    if Flag == False:
        print("No customer found with the entered id!")
        
def ViewAllCustomers():
    if len(CustomerList) == 0:
        print("No customers available!")
    else:
        print()
        print("---------- All customers ----------")
        print()
        print(tabulate(
            CustomerList,
            headers=["Customer ID", "Customer Name", "Type", "PhoneNumber", "Email"]
        ))

def EventReservation():
    
    CustomerFlag = False
    
    while True:
        CustomerId = input("Enter customer id: ")
        if CustomerId == "":
            print("CustomerId cannot be blank!")
        else:
            break
        
    for Customer in CustomerList:
        if Customer[0] == CustomerId:
            CustomerIndex = CustomerList.index(Customer)
            CustomerFlag = True
            break
        
    if CustomerFlag == False:
        print("Customer id does not exist!")
        
    else:
        while True:
            EventId = input("Enter event id: ")
            if EventId == "":
                print("Event id cannot be blank!")
            else:
                break
        EventFlag = False  
        for Event in EventList:
            if Event[0] == EventId:
                EventIndex = EventList.index(Event)
                EventFlag = True
                break
        if EventFlag == False:
            print("Event id does not exist!")
            
        else:
            Flag = False
            for Cust in EventList[EventIndex][9]:
                if Cust == CustomerList[CustomerIndex]:
                    Flag = True
                    break
            
            if Flag == False:
                EventList[EventIndex][9].append(CustomerList[CustomerIndex])
                EventList[EventIndex][7] += 1
                EventList[EventIndex][8] = EventList[EventIndex][6] - EventList[EventIndex][7]
                print("Reservation done successfully!")
                
                SaveEvents()
                
            else:
                print("You are already booked for this event!")
                
def CancelReservation():
    EventFlag = False

    while True:
        EventId = input("Enter event id: ")
        if EventId == "":
            print("Event id cannot be blank!")
        else:
            break

    for Event in EventList:
        if Event[0] == EventId:
            EventIndex = EventList.index(Event)
            EventFlag = True
            break

    if EventFlag == False:
        print("Event id does not exist!")
    else:
        CustomerFlag = False

        while True:
            CustomerId = input("Enter customer id: ")
            if CustomerId == "":
                print("Customer id cannot be blank!")
            else:
                break

        for Customer in CustomerList:
            if Customer[0] == CustomerId:
                CustomerFlag = True
                break

        if CustomerFlag == False:
            print("Customer id does not exist!")
        else:
            ReservationList = EventList[EventIndex][9]
            ReservationFlag = False

            for i in range(len(ReservationList)):
                if ReservationList[i][0] == CustomerId:
                    ReservationList.pop(i)
                    EventList[EventIndex][7] -= 1  
                    EventList[EventIndex][8] = EventList[EventIndex][6] - EventList[EventIndex][7] 
                    print("Reservation for customer id", CustomerId, "for event", EventId, "has been cancelled successfully!")
                    ReservationFlag = True
                    break

            if ReservationFlag == False:
                print("No reservation found for this customer in the selected event.")

            SaveEvents()

def CustomerListInEvent():
    while True:
        EventId = input("Enter event id: ")
        if EventId == "":
            print("Event id cannot be blank!")
        else:
            break

    EventFlag = False

    for Event in EventList:
        if Event[0] == EventId:
            EventFlag = True
            print("--- Customer List for Event id:", EventId, "---")
            if len(Event[9]) == 0:
                print("No customers have reserved this event yet.")
            else:
                print(tabulate(
                    Event[9],
                    headers=["Customer ID", "Customer Name", "Type", "PhoneNumber", "Email"]
                ))
            break

    if EventFlag == False:
        print("Event id does not exist!")
        
def EventSummary():
    while True:
        EventId = input("Enter event id: ")
        if EventId == "":
            print("Event id cannot be blank!")
        else:
            break
        
    for Event in EventList:
        if Event[0] == EventId:
            print()
            print("---------- Summary of the event ----------")
            print()
            print("Event id:", Event[0])
            print("Event name:", Event[1])
            print("Event description:", Event[2])
            print("Venue name:", Event[3])
            print("Date:", Event[4])
            print("Time", Event[5])
            print("Total seats:", Event[6])
            print("Booked seats:", Event[7])
            print("Available seats:", Event[8])
            for Customer in Event[9]:
                print("Customer name:", Customer[1])
            