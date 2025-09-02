import Login
import SignUp
import VehicleType
import GearboxType
import FuelType
import Vehicle
import CustomerType
import ServiceHistory
import TouristIndividual
import TravelAgencyPrivateCompany
import RentAndReturn
from tabulate import tabulate
from datetime import datetime

def ShowMenu(FullName):
    while True:
        print()
        print("------------------------ Whitechapel Vehicle Rental Service ------------------------")
        print()
        print("Welcome,", FullName)
        print()
        print("1. ADD Vehicle Type")
        print("2. UPDATE Vehicle Type")
        print("3. DELETE Vehicle Type")
        print("4. VIEW Vehicle Type By Id")
        print("5. VIEW ALL Vehicle Types")
        print("6. ADD Gearbox Type")
        print("7. UPDATE Gearbox Type")
        print("8. DELETE Gearbox Type")
        print("9. VIEW Gearbox Type By Id")
        print("10. VIEW ALL Gearbox Types")
        print("11. ADD Fuel Type")
        print("12. UPDATE Fuel Type")
        print("13. DELETE Fuel Type")
        print("14. VIEW Fuel Type By Id")
        print("15. VIEW ALL Fuel Types")
        print("16. ADD Customer Type")
        print("17. UPDATE Customer Type")
        print("18. DELETE Customer Type")
        print("19. VIEW Customer Type By Id")
        print("20. VIEW ALL Customer Types")
        print("21. ADD Vehicle")
        print("22. UPDATE Vehicle")
        print("23. DELETE Vehicle")
        print("24. VIEW Vehicle By Id")
        print("25. VIEW ALL Vehicles")
        print("26. ADD Service History Of A Vehicle")
        print("27. UPDATE Service History Of A Vehicle")
        print("28. DELETE Service History Of A Vehicle")
        print("29. VIEW Service Histories Of A Vehicle By Id")
        print("20. VIEW ALL Service Histories Of All Vehicles")
        print("31. ADD Tourist/Individual Details")
        print("32. UPDATE Tourist/Individual Details")
        print("33. DELETE Tourist/Individual Details")
        print("34. View Tourist/Individual Details By Id")
        print("35. VIEW ALL Tourist/Individual Details")
        print("36. ADD Travel Agency/Private Company Details")
        print("37. UPDATE Travel Agency/Private Company Details")
        print("38. DELETE Travel Agency/Private Company Details")
        print("39. VIEW Travel Agency/Private Company Details By Id")
        print("40. VIEW ALL Travel Agencies/Private Companies Details")
        print("41. ADD Rent And Return")
        print("42. UPDATE Rent And Return")
        print("43. DELETE Rent And Return")
        print("44. VIEW Rent And Return By Id")
        print("45. VIEW ALL Rent And Return")
        print("46. PRINT Receipt/Invoice")
        print("47. LOG OUT")
        print()
        Choice = int(input("Enter your choice (1 to 47): "))
        print()

        if Choice == 1:
            while True:
                VehicleTypeName = input("Enter vehicle type: ")
                if VehicleTypeName == "":
                    print("Vehicle type cannot be blank!")
                    continue
                            
                VehicleTypeObj = VehicleType.VehicleType(VehicleTypeName)
                VehicleTypeObj.SaveVehicleType(VehicleType.MyCursor, VehicleType.MyConnection)
                print()
                print("Vehicle type added successfully!")
                print()
                        
                Question = input("Do you want to add more vehicle types? (Y/N): ")
                if Question.lower() == "n":
                    break
        
        elif Choice == 2:
            while True:
                VehicleTypeName = input("Enter vehicle type to update: ")
                if VehicleTypeName == "":
                    print("Vehicle type cannot be blank!")
                else:
                    break
        
            VehicleTypeObj = VehicleType.VehicleType(VehicleTypeName)
            Result = VehicleTypeObj.ViewVehicleType(VehicleType.MyCursor, VehicleType.MyConnection, VehicleTypeName)
        
            if Result is False:
                print("Vehicle type does not exist!")
            else:
                NewVehicleTypeName = input("Enter new vehicle type name (leave blank to retain current): ")
                if NewVehicleTypeName == "":
                    NewVehicleTypeName = VehicleTypeName
        
                VehicleTypeObj = VehicleType.VehicleType(NewVehicleTypeName)
                VehicleTypeObj.UpdateVehicleType(VehicleType.MyCursor, VehicleType.MyConnection, VehicleTypeName, NewVehicleTypeName)
                print("Vehicle type updated successfully!")

        elif Choice == 3:
            VehicleTypeId = input("Enter vehicle type id to delete: ")
            if VehicleTypeId == "":
                print("Vehicle type id cannot be blank!")
            else:
                VehicleTypeObj = VehicleType.VehicleType("")
                Result = VehicleTypeObj.DeleteVehicleType(VehicleType.MyCursor, VehicleType.MyConnection, VehicleTypeId)

                if Result:
                    print("Vehicle type deleted successfully!")
                else:
                    print("Vehicle type id does not exist!")
        
        elif Choice == 4:
            VehicleTypeName = input("Enter vehicle type name to view: ")
            if VehicleTypeName == "":
                print("Vehicle type cannot be blank!")
            else:
                VehicleTypeObj = VehicleType.VehicleType(VehicleTypeName)
                Result = VehicleTypeObj.ViewVehicleType(VehicleType.MyCursor, VehicleType.MyConnection, VehicleTypeName)
        
                if Result is False:
                    print("Vehicle type does not exist!")
                else:
                    print("Vehicle Type ID:", Result[0], "\t Vehicle Type Name:", Result[1])
        
        elif Choice == 5:
            Results = VehicleType.VehicleType("").ViewAllVehicleTypes(VehicleType.MyCursor, VehicleType.MyConnection)
            if not Results:
                print("No vehicle types found!")
            else:
                Headers = ["Vehicle Type ID", "Vehicle Type Name"]
                print(tabulate(Results, headers=Headers))
            
        elif Choice == 6:
            while True:
                GearboxTypeName = input("Enter gearbox type: ")
                if GearboxTypeName == "":
                    print("Gearbox type cannot be blank!")
                    continue
                            
                GearboxTypeObj = GearboxType.GearboxType(GearboxTypeName)
                GearboxTypeObj.SaveGearboxType(GearboxType.MyCursor, GearboxType.MyConnection)
                print()
                print("Gearbox type added successfully!")
                print()
                        
                Question = input("Do you want to add more gearbox types? (Y/N): ")
                if Question.lower() == "n":
                    break
        
        elif Choice == 7:
            while True:
                GearboxTypeName = input("Enter gearbox type to update: ")
                if GearboxTypeName == "":
                    print("Gearbox type cannot be blank!")
                else:
                    break
        
            GearboxTypeObj = GearboxType.GearboxType(GearboxTypeName)
            Result = GearboxTypeObj.ViewGearboxType(GearboxType.MyCursor, GearboxType.MyConnection, GearboxTypeName)
        
            if Result is False:
                print("Gearbox type does not exist!")
            else:
                NewGearboxTypeName = input("Enter new gearbox type name (leave blank to retain current): ")
                if NewGearboxTypeName == "":
                    NewGearboxTypeName = GearboxTypeName
        
                GearboxTypeObj = GearboxType.GearboxType(GearboxTypeName)
                GearboxTypeObj.UpdateGearboxType(GearboxType.MyCursor, GearboxType.MyConnection, GearboxTypeName, NewGearboxTypeName)
                print("Gearbox type updated successfully!")

        elif Choice == 8:
            GearboxTypeId = input("Enter gearbox type id to delete: ")
            if GearboxTypeId == "":
                print("Gearbox type id cannot be blank!")
            else:
                GearboxTypeObj = GearboxType.GearboxType("")
                Result = GearboxTypeObj.DeleteGearboxType(GearboxType.MyCursor, GearboxType.MyConnection, GearboxTypeId)
                if Result:
                    print("Gearbox type deleted successfully!")
                else:
                    print("Gearbox type id does not exist!")
        
        elif Choice == 9:
            GearboxTypeName = input("Enter gearbox type name to view: ")
            if GearboxTypeName == "":
                print("Gearbox type cannot be blank!")
            else:
                GearboxTypeObj = GearboxType.GearboxType(GearboxTypeName)
                Result = GearboxTypeObj.ViewGearboxType(GearboxType.MyCursor, GearboxType.MyConnection, GearboxTypeName)
        
                if Result is False:
                    print("Gearbox type does not exist!")
                else:
                    print("Gearbox Type ID:", Result[0], "\t Gearbox Type Name:", Result[1])
        
        elif Choice == 10:
            Results = GearboxType.GearboxType("").ViewAllGearboxTypes(GearboxType.MyCursor, GearboxType.MyConnection)
            if not Results:
                print("No gearbox types found!")
            else:
                Headers = ["Gearbox Type ID", "Gearbox Type Name"]
                print(tabulate(Results, headers=Headers))    
                
        elif Choice == 11:
            while True:
                FuelTypeName = input("Enter fuel type: ")
                if FuelTypeName == "":
                    print("Fuel type cannot be blank!")
                    continue
                            
                FuelTypeObj = FuelType.FuelType(FuelTypeName)
                FuelTypeObj.SaveFuelType(FuelType.MyCursor, FuelType.MyConnection)
                print("Fuel type added successfully!")
                print()
        
                Question = input("Do you want to add more fuel types? (Y/N): ")
                if Question.lower() == "n":
                    break
        
        elif Choice == 12:
            FuelTypeName = input("Enter fuel type to update: ")
            FuelTypeObj = FuelType.FuelType(FuelTypeName)
            Result = FuelTypeObj.ViewFuelType(FuelType.MyCursor, FuelType.MyConnection, FuelTypeName)
        
            if Result is False:
                print("Fuel type does not exist!")
            else:
                NewFuelTypeName = input("Enter new fuel type name (leave blank to retain current): ")
                if NewFuelTypeName == "":
                    NewFuelTypeName = FuelTypeName
                FuelTypeObj = FuelType.FuelType(NewFuelTypeName)
                FuelTypeObj.UpdateFuelType(FuelType.MyCursor, FuelType.MyConnection, FuelTypeName, NewFuelTypeName)
                print("Fuel type updated successfully!")
        
        elif Choice == 13:
            FuelTypeId = input("Enter fuel type id to delete: ")
            if FuelTypeId == "":
                print("Fuel type id cannot be blank!")
            else:
                FuelTypeObj = FuelType.FuelType("")
                Result = FuelTypeObj.DeleteFuelType(FuelType.MyCursor, FuelType.MyConnection, FuelTypeId)
                if Result:
                    print("Fuel type deleted successfully!")
                else:
                    print("Fuel type id does not exist!")
        
        elif Choice == 14:
            FuelTypeName = input("Enter fuel type name to view: ")
            FuelTypeObj = FuelType.FuelType(FuelTypeName)
            Result = FuelTypeObj.ViewFuelType(FuelType.MyCursor, FuelType.MyConnection, FuelTypeName)
        
            if Result is False:
                print("Fuel type does not exist!")
            else:
                print("Fuel Type ID:", Result[0], "\t Fuel Type Name:", Result[1])
        
        elif Choice == 15:
            Results = FuelType.FuelType("").ViewAllFuelTypes(FuelType.MyCursor, FuelType.MyConnection)
            if not Results:
                print("No fuel types found!")
            else:
                Headers = ["Fuel Type ID", "Fuel Type Name"]
                print(tabulate(Results, headers=Headers))
        
        elif Choice == 16:
            while True:
                CustomerTypeName = input("Enter customer type: ")
                if CustomerTypeName == "":
                    print("Customer type cannot be blank!")
                    continue
                            
                CustomerTypeObj = CustomerType.CustomerType(CustomerTypeName)
                CustomerTypeObj.SaveCustomerType(CustomerType.MyCursor, CustomerType.MyConnection)
                print("Customer type added successfully!")
                print()
        
                Question = input("Do you want to add more customer types? (Y/N): ")
                if Question.lower() == "n":
                    break
        
        elif Choice == 17:
            CustomerTypeName = input("Enter customer type to update: ")
            CustomerTypeObj = CustomerType.CustomerType(CustomerTypeName)
            Result = CustomerTypeObj.ViewCustomerType(CustomerType.MyCursor, CustomerType.MyConnection, CustomerTypeName)
        
            if Result is False:
                print("Customer type does not exist!")
            else:
                NewCustomerTypeName = input("Enter new customer type name (leave blank to retain current): ")
                if NewCustomerTypeName == "":
                    NewCustomerTypeName = CustomerTypeName
                CustomerTypeObj = CustomerType.CustomerType(NewCustomerTypeName)
                CustomerTypeObj.UpdateCustomerType(CustomerType.MyCursor, CustomerType.MyConnection, CustomerTypeName, NewCustomerTypeName)
                print("Customer type updated successfully!")
        
        elif Choice == 18:
            CustomerTypeId = input("Enter customer type id to delete: ")
            if CustomerTypeId == "":
                print("Customer type id cannot be blank!")
            else:
                CustomerTypeObj = CustomerType.CustomerType("")
                Result = CustomerTypeObj.DeleteCustomerType(CustomerType.MyCursor, CustomerType.MyConnection, CustomerTypeId)
                if Result:
                    print("Customer type deleted successfully!")
                else:
                    print("Customer type id does not exist!")
        
        elif Choice == 19:
            CustomerTypeName = input("Enter customer type name to view: ")
            CustomerTypeObj = CustomerType.CustomerType(CustomerTypeName)
            Result = CustomerTypeObj.ViewCustomerType(CustomerType.MyCursor, CustomerType.MyConnection, CustomerTypeName)
        
            if Result is False:
                print("Customer type does not exist!")
            else:
                print("Customer Type ID:", Result[0], "\t Customer Type Name:", Result[1])
        
        elif Choice == 20:
            Results = CustomerType.CustomerType("").ViewAllCustomerTypes(CustomerType.MyCursor, CustomerType.MyConnection)
            if not Results:
                print("No customer types found!")
            else:
                Headers = ["Customer Type ID", "Customer Type Name"]
                print(tabulate(Results, headers=Headers))
                
        elif Choice == 21:
            while True:
                while True:
                    VehicleTypeId = input("Enter vehicle type id: ")
                    if VehicleTypeId == "":
                        print("Vehicle type id cannot be blank!")
                    else:
                        break
        
                while True:
                    GearboxTypeId = input("Enter gearbox type id: ")
                    if GearboxTypeId == "":
                        print("Gearbox type id cannot be blank!")
                    else:
                        break
        
                while True:
                    FuelTypeId = input("Enter fuel type id: ")
                    if FuelTypeId == "":
                        print("Fuel type id cannot be blank!")
                    else:
                        break
        
                while True:
                    RegistrationNumber = input("Enter registration number (AA 00 AA 0000) format: ")
                    if RegistrationNumber == "":
                        print("Registration number cannot be blank!")
                    else:
                        break
        
                while True:
                    EngineSize = input("Enter engine size (in litres): ")
                    if EngineSize == "":
                        print("Engine size cannot be blank!")
                    else:
                        break
        
                while True:
                    Colour = input("Enter colour: ")
                    if Colour == "":
                        print("Colour cannot be blank!")
                    else:
                        break
        
                while True:
                    Model = input("Enter model: ")
                    if Model == "":
                        print("Model cannot be blank!")
                    else:
                        break
        
                while True:
                    Make = input("Enter make (in Rs): ")
                    if Make == "":
                        print("Make cannot be blank!")
                    else:
                        break
        
                while True:
                    CurrentMileage = input("Enter current mileage: ")
                    if CurrentMileage == "":
                        print("Current mileage cannot be blank!")
                    else:
                        break
        
                while True:
                    NumberOfDoors = input("Enter number of doors: ")
                    if NumberOfDoors == "":
                        print("Number of doors cannot be blank!")
                    else:
                        break
        
                while True:
                    SafetyInformation = input("Enter safety information: ")
                    if SafetyInformation == "":
                        print("Safety information cannot be blank!")
                    else:
                        break
        
                while True:
                    Length = input("Enter length (in meters): ")
                    if Length == "":
                        print("Length cannot be blank!")
                    else:
                        break
        
                while True:
                    Width = input("Enter width (in meters): ")
                    if Width == "":
                        print("Width cannot be blank!")
                    else:
                        break
        
                while True:
                    Height = input("Enter height (in meters): ")
                    if Height == "":
                        print("Height cannot be blank!")
                    else:
                        break
        
                while True:
                    OnService = input("Is vehicle on service? (Y/N): ").upper()
                    if OnService not in ["Y", "N"]:
                        print("Please enter Y or N!")
                    else:
                        break
        
                # If vehicle is on service, default reserved/rented to N
                if OnService == "Y":
                    IsReserved = "N"
                    IsRented = "N"
                else:
                    while True:
                        IsReserved = input("Is reserved (Y/N): ").upper()
                        if IsReserved not in ["Y", "N"]:
                            print("Please enter Y or N!")
                        else:
                            break
        
                    while True:
                        IsRented = input("Is rented (Y/N): ").upper()
                        if IsRented not in ["Y", "N"]:
                            print("Please enter Y or N!")
                        else:
                            break
        
                VehicleObj = Vehicle.Vehicle(
                    VehicleTypeId, GearboxTypeId, FuelTypeId, RegistrationNumber,
                    EngineSize, Colour, Model, Make, CurrentMileage, NumberOfDoors,
                    SafetyInformation, Length, Width, Height, OnService, IsReserved, IsRented
                )
        
                Result = VehicleObj.SaveVehicle(Vehicle.MyCursor, Vehicle.MyConnection)
                if Result:
                    print("Vehicle added successfully!")
                else:
                    print("Invalid VehicleTypeId, GearboxTypeId or FuelTypeId — cannot add vehicle!")
        
                Question = input("Do you want to add more vehicles? (Y/N): ")
                if Question.lower() == "n":
                    break
        
        elif Choice == 22:
            while True:
                RegistrationNumber = input("Enter registration number of vehicle to update: ")
                if RegistrationNumber == "":
                    print("Registration number cannot be blank!")
                else:
                    break
        
            VehicleObj = Vehicle.Vehicle("", "", "", RegistrationNumber, "", "", "", "", "", "", "", "", "", "", "", "", "")
            Result = VehicleObj.UpdateVehicle(Vehicle.MyCursor, Vehicle.MyConnection, RegistrationNumber)
        
            if Result is False:
                print("Vehicle does not exist!")
            else:
                VehicleTypeId = input("Enter new vehicle type id (leave blank to retain current): ")
                GearboxTypeId = input("Enter new gearbox type id (leave blank to retain current): ")
                FuelTypeId = input("Enter new fuel type id (leave blank to retain current): ")
                EngineSize = input("Enter new engine size (leave blank to retain current): ")
                Colour = input("Enter new colour (leave blank to retain current): ")
                Model = input("Enter new model (leave blank to retain current): ")
                Make = input("Enter new make (leave blank to retain current): ")
                CurrentMileage = input("Enter new current mileage (leave blank to retain current): ")
                NumberOfDoors = input("Enter new number of doors (leave blank to retain current): ")
                SafetyInformation = input("Enter new safety information (leave blank to retain current): ")
                Length = input("Enter new length (leave blank to retain current): ")
                Width = input("Enter new width (leave blank to retain current): ")
                Height = input("Enter new height (leave blank to retain current): ")
        
                OnService = input("Enter OnService status (Y or N, leave blank to retain current): ").upper()
        
                if OnService == "Y":
                    IsReserved = "N"
                    IsRented = "N"
                else:
                    IsReserved = input("Enter reserved status (Y or N, leave blank to retain current): ").upper()
                    IsRented = input("Enter rented status (Y or N, leave blank to retain current): ").upper()
        
                VehicleObj = Vehicle.Vehicle(
                    VehicleTypeId, GearboxTypeId, FuelTypeId, RegistrationNumber,
                    EngineSize, Colour, Model, Make, CurrentMileage, NumberOfDoors,
                    SafetyInformation, Length, Width, Height, OnService, IsReserved, IsRented
                )
                Result = VehicleObj.UpdateVehicle(Vehicle.MyCursor, Vehicle.MyConnection, RegistrationNumber)
        
                if Result is False:
                    print("Invalid VehicleTypeId, GearboxTypeId or FuelTypeId — cannot update vehicle!")
                else:
                    print("Vehicle updated successfully!")

        elif Choice == 23:
            while True:
                VehicleId = input("Enter vehicle id to delete: ")
                if VehicleId == "":
                    print("Vehicle id cannot be blank!")
                else:
                    break
        
            VehicleObj = Vehicle.Vehicle("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
            Result = VehicleObj.DeleteVehicle(Vehicle.MyCursor, Vehicle.MyConnection, VehicleId)
        
            if Result:
                print("Vehicle deleted successfully!")
            else:
                print("Vehicle id does not exist!")
        
        elif Choice == 24:
            while True:
                VehicleId = input("Enter vehicle id to view: ")
                if VehicleId == "":
                    print("Vehicle id cannot be blank!")
                else:
                    break
        
            VehicleObj = Vehicle.Vehicle("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
            Result = VehicleObj.ViewVehicleById(Vehicle.MyCursor, Vehicle.MyConnection, VehicleId)
        
            if Result is False:
                print("Vehicle does not exist!")
            else:
                print("Vehicle Type:", Result[1],
                      "\nGearbox Type:", Result[2],
                      "\nFuel Type:", Result[3],
                      "\nRegistration Number:", Result[4],
                      "\nEngine Size:", Result[5],
                      "\nColour:", Result[6],
                      "\nModel:", Result[7],
                      "\nMake:", "Rs", Result[8],
                      "\nCurrent Mileage:", Result[9],
                      "\nNumber Of Doors:", Result[10],
                      "\nSafety Information:", Result[11],
                      "\nLength:", Result[12],
                      "\nWidth:", Result[13],
                      "\nHeight:", Result[14],
                      "\nOn Service:", Result[15],
                      "\nIs Reserved:", Result[16],
                      "\nIs Rented:", Result[17])
        
        elif Choice == 25:
            Results = Vehicle.Vehicle("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "").ViewAllVehicles(Vehicle.MyCursor, Vehicle.MyConnection)
            if not Results:
                print("No vehicles found!")
            else:
                Headers = ["Vehicle Id", "Vehicle Type", "Gearbox Type", "Fuel Type", "Registration Number",
                           "Engine Size", "Colour", "Model", "Make", "Current Mileage", "Number Of Doors",
                           "Safety Information", "Length", "Width", "Height", "On Service", "Is Reserved", "Is Rented"]
                
                print(tabulate(Results, headers=Headers))
                
        elif Choice == 26:
            while True:
                while True:
                    VehicleId = input("Enter vehicle id: ")
                    if VehicleId == "":
                        print("Vehicle id cannot be blank!")
                    else:
                        break
            
                while True:
                    ServiceType = input("Enter service type: ")
                    if ServiceType == "":
                        print("Service type cannot be blank!")
                    else:
                        break
            
                while True:
                    Cost = input("Enter service cost (in Rs): ")
                    if Cost == "":
                        print("Service cost cannot be blank!")
                    else:
                        break
            
                while True:
                    DateOfService = input("Enter date of service (YYYY-MM-DD): ")
                    if DateOfService == "":
                        print("Date of service cannot be blank!")
                    else:
                        break
            
                while True:
                    DateOfReturn = input("Enter date of return (YYYY-MM-DD): ")
                    if DateOfReturn == "":
                        print("Date of return cannot be blank!")
                    else:
                        break
            
                ServiceObj = ServiceHistory.ServiceHistory(VehicleId, ServiceType, Cost, DateOfService, DateOfReturn)
            
                Result = ServiceObj.SaveServiceHistory(ServiceHistory.MyCursor, ServiceHistory.MyConnection)
                if Result:
                    print("Service history added successfully!")


                else:
                    print("Vehicle id does not exist!")
            
                Question = input("Do you want to add more service histories? (Y/N): ")
                if Question.lower() == "n":
                    break
                

        elif Choice == 27:
            while True:
                ServiceHistoryId = input("Enter service history id to update: ")
                if ServiceHistoryId == "":
                    print("Service history id cannot be blank!")
                else:
                    break
        
            ServiceObj = ServiceHistory.ServiceHistory("", "", "", "", "")
            Result = ServiceObj.UpdateServiceHistory(ServiceHistory.MyCursor, ServiceHistory.MyConnection, ServiceHistoryId)
        
            if Result is False:
                print("Service history record does not exist!")
            else:
                VehicleId = input("Enter new vehicle id (leave blank to retain current): ")
                ServiceType = input("Enter new service type (leave blank to retain current): ")
                Cost = input("Enter new service cost (leave blank to retain current): ")
                DateOfService = input("Enter new date of service (YYYY-MM-DD) (leave blank to retain current): ")
                DateOfReturn = input("Enter new date of return (YYYY-MM-DD) (leave blank to retain current): ")
        
                ServiceObj = ServiceHistory.ServiceHistory(VehicleId, ServiceType, Cost, DateOfService, DateOfReturn)
                Result = ServiceObj.UpdateServiceHistory(ServiceHistory.MyCursor, ServiceHistory.MyConnection, ServiceHistoryId)
        
                if Result:
                    print("Service history updated successfully!")
                else:
                    print("Vehicle id does not exist!")

        elif Choice == 28:
            while True:
                ServiceHistoryId = input("Enter service history id to delete: ")
                if ServiceHistoryId == "":
                    print("Service history id cannot be blank!")
                else:
                    break
        
            ServiceObj = ServiceHistory.ServiceHistory("", "", "", "", "")
            Result = ServiceObj.DeleteServiceHistory(ServiceHistory.MyCursor, ServiceHistory.MyConnection, ServiceHistoryId)
        
            if Result:
                print("Service history deleted successfully!")
            else:
                print("Service history id does not exist!")

        elif Choice == 29:
            while True:
                VehicleModel = input("Enter vehicle model name to view service history: ")
                if VehicleModel == "":
                    print("Vehicle model cannot be blank!")
                else:
                    break
        
            ServiceObj = ServiceHistory.ServiceHistory("", "", "", "", "")
            Results = ServiceObj.ViewServiceHistoryByVehicle(ServiceHistory.MyCursor, ServiceHistory.MyConnection, VehicleModel)
        
            if Results is False:
                print("No service history found for this vehicle!")
            else:
                for record in Results:
                    print()
                    print("Service History Id:", record[0],
                          "\nModel:", "Rs", record[1],
                          "\nService Type:", record[3],
                          "\nCost:", "Rs", record[4],
                          "\nDate Of Service:", record[5],
                          "\nDate Of Return:", record[6])
                    
        elif Choice == 30:
            Results = ServiceHistory.ServiceHistory("", "", "", "", "").ViewAllServiceHistories(ServiceHistory.MyCursor, ServiceHistory.MyConnection)
        
            if not Results:
                print("No service histories found!")
            else:
                FormattedResults = [(Result[0], Result[1], Result[2], "Rs " + str(Result[3]), Result[4], Result[5]) for Result in Results]
        
                Headers = ["Service History Id", "Model", "Service Type", "Cost", "Date Of Service", "Date Of Return"]
                print(tabulate(FormattedResults, headers=Headers))

        elif Choice == 31:
            while True:
                while True:
                    FullName = input("Enter full name: ")
                    if FullName == "":
                        print("Full name cannot be blank!")
                    else:
                        break
        
                while True:
                    DrivingLicense = input("Enter driving license (AA-00-0000-000000 format --- max 17 chars): ")
                    if DrivingLicense == "":
                        print("Driving license cannot be blank!")
                    elif len(DrivingLicense) == 17 or len(DrivingLicense) == 16:
                        break
                    else:
                        print("Driving license should be of 16 or 17 characters!")
        
                while True:
                    DateOfBirth = input("Enter date of birth (YYYY-MM-DD): ")
                    if DateOfBirth == "":
                        print("Date of birth cannot be blank!")
                    else:
                        break
        
                while True:
                    Address = input("Enter address: ")
                    if Address == "":
                        print("Address cannot be blank!")
                    else:
                        break
        
                while True:
                    EmergencyContact = input("Enter emergency contact number: ")
                    if EmergencyContact == "":
                        print("Emergency contact cannot be blank!")
                    elif len(EmergencyContact) != 10:
                        print("Emergency contact should be exactly 10 digits!")
                    else:
                        break
        
                while True:
                    CustomerTypeId = input("Enter customer type id (1 for Tourist, 2 for Individual): ")
                    if CustomerTypeId == "":
                        print("Customer type id cannot be blank!")
                    elif CustomerTypeId not in ["1", "2"]:
                        print("You should be 1. Tourist or 2. Individual to proceed")
                    else:
                        break
        
                TouristObj = TouristIndividual.TouristIndividual(CustomerTypeId, FullName, DrivingLicense, DateOfBirth, Address, EmergencyContact)
        
                Result = TouristObj.SaveTouristIndividual(TouristIndividual.MyCursor, TouristIndividual.MyConnection)
                if Result:
                    print("Tourist/Individual details added successfully!")
                else:
                    print("Invalid CustomerTypeId or ServiceHistoryId! Could not save.")
        
                Question = input("Do you want to add more tourist/individual details? (Y/N): ")
                if Question.lower() == "n":
                    break

        elif Choice == 32:
            while True:
                TouristIndividualId = input("Enter TouristIndividual ID to update: ")
                if TouristIndividualId == "":
                    print("TouristIndividual ID cannot be blank!")
                else:
                    break
        
            TouristObj = TouristIndividual.TouristIndividual("", "", "", "", "", "")
            Result = TouristObj.UpdateTouristIndividual(TouristIndividual.MyCursor, TouristIndividual.MyConnection, TouristIndividualId)
        
            if Result is False:
                print("Tourist/Individual does not exist!")
            else:
                FullName = input("Enter new full name (leave blank to retain current): ")
                DrivingLicense = input("Enter new driving license (leave blank to retain current): ")
                DateOfBirth = input("Enter new date of birth (YYYY-MM-DD, leave blank to retain current): ")
                Address = input("Enter new address (leave blank to retain current): ")
                EmergencyContact = input("Enter new emergency contact (leave blank to retain current): ")
        
                while True:
                    CustomerTypeId = input("Enter new customer type id (1 for Tourist, 2 for Individual, leave blank to retain current): ")
                    if CustomerTypeId == "":
                        break
                    elif CustomerTypeId not in ["1", "2"]:
                        print("You should be 1. Tourist or 2. Individual to proceed")
                    else:
                        break
        
                TouristObj = TouristIndividual.TouristIndividual(CustomerTypeId, FullName, DrivingLicense, DateOfBirth, Address, EmergencyContact)
                Result = TouristObj.UpdateTouristIndividual(TouristIndividual.MyCursor, TouristIndividual.MyConnection, TouristIndividualId)
        
                if Result == "InvalidServiceHistory":
                    print("Invalid ServiceHistoryId! Cannot update.")
                else:
                    print("Tourist/Individual updated successfully!")

        elif Choice == 33:
            while True:
                TouristIndividualId = input("Enter TouristIndividual ID to delete: ")
                if TouristIndividualId == "":
                    print("TouristIndividual ID cannot be blank!")
                else:
                    break
        
            TouristObj = TouristIndividual.TouristIndividual("", "", "", "", "", "")
            Result = TouristObj.DeleteTouristIndividual(TouristIndividual.MyCursor, TouristIndividual.MyConnection, TouristIndividualId)
        
            if Result:
                print("Tourist / Individual deleted successfully!")
            else:
                print("Tourist / Individual does not exist!")

        elif Choice == 34:
            while True:
                TouristIndividualId = input("Enter TouristIndividual ID to view: ")
                if TouristIndividualId == "":
                    print("TouristIndividual ID cannot be blank!")
                else:
                    break
        
            TouristObj = TouristIndividual.TouristIndividual("", "", "", "", "", "")
            Result = TouristObj.ViewTouristIndividualById(TouristIndividual.MyCursor, TouristIndividual.MyConnection, TouristIndividualId)
        
            if Result is False:
                print("Tourist / Individual does not exist!")
            else:
                print()
                print("Customer Type:", Result[1],
                      "\nFull Name:", Result[2],
                      "\nDriving License:", Result[3],
                      "\nDate Of Birth:", Result[4],
                      "\nAddress:", Result[5],
                      "\nEmergency Contact:", Result[6])
                
        elif Choice == 35:
            Results = TouristIndividual.TouristIndividual("", "", "", "", "", "").ViewAllTouristIndividuals(
                TouristIndividual.MyCursor, TouristIndividual.MyConnection
            )
        
            if not Results:
                print()
                print("No Tourist/Individual records found!")
            else:
                Headers = ["TouristIndividual Id", "Customer Type", "Full Name", "Driving License",
                           "Date Of Birth", "Address", "Emergency Contact"]
                print(tabulate(Results, headers=Headers))
                
        elif Choice == 36:
            while True:
                while True:
                    CustomerTypeId = input("Enter customer type id (3 for Travel Agency, 4 for Private Company): ")
                    if CustomerTypeId == "":
                        print("Customer type id cannot be blank!")
                    elif CustomerTypeId not in ["3", "4"]:
                        print("You should be 3. Travel Agency or 4. Private Company to proceed")
                    else:
                        break

                while True:
                    CompanyName = input("Enter company name: ")
                    if CompanyName == "":
                        print("Company name cannot be blank!")
                    else:
                        break

                while True:
                    Address = input("Enter address: ")
                    if Address == "":
                        print("Address cannot be blank!")
                    else:
                        break

                while True:
                    ContactNumber = input("Enter contact number: ")
                    if ContactNumber == "":
                        print("Contact number cannot be blank!")
                    elif len(ContactNumber) != 10:
                        print("Contact number should be exactly 10 digits!")
                    else:
                        break

                while True:
                    ContactPerson = input("Enter contact person: ")
                    if ContactPerson == "":
                        print("Contact person cannot be blank!")
                    else:
                        break

                TravelAgencyPrivateCompanyObj = TravelAgencyPrivateCompany.TravelAgencyPrivateCompany(
                    CustomerTypeId, CompanyName, Address, ContactNumber, ContactPerson
                )
                Result = TravelAgencyPrivateCompanyObj.SaveTravelAgencyPrivateCompany(
                    TravelAgencyPrivateCompany.MyCursor, TravelAgencyPrivateCompany.MyConnection
                )

                if Result:
                    print("Travel Agency/Private Company details added successfully!")
                else:
                    print("Invalid CustomerTypeId! Could not save.")

                Question = input("Do you want to add more Travel Agencies/Private Companies? (Y/N): ")
                if Question.lower() == "n":
                    break

        elif Choice == 37:
            while True:
                TravelAgencyPrivateCompanyId = input("Enter TravelAgencyPrivateCompany ID to update: ")
                if TravelAgencyPrivateCompanyId == "":
                    print("TravelAgencyPrivateCompany ID cannot be blank!")
                else:
                    break

            TravelAgencyPrivateCompanyObj = TravelAgencyPrivateCompany.TravelAgencyPrivateCompany("", "", "", "", "")
            Result = TravelAgencyPrivateCompanyObj.UpdateTravelAgencyPrivateCompany(
                TravelAgencyPrivateCompany.MyCursor, TravelAgencyPrivateCompany.MyConnection, TravelAgencyPrivateCompanyId
            )

            if Result is False:
                print("Travel Agency/Private Company does not exist!")
            else:
                CustomerTypeId = input("Enter new customer type id (leave blank to retain current): ")
                CompanyName = input("Enter new company name (leave blank to retain current): ")
                Address = input("Enter new address (leave blank to retain current): ")
                ContactNumber = input("Enter new contact number (leave blank to retain current): ")
                ContactPerson = input("Enter new contact person (leave blank to retain current): ")
                print()

                TravelAgencyPrivateCompanyObj = TravelAgencyPrivateCompany.TravelAgencyPrivateCompany(
                    CustomerTypeId, CompanyName, Address, ContactNumber, ContactPerson
                )
                Result = TravelAgencyPrivateCompanyObj.UpdateTravelAgencyPrivateCompany(
                    TravelAgencyPrivateCompany.MyCursor, TravelAgencyPrivateCompany.MyConnection, TravelAgencyPrivateCompanyId
                )

                if Result:
                    print("Travel Agency/Private Company updated successfully!")
                else:
                    print("Invalid CustomerTypeId! Cannot update.")

        elif Choice == 38:
            while True:
                TravelAgencyPrivateCompanyId = input("Enter TravelAgencyPrivateCompany ID to delete: ")
                if TravelAgencyPrivateCompanyId == "":
                    print("TravelAgencyPrivateCompany ID cannot be blank!")
                else:
                    break

            TravelAgencyPrivateCompanyObj = TravelAgencyPrivateCompany.TravelAgencyPrivateCompany("", "", "", "", "")
            Result = TravelAgencyPrivateCompanyObj.DeleteTravelAgencyPrivateCompany(
                TravelAgencyPrivateCompany.MyCursor, TravelAgencyPrivateCompany.MyConnection, TravelAgencyPrivateCompanyId
            )

            if Result:
                print("Travel Agency/Private Company deleted successfully!")
            else:
                print("Travel Agency/Private Company does not exist!")

        elif Choice == 39:
            while True:
                TravelAgencyPrivateCompanyId = input("Enter TravelAgencyPrivateCompany ID to view: ")
                print()
                if TravelAgencyPrivateCompanyId == "":
                    print("TravelAgencyPrivateCompany ID cannot be blank!")
                else:
                    break

            TravelAgencyPrivateCompanyObj = TravelAgencyPrivateCompany.TravelAgencyPrivateCompany("", "", "", "", "")
            Result = TravelAgencyPrivateCompanyObj.ViewTravelAgencyPrivateCompanyById(
                TravelAgencyPrivateCompany.MyCursor, TravelAgencyPrivateCompany.MyConnection, TravelAgencyPrivateCompanyId
            )

            if Result is False:
                print("Travel Agency/Private Company does not exist!")
            else:
                print("Customer Type:", Result[1],
                      "\nCompany Name:", Result[2],
                      "\nAddress:", Result[3],
                      "\nContact Number:", Result[4],
                      "\nContact Person:", Result[5])

        elif Choice == 40:
            Results = TravelAgencyPrivateCompany.TravelAgencyPrivateCompany("", "", "", "", "").ViewAllTravelAgencyPrivateCompanies(
                TravelAgencyPrivateCompany.MyCursor, TravelAgencyPrivateCompany.MyConnection
            )

            if not Results:
                print("No Travel Agency/Private Company records found!")
            else:
                Headers = ["TravelAgencyPrivateCompany Id", "Customer Type", "Company Name",
                           "Address", "Contact Number", "Contact Person"]
                print(tabulate(Results, headers=Headers))

        elif Choice == 41:
            while True:
                while True:
                    CustomerTypeId = input("Enter customer type id (1=Tourist, 2=Individual, 3=Travel Agency, 4=Private Company): ")
                    if CustomerTypeId == "":
                        print("Customer type id cannot be blank!")
                    elif CustomerTypeId not in ["1", "2", "3", "4"]:
                        print("Invalid choice! Enter 1, 2, 3, or 4")
                    else:
                        break
        
                while True:
                    CustomerName = input("Enter customer name: ")
                    if CustomerName == "":
                        print("Customer name cannot be blank!")
                    else:
                        break
        
                if CustomerTypeId in ["1", "2"]:
                    RentAndReturn.MyCursor.execute(
                        "SELECT Address FROM TouristIndividual WHERE FullName = %s", (CustomerName,)
                    )
                else:
                    RentAndReturn.MyCursor.execute(
                        "SELECT Address FROM TravelAgencyPrivateCompany WHERE CompanyName = %s", (CustomerName,)
                    )
                AddressRecord = RentAndReturn.MyCursor.fetchone()
                if AddressRecord:
                    Address = AddressRecord[0]
                else:
                    print("Error: No matching customer found!")
                    break
        
                while True:
                    VehicleId = input("Enter vehicle id: ")
                    if VehicleId == "":
                        print("Vehicle id cannot be blank!")
                    else:
                        break
        
                while True:
                    RentalDate = input("Enter rental date (YYYY-MM-DD): ")
                    if RentalDate == "":
                        print("Rental date cannot be blank!")
                    else:
                        break
        
                while True:
                    ReturnDate = input("Enter return date (YYYY-MM-DD): ")
                    if ReturnDate == "":
                        print("Return date cannot be blank!")
                    else:
                        break
        
                while True:
                    Rate = input("Enter rate per day: ")
                    if Rate == "":
                        print("Rate cannot be blank!")
                    else:
                        break
        
                while True:
                    VAT = input("Enter VAT: ")
                    if VAT == "":
                        print("VAT cannot be blank!")
                    else:
                        break
        
                while True:
                    RentalServiceCost = input("Enter rental service cost: ")
                    if RentalServiceCost == "":
                        print("Rental service cost cannot be blank!")
                    else:
                        break
        
                RepairCost = "0"
                if CustomerTypeId in ["1", "2"]:
                    while True:
                        RepairCost = input("Enter repair cost: ")
                        if RepairCost == "":
                            print("Repair cost cannot be blank!")
                        else:
                            break
        
                Days = (datetime.strptime(ReturnDate, "%Y-%m-%d") - datetime.strptime(RentalDate, "%Y-%m-%d")).days
                Amount = (int(Rate) * Days) + int(VAT) + int(RentalServiceCost) + int(RepairCost)
                print("Total amount:", Amount)
        
                while True:
                    AmountPaid = input("Enter amount paid: ")
                    if AmountPaid == "":
                        print("Amount paid cannot be blank!")
                    else:
                        break
        
                TotalDueAmount = int(Amount) - int(AmountPaid)
        
                while True:
                    PaymentMethod = input("Enter payment method (Cash/Card/UPI): ")
                    if PaymentMethod == "":
                        print("Payment method cannot be blank!")
                    else:
                        break
        
                ReserveOnly = "N"
                if CustomerTypeId in ["3", "4"]:
                    ReserveOnly = input("Do you want to reserve the vehicle instead of renting? (Y/N): ").upper()
        
                RentObj = RentAndReturn.RentAndReturn(
                    CustomerTypeId, CustomerName, Address, VehicleId,
                    RentalDate, ReturnDate, str(Days), Rate, VAT, RentalServiceCost, RepairCost,
                    Amount, AmountPaid, TotalDueAmount, "Y", PaymentMethod, "", ""
                )
        
                Result = RentObj.SaveRentAndReturn(RentAndReturn.MyCursor, RentAndReturn.MyConnection, ReserveOnly)
        
                if Result == True:
                    print("Rent and Return details added successfully!")
                    RentObj.AutoReturnVehicle(RentAndReturn.MyCursor, RentAndReturn.MyConnection)
                elif Result == "InvalidVehicle":
                    print("Invalid vehicle!")
                elif Result == "VehicleUnavailable":
                    print("Vehicle is already reserved or rented!")
                else:
                    print("Invalid data! Could not save.")
        
                Question = input("Do you want to add more Rent and Return records? (Y/N): ")
                if Question.lower() == "n":
                    break

        elif Choice == 42:
            while True:
                RentAndReturnId = input("Enter RentAndReturn ID to update: ")
                if RentAndReturnId == "":
                    print("RentAndReturn ID cannot be blank!")
                else:
                    break
        
            RentObj = RentAndReturn.RentAndReturn("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
            Result = RentObj.UpdateRentAndReturn(RentAndReturn.MyCursor, RentAndReturn.MyConnection, RentAndReturnId)
        
            if Result is False:
                print("Rent and Return record does not exist!")
            else:
                CustomerTypeId = input("Enter new customer type id (leave blank to retain current): ")
                CustomerName = input("Enter new customer name (leave blank to retain current): ")
                Address = input("Enter new address (leave blank to retain current): ")
                VehicleId = input("Enter new vehicle id (leave blank to retain current): ")
                RentalDate = input("Enter new rental date (YYYY-MM-DD, leave blank to retain current): ")
                ReturnDate = input("Enter new return date (YYYY-MM-DD, leave blank to retain current): ")
                Rate = input("Enter new rate per day (leave blank to retain current): ")
                VAT = input("Enter new VAT (leave blank to retain current): ")
                RentalServiceCost = input("Enter new rental service cost (leave blank to retain current): ")
        
                RepairCost = ""
                if CustomerTypeId in ["1", "2"]:
                    RepairCost = input("Enter new repair cost (leave blank to retain current): ")
        
                Amount = ""
                AmountPaid = input("Enter new amount paid (leave blank to retain current): ")
                TotalDueAmount = ""
                PaymentConfirmation = input("Enter new payment confirmation (Y/N, leave blank to retain current): ")
                PaymentMethod = input("Enter new payment method (Cash/Card/UPI, leave blank to retain current): ")
        
                RentObj = RentAndReturn.RentAndReturn(
                    CustomerTypeId, CustomerName, Address, VehicleId,
                    RentalDate, ReturnDate, "", Rate, VAT, RentalServiceCost,
                    RepairCost, Amount, AmountPaid, TotalDueAmount,
                    PaymentConfirmation, PaymentMethod, "", ""
                )
        
                Result = RentObj.UpdateRentAndReturn(RentAndReturn.MyCursor, RentAndReturn.MyConnection, RentAndReturnId)
        
                if Result:
                    print("Rent and Return record updated successfully!")
                else:
                    print("Update failed! Invalid data.")
                    
        elif Choice == 43: 
            while True:
                RentAndReturnId = input("Enter RentAndReturn ID to delete: ")
                if RentAndReturnId == "":
                    print("ID cannot be blank!")
                else:
                    break
        
            RentObj = RentAndReturn.RentAndReturn("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
            Result = RentObj.DeleteRentAndReturn(RentAndReturn.MyCursor, RentAndReturn.MyConnection, RentAndReturnId)
        
            if Result:
                print("Rent and Return record deleted successfully!")
            else:
                print("Record not found!")
        
        elif Choice == 44:
            while True:
                RentAndReturnId = input("Enter RentAndReturn ID to view: ")
                print()
                if RentAndReturnId == "":
                    print("RentAndReturn ID cannot be blank!")
                else:
                    break
        
            RentObj = RentAndReturn.RentAndReturn("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
            Result = RentObj.ViewRentAndReturnById(RentAndReturn.MyCursor, RentAndReturn.MyConnection, RentAndReturnId)
        
            if Result is False:
                print("RentAndReturn record does not exist!")
            else:
                print("Customer Type:", Result[1],
                      "\nCustomer Name:", Result[2],
                      "\nAddress:", Result[3],
                      "\nVehicle ID:", Result[4],
                      "\nRental Date:", Result[5],
                      "\nReturn Date:", Result[6],
                      "\nNo. of Days:", Result[7],
                      "\nRate per Day:", Result[8],
                      "\nVAT:", Result[9],
                      "\nRental Service Cost:", Result[10],
                      "\nRepair Cost:", Result[11],
                      "\nAmount:", Result[12],
                      "\nAmount Paid:", Result[13],
                      "\nTotal Due Amount:", Result[14],
                      "\nPayment Confirmation:", Result[15],
                      "\nPayment Method:", Result[16],
                      "\nInvoice No:", Result[17],
                      "\nReceipt No:", Result[18])
        
        elif Choice == 45: 
            RentObj = RentAndReturn.RentAndReturn("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
            Records = RentObj.ViewAllRentAndReturn(RentAndReturn.MyCursor, RentAndReturn.MyConnection)
        
            if Records:
                Headers = ["ID", "Customer Type", "Customer Name", "Address", "Vehicle", "Rental Date",
                           "Return Date", "Days", "Rate", "VAT", "Service Cost", "Repair Cost", "Amount",
                           "Paid", "Due", "Confirmed", "Method", "Invoice", "Receipt"]
                print(tabulate(Records, headers=Headers))
            else:
                print("No Rent and Return records found!")

        elif Choice == 46:
            while True:
                RentAndReturnId = input("Enter RentAndReturn ID to print receipt/invoice: ")
                if RentAndReturnId == "":
                    print("RentAndReturn ID cannot be blank!")
                else:
                    break
        
            RentObj = RentAndReturn.RentAndReturn("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
            Record = RentObj.PrintReceiptInvoice(RentAndReturn.MyCursor, RentAndReturnId)
        
            if Record is None:
                print("RentAndReturn record does not exist!")
            else:
                if Record["InvoiceNo"] is not None:
                    Title = "INVOICE"
                    RefNo = Record["InvoiceNo"]
                else:
                    Title = "RECEIPT"
                    RefNo = Record["ReceiptNo"]
        
                headers = ["Field", "Details"]
                table = [
                    ["Reference No", RefNo],
                    ["Customer Name", Record["CustomerName"]],
                    ["Address", Record["Address"]],
                    ["Vehicle ID", Record["VehicleId"]],
                    ["Rental Date", Record["RentalDate"]],
                    ["Return Date", Record["ReturnDate"]],
                    ["No Of Days", Record["NoOfDays"]],
                    ["Rate per Day", Record["Rate"]],
                    ["VAT", Record["VAT"]],
                    ["Rental Service Cost", Record["RentalServiceCost"]],
                    ["Repair Cost", Record["RepairCost"]],
                    ["Total Amount", Record["Amount"]],
                    ["Amount Paid", Record["AmountPaid"]],
                    ["Total Due Amount", Record["TotalDueAmount"]],
                    ["Payment Method", Record["PaymentMethod"]],
                ]
        
                print("\n" + "="*50)
                print("        " + Title)
                print("="*50)
                print(tabulate(table, headers, tablefmt="grid"))
                print("="*50)

        elif Choice == 47:
            print("Log out!")
            print()
            break

def main():
    while True:
        print()
        print("1. LOGIN")
        print("2. SIGN UP")
        print("3. EXIT")
        print()
        Choice = int(input("Enter your choice (1 or 3): "))
        print()
        
        if Choice == 1:
            Attempts = 0
            MaxAttempts = 3
        
            while Attempts < MaxAttempts:
                Username = input("Enter your username: ")
                Password = input("Enter your password: ")
        
                LoginObj = Login.Login(Username, Password)
                Result = LoginObj.ValidateLogin(SignUp.MyCursor)
        
                if Result:
                    print()
                    print("Login successful!")
                    print()
                    ShowMenu(Result[3])
                    break
                else:
                    Attempts = Attempts + 1
                    print()
                    print("Invalid username or password! Attempts left:", MaxAttempts - Attempts)
                    print()
        
                    if Attempts == MaxAttempts:
                        print("You have used all 3 attempts!")
                        break
        
                    Question = input("Try again? (Y/N): ")
                    if Question.lower() == "n":
                        break
                
        elif Choice == 2:
            while True:
                Username = input("Enter your username: ")
                if Username == "":
                    input("Username cannot be blank!")
                else:
                    break
            
            while True:
                Password = input("Enter your password: ")
                if Password == "":
                    print("Password cannot be empty!")
                elif len(Password) < 8:
                    print("Password should be atleast 8 characters!")
                elif "@" not in Password and "#" not in Password:
                    print("Password should contain atleast one from (@ or #)!")
                else:
                    break
                
            while True:
                FullName = input("Enter your full name: ")
                if FullName == "":
                    print("Full name cannot be blank!")
                else:
                    break
                
            while True:
                Address = input("Enter your address: ")
                if Address == "":
                    print("Address cannot be blank!")
                else:
                    break

                
            while True:
                Email = input("Enter your email: ")
                if Email == "":
                    print("Email cannot be blank!")
                elif "@" not in Email or "." not in Email:
                    print("Invalid email format!")
                else:
                    break
                
            while True:
                PhoneNumber = input("Enter your phone number: ")
                if PhoneNumber == "":
                    print("Phone number cannot be empty!")
                elif len(PhoneNumber) != 10:
                    print("Phone number should be of 10 digits!")
                else:
                    break
                    
            SignUpObj = SignUp.SignUp(Username, Password, FullName, Address, Email, PhoneNumber)
            SignUpObj.SaveSignUp(SignUp.MyCursor, SignUp.MyConnection)
            print()
            print("User signed up successfully!")
            print()
            
        elif Choice == 3:
            print("Exiting application!")
            break

if __name__ == "__main__":
    main()
            