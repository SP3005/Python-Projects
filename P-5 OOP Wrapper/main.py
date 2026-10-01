class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.role = "Person"

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def display(self):
        print("\n+----- Person Details -----+")
        print("Name:",self.name)
        print("Age:",self.age)
        print("+--------------------------+")

class Employee(Person):
    def __init__(self,name,age,employee_id="N/A",salary=0.0):
        super().__init__(name,age)
        self.__employee_id = employee_id
        self.__salary = salary
        self.role = "Employee"

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self,employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        self.__salary = salary

    def display(self):
        print("\n+----- Employee Details -----+")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Employee ID:",self.__employee_id)
        print("Salary:",self.__salary)
        print("+----------------------------+")

class Manager(Employee):
    def __init__(self,name,age,employee_id,salary,department):
        super().__init__(name,age,employee_id,salary)
        self.department = department
        self.role = "Manager"

    def set_department(self, department):
        self.department = department

    def display(self):
        print("\n+----- Manager Details -----+")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Employee ID:",self.get_employee_id())
        print("Salary:",self.get_salary())
        print("Dapartment:",self.department)
        print("+---------------------------+")

class Developer(Employee):
    def __init__(self,name,age,employee_id,salary,programming_language):
        super().__init__(name,age,employee_id,salary)
        self.programming_language = programming_language
        self.role = "Developer"

    def set_programming_language(self, programming_language):
        self.programming_language = programming_language

    def display(self):
        print("\n+------- Developer Details -------+")
        print("Name:",self.name)
        print("Age:",self.age)
        print("Employee ID:",self.get_employee_id())
        print("Salary:",self.get_salary())
        print("Programming Language:",self.programming_language)
        print("+---------------------------------+")


persons = []

while True:
    print("+--- Employee Management System --+")
    print("| 1. Create a Person              |")
    print("| 2. Create an Employee           |")
    print("| 3. Create a Manager             |")
    print("| 4. Create a Developer           |")
    print("| 5. Show Details                 |")
    print("| 6. Update Employee              |")
    print("| 7. Remove Person                |")
    print("| 8. Check Inheritance            |")
    print("| 9. Exit                         |")
    print("+---------------------------------+")
    Choice = input("\nEnter Your Choice: ")

    if Choice == "1":
        print("\n+----- Create a Person -----+")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        person = Person(name,age)
        persons.append(person)
        print("\nPerson created successfully.")
        print("+---------------------------+")

    elif Choice == "2":
        if len(persons) == 0:
            print("\nNo person found.")
        else:
            print("\n+---- Select a Person ----+")
            for i in range(len(persons)):
                print(i+1,".",persons[i].name,"-",persons[i].role)
            print("+-------------------------+")
            person_choice = int(input("\nEnter your Choice: "))
            if person_choice >= 1 and person_choice <= len(persons):
                index = person_choice - 1
                person = persons[index]
                print("\n+------------- Create a Employee -------------+")
                employee_id = input("Enter Employee ID: ")
                salary = float(input("Enter Salary: "))
                employee = Employee(person.name,person.age,employee_id,salary)
                persons[index] = employee
                print("\nPerson assingned as Employee Successfully.")
                print("+---------------------------------------------+")
            else:
                print("\nInvaild choice.")

    elif Choice == "3":
        if len(persons) == 0:
            print("\nNo person found.")
        else:
            print("\n+---- Select a Person ----+")
            for i in range(len(persons)):
                print(i+1,".",persons[i].name,"-",persons[i].role)
            print("+-------------------------+")
            person_choice = int(input("\nEnter your choice: "))
            if person_choice >= 1 and person_choice <= len(persons):
                index = person_choice - 1
                person = persons[index]
                print("\n+------------- Create a Manager -------------+")
                employee_id = input("Enter Employee ID: ")
                salary = float(input("Emter Salary: "))
                department = input("Enter Department: ")
                manager = Manager(person.name,person.age,employee_id,salary,department)
                persons[index] = manager
                print("\nPerson assingned as Manager Successfully.")
                print("+--------------------------------------------+")
            else:
                print("\nInvaild choice.")

    elif Choice == "4":
        if len(persons) == 0:
            print("\nNo person found.")
        else:
            print("\n+---- Select a Person ----+")
            for i in range(len(persons)):
                print(i+1,".",persons[i].name,"-",persons[i].role)
            print("+-------------------------+")
            person_choice = int(input("\nEnter your choice: "))
            if person_choice >= 1 and person_choice <= len(persons):
                index = person_choice - 1
                person = persons[index]
                print("\n+------------- Create a Developer -------------+")
                employee_id = input("Enter Employee ID: ")
                salary = float(input("Emter Salary: "))
                Programming_language = input("Enter Programming Language: ")
                developer = Developer(person.name,person.age,employee_id,salary,Programming_language)
                persons[index] = developer
                print("\nPerson assingned as Manager Successfully.")
                print("+----------------------------------------------+")
            else:
                print("\nInvaild choice.")

    elif Choice == "5":
        if len(persons) == 0:
            print("\nNo person found.")
        else:
            print("\n+---- Select a Person ----+")
            for i in range(len(persons)):
                print(i+1,".",persons[i].name,"-",persons[i].role)
            print("+-------------------------+")
            person_choice = int(input("\nEnter your choice: "))
            if person_choice >= 1 and person_choice <= len(persons):
                index = person_choice - 1
                persons[index].display()
            else:
                print("\nInvalid choice.")

    elif Choice == "6":
        if len(persons) == 0:
            print("\nNo person found.")
        else:
            print("\n+---- Select a Person ----+")
            for i in range(len(persons)):
                print(i+1,".",persons[i].name,"-",persons[i].role)
            print("+-------------------------+")
            person_choice = int(input("\nEnter your choice: "))
            if person_choice >= 1 and person_choice <= len(persons):
                person = persons[person_choice - 1]
                print("\n+--- What do you want to update? ---+")
                print("| 1. Name                           |")
                print("| 2. Age                            |")
                if person.role == "Employee":
                    print("| 3. Employee ID                    |")
                    print("| 4. Salary                         |")
                elif person.role == "Manager":
                    print("| 3. Employee ID                    |")
                    print("| 4. Salary                         |")
                    print("| 5. Department                     |")
                elif person.role == "Developer":
                    print("| 3. Employee ID                    |")
                    print("| 4. Salary                         |")
                    print("| 5. Programming Language           |")
                print("+-----------------------------------+")
                update_choice = input("\nEnter your choice: ")
                
                if update_choice == "1":
                    print("\n+-------- Update name --------+") 
                    new_name = input("Enter New Name: ")
                    person.set_name(new_name)
                    print("\nName updated successfully.")
                    print("+-----------------------------+")
                elif update_choice == "2":
                    print("\n+-------- Update Age --------+")
                    new_age = input("Enter New Age: ")
                    person.set_age(new_age)
                    print("\nAge updated successfully.")
                    print("+----------------------------+")
                elif update_choice == "3" and person.role in ["Employee","Manager","Developer"]:
                    print("\n+-------- Update Employee ID --------+")
                    new_id = input("Enter New Employee ID: ")
                    person.set_employee_id(new_id)
                    print("\nEmployee ID updated successfully.")
                    print("+------------------------------------+")
                elif update_choice == "4" and person.role in ["Employee","Manager","Developer"]:
                    print("\n+-------- Update Salary --------+")
                    new_salary = float(input("Enter New Salary: "))
                    person.set_salary(new_salary)
                    print("\nSalary updated successfully.")
                    print("+-------------------------------+")
                elif update_choice == "5" and person.role == "Manager":
                    print("\n+-------- Update Department --------+")
                    new_department = input("Enter New Department: ")
                    person.set_department(new_department)
                    print("\nDepartment updated successfully.")
                    print("+-----------------------------------+")
                elif update_choice == "5" and person.role == "Developer":
                    print("\n+-------- Update Programming Language --------+")
                    new_language = input("Enter New Programming Language: ")
                    person.set_programming_language(new_language)
                    print("\nProgramming Language updated successfully.")
                    print("+---------------------------------------------+")
                else:
                    print("\nInvalid choice.")
            else:
                print("\nInvalid choice.")

                
    elif Choice == "7":
        if len(persons) == 0:
            print("\nNo person found.")
        else:
            print("\n+---- Select a Person to remove ----+")
            for i in range(len(persons)):
                print(i + 1,".",persons[i].name,"-",persons[i].role)
            print("+-----------------------------------+")
            person_choice = int(input("\nEnter your choice: "))
            if person_choice >= 1 and person_choice <= len(persons):
                removed_person = persons.pop(person_choice - 1)
                print("+-----------------------------------+")
                print("\n",removed_person.name,"removed successfully.")
                print("+-----------------------------------+")
            else:
                print("\nInvalid choice.")
                
    elif Choice == "8":
        print("\n+----------- Inheritance Check -----------+")
        print("|Employee is subclass of Person:",issubclass(Employee, Person),"    |")
        print("|Manager is subclass of Employee:",issubclass(Manager, Employee),"   |")
        print("|Developer is subclass of Employee:",issubclass(Developer, Employee)," |")
        print("+-----------------------------------------+")
                    
    elif Choice == "9":
        print("+-----------------------------+")
        print("| Exiting the system.         |")
        print("| GoodBye!                    |")
        print("+-----------------------------+")
        break
    
    else:
        print("\nInvalid choice.")
        print("Please enter a valid choice.")








        
        
