students = []
print("\n+-------------------------------------------+")
print("|  Welcome to the student data oraganizer!  |")
print("+-------------------------------------------+")

while True:
    print("\n~~~~~ Select an option: ~~~~~~")
    print("(1) Add Student \n(2) View All Student \n(3) Search a Student \n(4) Update a Student \n(5) Delete a Student \n(6) Display Subjects Offered \n(7) Delete All Students \n(8) Count Students \n(9) Display Students by Grade \n(10) Exit")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    choice = int(input("Enter your Choice = "))

    match choice:
        case 1:
            print("\n+------------- ADD STUDENT -------------+")
            student_id = int(input("Student ID: "))
            name = input("Name: ")
            age = int(input("Age: "))
            grade = input("Grade: ")
            dob = input("Date of Birth (YYYY-MM-DD): ")
            subject_input = input("Subjects (comma-separated): ")
            
            subjects = set()
            
            for subject in subject_input.split(","):
                subjects.add(subject.strip())
                
            unique_info = (student_id, dob)
            
            student = {"unique_info": unique_info,"name": name,"age": age,"grade": grade,"subjects": subjects}
            students.append(student)
            
            print("\n✅ Student added successfully!")
            print("\n+---------------------------------------+")
            
        case 2:
            print("\n+----------------------------- Display All Students -----------------------------+\n")

            if len(students) == 0:
                print("\n✖ No student records found.")
            else:
                for student in students:
                    student_id = student["unique_info"][0]
                    print(f"Student ID: {student_id} | " f"Name: {student['name']} | " f"Age: {student['age']} | " f"Grade: {student['grade']} | " f"Subjects: " f"{', '.join(student['subjects'])}")
            print("\n+--------------------------------------------------------------------------------+")
            
        case 3:
             print("\n+----------------------------- Search Student -----------------------------+")
             student_id = int(input("Enter Student ID: "))
             found = False
             for student in students:
                 if student["unique_info"][0] == student_id:
                     print("\nStudent Found!\n")
                     print(f"Student ID: {student_id} | " f"Name: {student['name']} | " f"Age: {student['age']} | " f"Grade: {student['grade']} | " f"Subjects: " f"{', '.join(student['subjects'])}")
                     found = True
                     break
                 if found == False:
                    print("Student not found.")
             print("\n+--------------------------------------------------------------------------+")
        case 4:
            print("\n+----- Update Student Information ------+")
            student_id = int(input("Enter Student ID: "))
            found = False
            for student in students:
                if student["unique_info"][0] == student_id:
                    found = True
                    print("\nWhat do you want to update?")
                    print("1. Update Name")
                    print("2. Update Age")
                    print("3. Update Grade")
                    print("4. Update Date of Birth")
                    print("5. Update Subjects")
                    update_choice = int(
                        input("Enter your choice: ")
                    )
                    match update_choice:
                        case 1:
                            new_name = input("Enter New Name: ")
                            student["name"] = new_name
                            print("\n✅ Name updated successfully!")
                        case 2:
                            new_age = int(input("Enter New Age: "))
                            student["age"] = new_age
                            print("\n✅ Age updated successfully!")
                        case 3:
                            new_grade = input("Enter New Grade: ")
                            student["grade"] = new_grade
                            print("\n✅ Grade updated successfully!")
                        case 4:
                            new_dob = input("Enter New Date of Birth ""(YYYY-MM-DD): ")
                            student["unique_info"] = (student_id,new_dob)
                            print("\n✅ Date of Birth updated successfully!")
                        case 5:
                            subject_input = input("Enter New Subjects ""(comma-separated): ")
                            new_subjects = set()
                            for subject in subject_input.split(","):
                                new_subjects.add(subject.strip())
                            student["subjects"] = new_subjects
                            print(
                                "\n✅ Subjects updated successfully!"
                            )
                        case _:
                            print("Invalid choice!")
                    break
            if found == False:
                print("\n✖ Student ID not found.")
            print("\n+---------------------------------------+")   
        case 5:
            print("\n+---------- Delete a Student ----------+")
            student_id = int(input("Enter Student ID to delete: "))
            found = False

            for i in range(len(students)):
                if students[i]["unique_info"][0] == student_id:
                    students.pop(i)
                    found = True
                    print("\n✅ Student deleted Successfully!")
                    break

            if found == False:
                print("Student ID not found.")

            print("\n+--------------------------------------+")
            
        case 6:
            print("\n+---------- Subjects Offered ----------+")
            all_subject = set()
            for student in students:
                all_subject.update(student["subjects"])
            if len(all_subject) == 0:
                print("\n✖ No subjects available.")
            else:
                print("Unique Subjects:")
                for subject in sorted(all_subject):
                    print("-", subject)
            print("\n+--------------------------------------+")
        case 7:
            print("\n+-------- Delete All Students ---------+")
            if len(students) == 0:
                print("\n✖ No student records found.")
            else:
                students.clear()
                print("\n✅ All student records deleted successfully!")
            print("\n+--------------------------------------+")
        case 8:
            print("\n+--- Students Count ---+")
            print("\nTotal Students: ", len(students))
            print("\n+----------------------+")
        case 9:
            print("\n+--------- Students by Grade ---------+")
            grade = input("Enter Grade: ")
            found = False
            for student in students:
                if student["grade"] == grade:
                    print(f"Student ID:" f"{student['unique_info'][0]} | " f"Name: {student['name']} | " f"Age: {student['age']} | " f"Grade: {student['grade']} | ")
                    found = True
            if found == False:
                print("\n✖ No student found with this grade.")
                
            print("\n+-------------------------------------+")
        case 10:
            print("\nThank you for using the Student Data Organizer!")
            print("\n✅ Program exited successfully.")
            break
        case _:
            print("\nInvalid choice! Please try again.")
        
        
