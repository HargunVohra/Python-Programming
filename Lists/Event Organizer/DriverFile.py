import EventOrgainzer as EO

def main():
    
    EO.LoadEvents()
    EO.LoadCustomers()
    
    while True: 
        
        print()
        print("-------- Organized Event Details --------")
        print()
        print("1. Add New Event")
        print("2. Edit Event")
        print("3. Delete Event")
        print("4. View Event (by Id)")
        print("5. View all Events")
        print("6. Add New Customer")
        print("7. Edit Customer")
        print("8. Delete Customer")
        print("9. View Customer (by Id)")
        print("10. View all customers")
        print("11. Event Reservation")
        print("12. Cancel Reservation")
        print("13. Show the list of customers in event")
        print("14. Summary of an event")
        print("15. Exit Application")
        Choice = int(input("Enter your choice (1 to 15): "))
        if Choice == 1:
            EO.AddEvent()
        elif Choice == 2:
            EO.EditEvent()
        elif Choice == 3:
            EO.DeleteEvent()
        elif Choice == 4:
            EO.ViewEventById()
        elif Choice == 5:
            EO.ViewAllEvents()
        elif Choice == 6:
            EO.AddCustomer()
        elif Choice == 7:
            EO.EditCustomer()
        elif Choice == 8:
            EO.DeleteCustomer()
        elif Choice == 9:
            EO.ViewCustomerById()
        elif Choice == 10:
            EO.ViewAllCustomers()
        elif Choice == 11:
            EO.EventReservation()
        elif Choice == 12:
            EO.CancelReservation()
        elif Choice == 13:
            EO.CustomerListInEvent()
        elif Choice == 14:
            EO.EventSummary()
        elif Choice == 15:
            break
        else:
            print("Invalid Input!")
        
if __name__ == "__main__":
    main()