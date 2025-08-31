from tabulate import tabulate
import EmployeeClass as EC
import pickle
import os

def main():
    filename = "employee_data.pkl"

    if os.path.exists(filename):
        with open(filename, "rb") as file:
            EmployeeData = pickle.load(file)
    else:
        EmployeeData = {}    
    
    while True:
        if EmployeeData:
            Table = []
            for emp in EmployeeData.values():
                Table.append([
                    emp.GetEmployeeName(),
                    emp.GetEmployeeId(),
                    emp.GetDepartment(),
                    emp.GetJobTitle()
                ])
            print()
            print("------------------ Employee Records ------------------")
            print()
            print(tabulate(Table, headers=["Name", "ID", "Department", "Job Title"]))
        else:
            print()
            print("No employee records found.")

        print()
        print("------------------- Employee Management ------------------------")
        print()
        print("1. Add Employee")
        print("2. Edit Employee")
        print("3. Delete Employee")
        print("4. Exit")
        print()
        Choice = int(input("Enter your choice (1 to 4): "))
        
        if Choice == 1:
            EmployeeId = input("Enter employee id: ")
            
            EmployeeName = input("Enter employee name: ")
            Department = input("Enter employee's department: ")
            JobTitle = input("Enter job title: ")
            EmployeeObj = EC.Employee(EmployeeName, EmployeeId, Department, JobTitle)
            EmployeeData[EmployeeId] = EmployeeObj
            print("Employee added successfully.")
        
        elif Choice == 2:
            EmployeeId = input("Enter employee id to edit: ")
            if EmployeeId in EmployeeData:
                EmployeeName = input("Enter new employee name: ")
                Department = input("Enter new department: ")
                JobTitle = input("Enter new job title: ")
                EmployeeData[EmployeeId].SetEmployeeName(EmployeeName)
                EmployeeData[EmployeeId].SetDepartment(Department)
                EmployeeData[EmployeeId].SetJobTitle(JobTitle)
                print("Employee updated successfully.")
            else:
                print("Employee ID not found.")
                
        elif Choice == 3:
            EmployeeId = input("Enter employee id to delete: ")
            if EmployeeId in EmployeeData:
                del EmployeeData[EmployeeId]
                print("Employee deleted successfully.")
            else:
                print("Employee ID not found.")
            
        elif Choice == 4:
            with open(filename, "wb") as file:
                pickle.dump(EmployeeData, file)
            print("Data saved. Exiting application!")
            break

if __name__ == "__main__":
    main()
