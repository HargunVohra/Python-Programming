import Patient 
import Procedure 

def main():
    
    PatientList = []
    TotalProcedureCharges = 0
    
    while True:
        print()
        print("------------------------- Medical Report -------------------------")
        print()
        FirstName = input("Enter patient's first name: ")
        MiddleName = input("Enter patient's middle name: ")
        LastName = input("Enter patient's last name: ")
        Address = input("Enter address: ")
        City = input("Enter city: ")
        State = input("Enter state: ")
        PinCode = input("Enter 6 digit pin code: ")
        PhoneNumber = input("Enter patient's phone number: ")
        EmergencyContactName = input("Enter emergency contact's name: ")
        EmergencyContactNumber = input("Enter emergency contact's number: ")
        print()
    
        PatientObj = Patient.Patient(FirstName, MiddleName, LastName, Address, City, State, PinCode, PhoneNumber, EmergencyContactName, EmergencyContactNumber)
        
        print()
        print("-------------------------- Patient's details --------------------------")
        print()
        print("Patient's first name:", PatientObj.GetFirstName())
        print("Patient's middle name:", PatientObj.GetMiddleName())
        print("Patient's last name:", PatientObj.GetLastName())        
        print("Patient's address:", PatientObj.GetAddress())
        print("Patient's city:", PatientObj.GetCity())
        print("Patient's state:", PatientObj.GetState())
        print("Patient's pin code:", PatientObj.GetPinCode())
        print("Patient's phone number:", PatientObj.GetPhoneNumer())
        print("Emergency contact's name:", PatientObj.GetEmergencyContactName())
        print("Emergency contact's phone number:", PatientObj.GetEmergencyContactNumber())
        
        PatientList.append(PatientObj)
        
        while True:
            ProcedureName = input("Enter procedure name: ")
            ProcedureDate = input("Enter procedure date (dd/mm/yyyy): ")
            PractitionerName = input("Enter practitioner's name: ")
            ProcedureCharges = float(input("Enter procedure charges: "))
            
            ProcedureObj = Procedure.Procedure(ProcedureName, ProcedureDate, PractitionerName, ProcedureCharges)
            
            print()
            print("-------------------------- Procedure details --------------------------")
            print()
            print("Procedure Name:", ProcedureObj.GetProcedureName())
            print("Procedure date:", ProcedureObj.GetProcedureDate())
            print("Practitioner name:", ProcedureObj.GetPractitionerName()) 
            print("Procedure charges:", ProcedureObj.GetProcedureCharges())
            
            TotalProcedureCharges = TotalProcedureCharges + ProcedureCharges
            
            Question = input("Do you want to add more procedures? (Y/N): ")
            if Question.lower() == "n":
                break

            print()
            print("Total procedure charges are Rs", TotalProcedureCharges)
            print()
            
                
        Question = input("Do you want to create another report? (Y/N): ")
        if Question.lower() == "n":
            break
        
if __name__ == "__main__":
    main()