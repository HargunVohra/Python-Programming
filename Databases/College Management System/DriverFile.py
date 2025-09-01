import CourseType
import Courses
import Faculty
import Subjects
import CourseSubject
import Student
import StudentRegistration
import StudentCourseMarks
from tabulate import tabulate

def main():
    while True:
        print()
        print("---------------------------- College Management System ----------------------------")
        print()
        print("1. ADD Course Type")
        print("2. UPDATE Course Type")
        print("3. DELETE Course Type")
        print("4. VIEW Course Type")
        print("5. VIEW ALL Course Types")
        print("6. ADD Course")
        print("7. UPDATE Course")
        print("8. DELETE Course")
        print("9. VIEW Course By Name")
        print("10. VIEW ALL Courses")
        print("11. ADD Faculty")
        print("12. UPDATE Faculty")
        print("13. DELETE Faculty")
        print("14. VIEW Faculty By Name")
        print("15. VIEW ALL Faculties")
        print("16. ADD Subject")
        print("17. UPDATE Subject")
        print("18. DELETE Subject")
        print("19. VIEW Subject By Name")
        print("20. VIEW ALL Subjects")
        print("21. ASSIGN Subjects To Course")
        print("22. UPDATE Assigned Subjects")
        print("23. DISMISS Assigned Subjects")
        print("24. VIEW Assigned Subjects By Id")
        print("25. VIEW ALL Assigned Subjects With Courses")
        print("26. ADD Student")
        print("27. UPDATE Student")
        print("28. DELETE Student")
        print("29. VIEW Student By Name")
        print("30. VIEW ALL Students")
        print("31. REGISTER Student")
        print("32. UPDATE Registered Student")
        print("33. UNREGISTER Student")
        print("34. VIEW Registrations By Id")
        print("35. VIEW ALL Registrations")
        print("36. ADD Course's Marks")
        print("37. UPDATE Marks")
        print("38. DELETE Marks")
        print("39. VIEW Marks By Id")
        print("40. VIEW ALL Marks")
        print("41. EXIT")
        print()
        Choice = int(input("Enter your choice (1 to 41): "))
        if Choice == 1:
            while True:
                while True:
                    CourseTypeName = input("Enter course type: ")
                    if CourseTypeName == "":
                        print("Course type cannot be blank!")
                    else:
                        break
                    
                CourseTypeObj = CourseType.CourseType(CourseTypeName)
                CourseTypeObj.SaveCourseType(CourseType.MyCursor, CourseType.MyConnection)
                print()
                print("Course type added successfully!")
                print()
                
                Question = input("Do you want to add more course types? (Y/N): ")
                if Question.lower() == "n":
                    break

        elif Choice == 2:
            while True:
                CourseTypeName = input("Enter course type to update: ")
                if CourseTypeName == "":
                    print("Course type cannot be blank!")
                else:
                    break
    
            CourseTypeObj = CourseType.CourseType(CourseTypeName)
            Result = CourseTypeObj.UpdateCourseType(CourseType.MyCursor, CourseType.MyConnection, CourseTypeName)
    
            if Result is False:
                print("Course type does not exist!")
            else:
                CourseTypeName = input("Enter new course type name (leave blank to retain current): ")
                
                CourseTypeObj = CourseType.CourseType(CourseTypeName)
                CourseTypeObj.UpdateCourseType(CourseType.MyCursor, CourseType.MyConnection, CourseTypeName)
                print("Course type updated successfully!")

        elif Choice == 3:
            while True:
                CourseTypeId = input("Enter course type id to delete: ")
                if CourseTypeId == "":
                    print("Course type id cannot be blank!")
                else:
                    break
    
            CourseTypeObj = CourseType.CourseType(CourseTypeId)
            CourseTypeObj.DeleteCourseType(CourseType.MyCursor, CourseType.MyConnection, CourseTypeId)
    
            print("Course type deleted successfully!")
                
        elif Choice == 4:
            while True:
                CourseTypeName = input("Enter course type name to view: ")
                if CourseTypeName == "":
                    print("Course type cannot be blank!")
                else:
                    break
        
            CourseTypeObj = CourseType.CourseType(CourseTypeName)
            Result = CourseTypeObj.ViewCourseType(CourseType.MyCursor, CourseType.MyConnection, CourseTypeName)
        
            if Result is False:
                print()
                print("Course type does not exist!")
                print()
            else:
                print("Course Type ID:", Result[0], "\t Course Type Name:", Result[1])
                
        elif Choice == 5:
            Results = CourseType.CourseType("").ViewAllCourseTypes(CourseType.MyCursor, CourseType.MyConnection)
            if not Results:
                print("No course types found!")
            else:
                Headers = ["Course Type ID", "Course Type Name"]
                print(tabulate(Results, headers=Headers))
            
        elif Choice == 6:
            while True:
                while True:
                    CourseName = input("Enter course's name: ")
                    if CourseName == "":
                        print("Course name cannot be blank!")
                    else:
                        break
                
                while True:
                    CourseDuration = input("Enter course duration (in months): ")
                    if CourseDuration == "":
                        print("Course duration cannot be blank!")
                    else:
                        break
                    
                while True:
                    StartDate = input("Enter start date (YYYY-MM-DD): ")
                    if StartDate == "":
                        print("Start date cannot be blank!")
                    else:
                        break
        
                while True:
                    CourseFee = input("Enter course fee: ")
                    if CourseFee == "":
                        print("Course fee cannot be empty!")
                    else:
                        CourseFee = int(CourseFee)
                        break
        
                while True:
                    CourseTypeId = input("Enter course type id: ")
                    if CourseTypeId == "":
                        print("Course type id cannot be empty!")
                    else:
                        break
        
                CourseObj = Courses.Courses(CourseName, CourseTypeId, CourseDuration, StartDate, CourseFee)
        
                Result = CourseObj.SaveCourse(Courses.MyCursor, Courses.MyConnection)
                if Result:
                    print("Course added successfully!")
                else:
                    print("No such course type id exists!")
        
                Question = input("Do you want to add more courses? (Y/N): ")
                if Question.lower() == "n":
                    break
                
        elif Choice == 7:
            while True:
                CourseName = input("Enter course name to update: ")
                if CourseName == "":
                    print("Course name cannot be blank!")
                else:
                    break
        
            CourseObj = Courses.Courses(CourseName, "", "", "", "")
            Result = CourseObj.UpdateCourse(Courses.MyCursor, Courses.MyConnection, CourseName)
        
            if Result is False:
                print("Course does not exist!")
            else:
                Name = input("Enter new course name (leave blank to retain current): ")
                Duration = input("Enter new course duration (leave blank to retain current): ")
                StartDate = input("Enter new start date (YYYY-MM-DD, leave blank to retain current): ")
                Fee = input("Enter new course fee (leave blank to retain current): ")
                CourseTypeId = input("Enter new course type id (leave blank to retain current): ")
        
                CourseObj = Courses.Courses(Name, CourseTypeId, Duration, StartDate, Fee)
                Result = CourseObj.UpdateCourse(Courses.MyCursor, Courses.MyConnection, CourseName)
                
                if Result is False:
                    if CourseTypeId != "":
                        print("Course type does not exist!")
                    else:
                        print("Course does not exist!")
                else:
                    print("Course updated successfully!")
                    
        elif Choice == 8:
            while True:
                CourseId = input("Enter course id to delete: ")
                if CourseId == "":
                    print("Course id cannot be blank!")
                else:
                    break
        
            CourseObj = Courses.Courses("", "", "", "", "")
            CourseObj.DeleteCourse(Courses.MyCursor, Courses.MyConnection, CourseId)
        
            if Result is False:
                print("Course does not exist!")
            else:
                print("Course deleted successfully!")
                
        elif Choice == 9:
            while True:
                CourseName = input("Enter course name to view: ")
                if CourseName == "":
                    print("Course name cannot be blank!")
                else:
                    break
        
            CourseObj = Courses.Courses(CourseName, "", "", "", "")
            Result = CourseObj.ViewCourse(Courses.MyCursor, Courses.MyConnection, CourseName)
        
            if Result is False:
                print()
                print("Course does not exist!")
                print()
            else:
                print("Course ID:", Result[0], 
                      "\nCourse Name:", Result[1], 
                      "\nCourse Type ID:", Result[2], 
                      "\nDuration:", Result[3], 
                      "\nStart Date:", Result[4], 
                      "\nFee:", Result[5])

        elif Choice == 10:
            Results = Courses.Courses("", "", "", "", "").ViewAllCourses(Courses.MyCursor, Courses.MyConnection)
            if not Results:
                print("No courses found!")
            else:
                Headers = ["Course ID", "Course Name", "Course Type ID", "Duration", "Start Date", "Fee"]
                print(tabulate(Results, headers=Headers))
                
        if Choice == 11:
            while True:
                while True:
                    FacultyName = input("Enter faculty name: ")
                    if FacultyName == "":
                        print("Faculty name cannot be blank!")
                    else:
                        break
                    
                while True:
                    RoomNumber = input("Enter room number: ")
                    if RoomNumber == "":
                        print("Room number cannot be blank!")
                    else:
                        break
                    
                while True:
                    MobileNumber = input("Enter mobile number: ")
                    if MobileNumber == "":
                        print("Mobile number cannot be blank!")
                    elif len(MobileNumber) != 10:
                        print("Mobile number should be of 10 digits!")
                    else:
                        break
                    
                while True:
                    Email = input("Enter email address: ")
                    if Email == "":
                        print("Email cannot be blank!")
                    elif "@" not in Email or "." not in Email:
                        print("Invalid email address format!")
                    else:
                        break
                    
                FacultyObj = Faculty.Faculty(FacultyName, RoomNumber, MobileNumber, Email)
                FacultyObj.SaveFaculty(Faculty.MyCursor, Faculty.MyConnection)
                print()
                print("Faculty added successfully!")
                print()
                
                Question = input("Do you want to add more course types? (Y/N): ")
                if Question.lower() == "n":
                    break
                
        elif Choice == 12:
            while True:
                FacultyName = input("Enter faculty name to update: ")
                if FacultyName == "":
                    print("Faculty name cannot be blank!")
                else:
                    break
        
            FacultyObj = Faculty.Faculty(FacultyName, "", "", "")
            Result = FacultyObj.UpdateFaculty(Faculty.MyCursor, Faculty.MyConnection, FacultyName)
        
            if Result is False:
                print("Faculty does not exist!")
            else:
                Name = input("Enter new faculty name (leave blank to retain current): ")
                RoomNumber = input("Enter new room number (leave blank to retain current): ")
                MobileNumber = input("Enter new mobile number (leave blank to retain current): ")
                Email = input("Enter new email address (leave blank to retain current): ")
        
                FacultyObj = Faculty.Faculty(Name, RoomNumber, MobileNumber, Email)
                Result = FacultyObj.UpdateFaculty(Faculty.MyCursor, Faculty.MyConnection, FacultyName)
                if Result is False:
                    print("Faculty does not exist!")
                else:
                    print("Faculty updated successfully!")
                    
        elif Choice == 13:
            while True:
                FacultyId = input("Enter faculty id to delete: ")
                if FacultyId == "":
                    print("Faculty id cannot be blank!")
                else:
                    break
        
            FacultyObj = Faculty.Faculty("", "", "", "")
            Result = FacultyObj.DeleteFaculty(Faculty.MyCursor, Faculty.MyConnection, FacultyId)
        
            if Result is False:
                print("Faculty does not exist!")
            else:
                print("Faculty deleted successfully!")
                
        elif Choice == 14:
            while True:
                FacultyName = input("Enter faculty name to view: ")
                if FacultyName == "":
                    print("Faculty name cannot be blank!")
                else:
                    break
        
            FacultyObj = Faculty.Faculty("", "", "", "")
            Result = FacultyObj.ViewFaculty(Faculty.MyCursor, Faculty.MyConnection, FacultyName)
        
            if Result is False:
                print()
                print("Faculty does not exist!")
                print()
            else:
                print("Faculty ID:", Result[0],
                      "\nFaculty Name:", Result[1],
                      "\nRoom Number:", Result[2],
                      "\nMobile Number:", Result[3],
                      "\nEmail:", Result[4])
        
        elif Choice == 15:
            Results = Faculty.Faculty("", "", "", "").ViewAllFaculties(Faculty.MyCursor, Faculty.MyConnection)
            if not Results:
                print("No faculties found!")
            else:
                Headers = ["Faculty ID", "Faculty Name", "Room Number", "Mobile Number", "Email"]
                print(tabulate(Results, headers=Headers))
                
        elif Choice == 16:
            while True:
                while True:
                    SubjectName = input("Enter subject name: ")
                    if SubjectName == "":
                        print("Subject name cannot be blank!")
                    else:
                        break
        
                while True:
                    NumberOfCredits = input("Enter number of credits: ")
                    if NumberOfCredits == "":
                        print("Number of credits cannot be blank!")
                    else:
                        break
        
                while True:
                    FacultyId = input("Enter faculty id: ")
                    if FacultyId == "":
                        print("Faculty id cannot be blank!")
                    else:
                        break
        
                SubjectObj = Subjects.Subjects(SubjectName, NumberOfCredits, FacultyId)
                Result = SubjectObj.SaveSubject(Subjects.MyCursor, Subjects.MyConnection)
        
                print()
                if Result is False:
                    print("Faculty does not exist!")
                else:
                    print("Subject added successfully!")
                print()
        
                Question = input("Do you want to add more subjects? (Y/N): ")
                if Question.lower() == "n":
                    break
                
        elif Choice == 17:
            while True:
                SubjectName = input("Enter subject name to update: ")
                if SubjectName == "":
                    print("Subject name cannot be blank!")
                else:
                    break

            SubjectObj = Subjects.Subjects(SubjectName, "", "")
            Result = SubjectObj.UpdateSubject(Subjects.MyCursor, Subjects.MyConnection, SubjectName)

            if Result is False:
                print("Subject does not exist!")
            else:
                Name = input("Enter new subject name (leave blank to retain current): ")
                NumberOfCredits = input("Enter new number of credits (leave blank to retain current): ")
                FacultyId = input("Enter new faculty id (leave blank to retain current): ")

                SubjectObj = Subjects.Subjects(Name, NumberOfCredits, FacultyId)
                Result = SubjectObj.UpdateSubject(Subjects.MyCursor, Subjects.MyConnection, SubjectName)
                if Result is False:
                    if FacultyId != "":
                        print("Faculty does not exist!")
                    else:
                        print("Subject does not exist!")
                else:
                    print("Subject updated successfully!")
                    
        elif Choice == 18:
            while True:
                SubjectId = input("Enter subject id to delete: ")
                if SubjectId == "":
                    print("Subject id cannot be blank!")
                else:
                    break
        
            SubjectObj = Subjects.Subjects("", "", "")
            Result = SubjectObj.DeleteSubject(Subjects.MyCursor, Subjects.MyConnection, SubjectId)
        
            if Result is False:
                print("Subject does not exist!")
            else:
                print("Subject deleted successfully!")
                
        elif Choice == 19:
            while True:
                SubjectName = input("Enter subject name to view: ")
                if SubjectName == "":
                    print("Subject name cannot be blank!")
                else:
                    break
        
            SubjectObj = Subjects.Subjects("", "", "")
            Result = SubjectObj.ViewSubject(Subjects.MyCursor, Subjects.MyConnection, SubjectName)
        
            if Result is False:
                print()
                print("Subject does not exist!")
                print()
            else:
                print("Subject ID:", Result[0],
                      "\nSubject Name:", Result[1],
                      "\nNumber Of Credits:", Result[2],
                      "\nFaculty ID:", Result[3])
        
        elif Choice == 20:
            Results = Subjects.Subjects("", "", "").ViewAllSubjects(Subjects.MyCursor, Subjects.MyConnection)
            if not Results:
                print("No subjects found!")
            else:
                Headers = ["Subject ID", "Subject Name", "Number Of Credits", "Faculty ID"]
                print(tabulate(Results, headers=Headers))
                
        elif Choice == 21:
            while True:
                while True:
                    CourseId = input("Enter course id you want to assign subject to: ")
                    if CourseId == "":
                        print("Course id cannot be blank!")
                    else:
                        break
                    
                while True:
                    SubjectId = input("Enter subject id you want to assign course to: ")
                    if SubjectId == "":
                        print("Subject id cannot be blank!")
                    else:
                        break
                    
                CourseSubjectObj = CourseSubject.CourseSubject(CourseId, SubjectId)
                Result = CourseSubjectObj.AssignSubjectToCourse(CourseSubject.MyCursor, CourseSubject.MyConnection)
            
                if Result == "Course":
                    print("Course id does not exist!")
                elif Result == "Subject":
                    print("Subject id does not exist!")
                else:
                    print("Subject assigned to course successfully!")
                    
                Question = input("Do you want to assign more subjects to courses? (Y/N): ")
                if Question.lower() == "n":
                    break
        
        elif Choice == 22:
            while True:
                CourseId = input("Enter course id of the current assignment: ")
                if CourseId == "":
                    print("Course id cannot be blank!")
                else:
                    break
        
            while True:
                SubjectId = input("Enter subject id of the current assignment: ")
                if SubjectId == "":
                    print("Subject id cannot be blank!")
                else:
                    break
        
            CheckObj = CourseSubject.CourseSubject("", "")
            Result = CheckObj.UpdateAssignedSubject(CourseSubject.MyCursor, CourseSubject.MyConnection, CourseId, SubjectId)
        
            if Result == "Assignment":
                print("This assignment does not exist!")
            else:
                NewCourseId = input("Enter new course id (leave blank to retain current): ")
                NewSubjectId = input("Enter new subject id (leave blank to retain current): ")
        
                CourseSubjectObj = CourseSubject.CourseSubject(NewCourseId, NewSubjectId)
                Result = CourseSubjectObj.UpdateAssignedSubject(CourseSubject.MyCursor, CourseSubject.MyConnection, CourseId, SubjectId)
        
                if Result == "Course":
                    print("New course id does not exist!")
                elif Result == "Subject":
                    print("New subject id does not exist!")
                else:
                    print("Assignment updated successfully!")
                    
        elif Choice == 23:
            while True:
                CourseId = input("Enter course id of the assignment to dismiss: ")
                if CourseId == "":
                    print("Course id cannot be blank!")
                else:
                    break
        
            while True:
                SubjectId = input("Enter subject id of the assignment to dismiss: ")
                if SubjectId == "":
                    print("Subject id cannot be blank!")
                else:
                    break
        
            CourseSubjectObj = CourseSubject.CourseSubject("", "")
            Result = CourseSubjectObj.DismissAssignedSubject(CourseSubject.MyCursor, CourseSubject.MyConnection, CourseId, SubjectId)
        
            if Result == "Assignment":
                print("This assignment does not exist!")
            else:
                print("Assignment dismissed successfully!")
                
        elif Choice == 24:
            while True:
                CourseId = input("Enter course id to view assigned subjects: ")
                if CourseId == "":
                    print("Course id cannot be blank!")
                else:
                    break
        
            CourseSubjectObj = CourseSubject.CourseSubject(CourseId, "")
            Results = CourseSubjectObj.ViewAssignedSubjectsByName(CourseSubject.MyCursor, CourseSubject.MyConnection, CourseId)
        
            if not Results:
                print("No subjects assigned to this course!")
            else:
                Headers = ["Course ID", "Subject ID", "Subject Name"]
                print(tabulate(Results, headers=Headers))
        
        
        elif Choice == 25:
            CourseSubjectObj = CourseSubject.CourseSubject("", "")
            Results = CourseSubjectObj.ViewAllAssignedSubjects(CourseSubject.MyCursor, CourseSubject.MyConnection)
        
            if not Results:
                print("No assigned subjects found!")
            else:
                Headers = ["Course ID", "Course Name", "Subject ID", "Subject Name"]
                print(tabulate(Results, headers=Headers))
                
        elif Choice == 26:
            while True:
                while True:
                    Name = input("Enter student name: ")
                    if Name == "":
                        print("Student name cannot be blank!")
                    else:
                        break
            
                while True:
                    Address = input("Enter address: ")
                    if Address == "":
                        print("Address cannot be blank!")
                    else:
                        break
            
                while True:
                    City = input("Enter city: ")
                    if City == "":
                        print("City cannot be blank!")
                    else:
                        break
            
                while True:
                    State = input("Enter state: ")
                    if State == "":
                        print("State cannot be blank!")
                    else:
                        break
            
                while True:
                    ZipCode = input("Enter zip code: ")
                    if ZipCode == "":
                        print("Zip code cannot be blank!")
                    elif len(ZipCode) != 6:
                        print("Zip code must be of 6 digits!")
                    else:
                        break
            
                while True:
                    MobileNumber = input("Enter mobile number: ")
                    if MobileNumber == "":
                        print("Mobile number cannot be blank!")
                    elif len(MobileNumber) != 10:
                        print("Mobile number must be of 10 digits!")
                    else:
                        break
            
                while True:
                    Email = input("Enter email: ")
                    if Email == "":
                        print("Email cannot be blank!")
                    elif "@" not in Email or "." not in Email:
                        print("Invalid email format!")
                    else:
                        break
            
                while True:
                    DateOfBirth = input("Enter date of birth (YYYY-MM-DD): ")
                    if DateOfBirth == "":
                        print("Date of birth cannot be blank!")
                    else:
                        break
            
                while True:
                    Gender = input("Enter gender (Male/Female): ")
                    if Gender == "":
                        print("Gender cannot be blank!")
                    else:
                        break
            
                StudentObj = Student.Student(Name, Address, City, State, ZipCode, MobileNumber, Email, DateOfBirth, Gender)
                StudentObj.SaveStudent(Student.MyCursor, Student.MyConnection)
            
                print()
                print("Student added successfully!")
                print()
            
                Question = input("Do you want to add more students? (Y/N): ")
                if Question.lower() == "n":
                    break
        
        elif Choice == 27:
            while True:
                StudentName = input("Enter student name to update: ")
                if StudentName == "":
                    print("Student name cannot be blank!")
                else:
                    break
        
            StudentObj = Student.Student("", "", "", "", "", "", "", "", "")
            Result = StudentObj.UpdateStudent(Student.MyCursor, Student.MyConnection, StudentName)
        
            if Result is False:
                print("Student does not exist!")
            else:
                Name = input("Enter new student name (leave blank to retain current): ")
                Address = input("Enter new address (leave blank to retain current): ")
                City = input("Enter new city (leave blank to retain current): ")
                State = input("Enter new state (leave blank to retain current): ")
                ZipCode = input("Enter new zip code (leave blank to retain current): ")
                MobileNumber = input("Enter new mobile number (leave blank to retain current): ")
                Email = input("Enter new email (leave blank to retain current): ")
                DateOfBirth = input("Enter new date of birth (YYYY-MM-DD, leave blank to retain current): ")
                Gender = input("Enter new gender (leave blank to retain current): ")
        
                StudentObj = Student.Student(Name, Address, City, State, ZipCode, MobileNumber, Email, DateOfBirth, Gender)
                Result = StudentObj.UpdateStudent(Student.MyCursor, Student.MyConnection, StudentName)
        
                if Result is False:
                    print("Student does not exist!")
                else:
                    print("Student updated successfully!")
        
        elif Choice == 28:
            while True:
                StudentId = input("Enter student id to delete: ")
                if StudentId == "":
                    print("Student id cannot be blank!")
                else:
                    break
        
            StudentObj = Student.Student("", "", "", "", "", "", "", "", "")
            Result = StudentObj.DeleteStudent(Student.MyCursor, Student.MyConnection, StudentId)
        
            if Result is False:
                print("Student does not exist!")
            else:
                print("Student deleted successfully!")
                
        elif Choice == 29:
            while True:
                StudentName = input("Enter student name to view: ")
                if StudentName == "":
                    print("Student name cannot be blank!")
                else:
                    break
        
            StudentObj = Student.Student("", "", "", "", "", "", "", "", "")
            Result = StudentObj.ViewStudent(Student.MyCursor, Student.MyConnection, StudentName)
        
            if Result is False:
                print()
                print("Student does not exist!")
                print()
            else:
                print("Student ID:", Result[0],
                      "\nStudent Name:", Result[1],
                      "\nAddress:", Result[2],
                      "\nCity:", Result[3],
                      "\nState:", Result[4],
                      "\nZipCode:", Result[5],
                      "\nMobile Number:", Result[6],
                      "\nEmail:", Result[7],
                      "\nDate Of Birth:", Result[8],
                      "\nGender:", Result[9])
                
        elif Choice == 30:
            StudentObj = Student.Student("", "", "", "", "", "", "", "", "")
            Results = StudentObj.ViewAllStudents(Student.MyCursor, Student.MyConnection)
        
            if not Results:
                print("No students found!")
            else:
                Headers = ["Student ID", "Student Name", "Address", "City", "State", "ZipCode", "Mobile Number", "Email", "Date Of Birth", "Gender"]
                print(tabulate(Results, headers=Headers))
                
        elif Choice == 31:
            while True:
                while True:
                    RegistrationNumber = input("Enter registration number: ")
                    if RegistrationNumber == "":
                        print("Registration number cannot be blank!")
                    else:
                        break
            
                while True:
                    RegistrationDate = input("Enter registration date (YYYY-MM-DD): ")
                    if RegistrationDate == "":
                        print("Registration date cannot be blank!")
                    else:
                        break
            
                while True:
                    StudentId = input("Enter student id to register: ")
                    if StudentId == "":
                        print("Student id cannot be blank!")
                    else:
                        break
            
                while True:
                    CourseId = input("Enter course id for registration: ")
                    if CourseId == "":
                        print("Course id cannot be blank!")
                    else:
                        break
            
                while True:
                    FeePaid = int(input("Enter fee paid: "))
                    if FeePaid == "":
                        print("Fee paid cannot be blank!")
                    else:
                        break
            
                StudentRegistrationObj = StudentRegistration.StudentRegistration(
                    RegistrationNumber, RegistrationDate, StudentId, CourseId, "", FeePaid, ""
                )
            
                Result = StudentRegistrationObj.RegisterStudent(StudentRegistration.MyCursor, StudentRegistration.MyConnection)
            
                if Result == "Student":
                    print("Student id does not exist!")
                elif Result == "Course":
                    print("Course id does not exist!")
                elif Result == "Duplicate":
                    print("This student is already registered for this course!")
                else:
                    print("Student registered successfully!")
                    
                Question = input("Dpo you want to register more students? (Y/N): ")
                if Question.lower() == "n":
                    break
                
        elif Choice == 32:
            while True:
                RegistrationNumber = input("Enter registration number to update: ")
                if RegistrationNumber == "":
                    print("Registration number cannot be blank!")
                else:
                    break

            StudentRegistrationObj = StudentRegistration.StudentRegistration(
                RegistrationNumber, "", "", "", "", "", ""
            )
            Result = StudentRegistrationObj.UpdateRegisteredStudent(
                StudentRegistration.MyCursor, StudentRegistration.MyConnection, RegistrationNumber
            )

            if Result == "Registration":
                print("Registration does not exist!")
            elif Result == "Student":
                print("New student id does not exist!")
            elif Result == "Course":
                print("New course id does not exist!")
            else:
                RegistrationDate = input("Enter new registration date (YYYY-MM-DD, leave blank to retain current): ")
                StudentId = input("Enter new student id (leave blank to retain current): ")
                CourseId = input("Enter new course id (leave blank to retain current): ")
                FeePaid = input("Enter new fee paid (leave blank to retain current): ")

                StudentRegistrationObj = StudentRegistration.StudentRegistration(RegistrationNumber, RegistrationDate, StudentId, CourseId, "", FeePaid, ""
                )
                Result = StudentRegistrationObj.UpdateRegisteredStudent(
                    StudentRegistration.MyCursor, StudentRegistration.MyConnection, RegistrationNumber
                )

                if Result == "Student":
                    print("New student id does not exist!")
                elif Result == "Course":
                    print("New course id does not exist!")
                else:
                    print("Registration updated successfully!")

        elif Choice == 33:
            while True:
                RegistrationNumber = input("Enter registration number to unregister: ")
                if RegistrationNumber == "":
                    print("Registration number cannot be blank!")
                else:
                    break

            StudentRegistrationObj = StudentRegistration.StudentRegistration(
                RegistrationNumber, "", "", "", "", "", ""
            )
            Result = StudentRegistrationObj.UnregisterStudent(
                StudentRegistration.MyCursor, StudentRegistration.MyConnection, RegistrationNumber
            )

            if Result is False:
                print("Registration does not exist!")
            else:
                print("Registration deleted successfully!")
        
        elif Choice == 34:
            while True:
                RegistrationNumber = input("Enter registration number to view: ")
                if RegistrationNumber == "":
                    print("Registration number cannot be blank!")
                else:
                    break
        
            StudentRegistrationObj = StudentRegistration.StudentRegistration("", "", "", "", "", "", "")
            Result = StudentRegistrationObj.ViewRegistration(StudentRegistration.MyCursor, StudentRegistration.MyConnection, RegistrationNumber)
        
            if Result is False:
                print("Registration does not exist!")
            else:
                print("Registration Number:", Result[0],
                      "\nRegistration Date:", Result[1],
                      "\nStudent Name:", Result[2],
                      "\nCourse Name:", Result[3],
                      "\nCourse Fee:", Result[4],
                      "\nFee Paid:", Result[5],
                      "\nBalance Fee:", Result[6])
        
        elif Choice == 35:
            StudentRegistrationObj = StudentRegistration.StudentRegistration("", "", "", "", "", "", "")
            Results = StudentRegistrationObj.ViewAllRegistrations(StudentRegistration.MyCursor, StudentRegistration.MyConnection)
        
            if not Results:
                print("No registrations found!")
            else:
                Headers = ["Registration Number", "Registration Date", "Student Name", "Course Name", "Course Fee", "Fee Paid", "Balance Fee"]
                print(tabulate(Results, headers=Headers))
                
        elif Choice == 36:
            while True:
                StudentId = input("Enter student id: ")
                CourseId = input("Enter course id: ")
        
                StudentCourseMarksObj = StudentCourseMarks.StudentCourseMarks(StudentId, CourseId, "", "")
        
                AssignedSubjects = StudentCourseMarksObj.GetAssignedSubjects(
                    StudentCourseMarks.MyCursor, StudentCourseMarks.MyConnection, CourseId
                )
        
                CheckResult = StudentCourseMarksObj.SaveStudentCourseMarks(StudentCourseMarks.MyCursor, StudentCourseMarks.MyConnection, StudentId, CourseId, []
                )
        
                if CheckResult == "Student":
                    print("Student id does not exist!")
                elif CheckResult == "Course":
                    print("Course id does not exist!")
                elif CheckResult == "Registration":
                    print("Student is not registered in this course!")
                elif CheckResult == "NoSubjects":
                    print("No subjects assigned to this course!")
                else:
                    MarksList = []
                    for Subject in AssignedSubjects:
                        SubjectId, SubjectName = Subject
                        while True:
                            Marks = input("Enter marks for " + SubjectName + ": ")
                            if Marks == "":
                                print("Marks cannot be blank!")
                            else:
                                break
                        MarksList.append(Marks)
        
                    Result = StudentCourseMarksObj.SaveStudentCourseMarks( StudentCourseMarks.MyCursor, StudentCourseMarks.MyConnection, StudentId, CourseId, MarksList
                    )
        
                    if Result == "Mismatch":
                        print("Number of marks does not match number of subjects!")
                    elif Result == "Duplicate":
                        print("Marks already exist for one of the subjects!")
                    elif Result is True:
                        print("Marks inserted successfully!")
        
                Question = input("Do you want to allot marks to more students? (Y/N): ")
                if Question.lower() == "n":
                    break
        
        elif Choice == 37:
            StudentId = input("Enter student id: ")
            CourseId = input("Enter course id: ")
    
            StudentCourseMarksObj = StudentCourseMarks.StudentCourseMarks(StudentId, CourseId, "", "")
    
            AssignedSubjects = StudentCourseMarksObj.GetAssignedSubjects(
                StudentCourseMarks.MyCursor, StudentCourseMarks.MyConnection, CourseId
            )
    
            CheckResult = StudentCourseMarksObj.UpdateStudentCourseMarks(
                StudentCourseMarks.MyCursor, StudentCourseMarks.MyConnection, StudentId, CourseId, []
            )
    
            if CheckResult == "Student":
                print("Student id does not exist!")
            elif CheckResult == "Course":
                print("Course id does not exist!")
            elif CheckResult == "Registration":
                print("Student is not registered in this course!")
            elif CheckResult == "NoSubjects":
                print("No subjects assigned to this course!")
            elif CheckResult == "NoMarks":
                print("No marks exist for this student in this course!")
            else:
                MarksList = []
                for Subject in AssignedSubjects:
                    SubjectId, SubjectName = Subject
                    Marks = input("Enter new marks for " + SubjectName + " (leave blank to retain current): ")
                    MarksList.append(Marks)
    
                Result = StudentCourseMarksObj.UpdateStudentCourseMarks(
                    StudentCourseMarks.MyCursor, StudentCourseMarks.MyConnection, StudentId, CourseId, MarksList
                )
    
                if Result == "Mismatch":
                    print("Number of marks does not match number of subjects!")
                elif Result == "NoMarks":
                    print("No marks exist for this student in this course!")
                elif Result is True:
                    print("Marks updated successfully!")
                    
        elif Choice == 38:
            StudentId = input("Enter student id: ")
            CourseId = input("Enter course id: ")
    
            StudentCourseMarksObj = StudentCourseMarks.StudentCourseMarks(StudentId, CourseId, "", "")
            Result = StudentCourseMarksObj.DeleteStudentCourseMarks(
                StudentCourseMarks.MyCursor, StudentCourseMarks.MyConnection, StudentId, CourseId
            )
    
            if Result == "Student":
                print("Student id does not exist!")
            elif Result == "Course":
                print("Course id does not exist!")
            elif Result == "Registration":
                print("Student is not registered in this course!")
            elif Result == "NoMarks":
                print("No marks exist for this student in this course!")
            elif Result is True:
                print("Marks deleted successfully!")
                
        elif Choice == 39:
            while True:
                StudentId = input("Enter student id: ")
                if StudentId == "":
                    print("Student id cannot be blank!")
                else:
                    break
        
            while True:
                CourseId = input("Enter course id: ")
                if CourseId == "":
                    print("Course id cannot be blank!")
                else:
                    break
        
            StudentCourseMarksObj = StudentCourseMarks.StudentCourseMarks("", "", "", "")
            Result = StudentCourseMarksObj.ViewStudentCourseMarks(
                StudentCourseMarks.MyCursor, StudentCourseMarks.MyConnection, StudentId, CourseId
            )
        
            if Result is False:
                print("No marks found for this student in this course!")
            else:
                TotalObtained = 0
                TotalSubjects = len(Result)
                StudentName = Result[0][0]
                CourseName = Result[0][1]
        
                print("Student Name:", StudentName,
                      "\nCourse Name:", CourseName)
        
                for Row in Result:
                    SubjectName = Row[2]
                    Marks = int(Row[3])
                    TotalObtained += Marks
        
                    print("\nSubject Name:", SubjectName,
                          "\nMarks:", Marks, "/ 100")
        
                TotalMarks = TotalSubjects * 100
                Percentage = (TotalObtained / TotalMarks) * 100
        
                if Percentage >= 90:
                    Grade = "A+"
                elif Percentage >= 80:
                    Grade = "A"
                elif Percentage >= 70:
                    Grade = "B+"
                elif Percentage >= 60:
                    Grade = "B"
                elif Percentage >= 50:
                    Grade = "C"
                elif Percentage >= 40:
                    Grade = "D"
                else:
                    Grade = "F" 
        
                print("\nTotal Obtained:", TotalObtained, "/", TotalMarks,
                      "\nPercentage:", round(Percentage, 2), "%",
                      "\nGrade:", Grade)
        
        elif Choice == 40:
            StudentCourseMarksObj = StudentCourseMarks.StudentCourseMarks("", "", "", "")
            Results = StudentCourseMarksObj.ViewAllStudentCourseMarks(
                StudentCourseMarks.MyCursor, StudentCourseMarks.MyConnection
            )
        
            if not Results:
                print("No marks found!")
            else:
                Headers = ["Student Name", "Course Name", "Subject Name", "Marks"]
                print(tabulate(Results, headers=Headers))
        
        elif Choice == 41:
            print("Exiting Application!")
            break

if __name__ == "__main__":
    main()