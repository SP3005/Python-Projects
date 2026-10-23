import datetime 
import time
import math
import random
import string
import uuid

from toolkit.file_operations import create_file, write_file, read_file, append_file
from toolkit.math_operations import factorial, compound_interest, trigonometric_calation, area_of_shape


def datetime_menu():
    while True:
        print("\nDate and Time Operations:")
        print("1. Current Date and Time")
        print("2. calculate the difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Calculate Working Hours")
        print("7. Back to Main Menu")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            current_datetime = datetime.datetime.now()
            print("Current Date and Time:", current_datetime)
        elif choice == '2':
            try:
                first_date = input("Enter the first date (YYYY-MM-DD): ")
                second_date = input("Enter the second date (YYYY-MM-DD): ")
                date1 = datetime.datetime.strptime(first_date, "%Y-%m-%d")
                date2 = datetime.datetime.strptime(second_date, "%Y-%m-%d")
                difference = abs(date2 - date1)
                print("Difference:", difference.days," days")
            except ValueError:
                print("Error: Please enter valid dates in the format YYYY-MM-DD.")
        elif choice == '3':
            try:
                date_input = input("Enter the date (YYYY-MM-DD): ")
                date_value = datetime.datetime.strptime(date_input, "%Y-%m-%d")
                print("DD-MM-YYYY:", date_value.strftime("%d-%m-%Y"))
                print("MM/DD/YYYY:", date_value.strftime("%m/%d/%Y"))
                print("Long Format:", date_value.strftime("%A, %B %d, %Y"))
            except ValueError:
                print("Error: Please enter a valid date in the format YYYY-MM-DD.")
        elif choice == '4':
            print("\nStopwatch started.")
            input("Press Enter to start the stopwatch...")
            start_time = time.time()
            input("Press Enter again to finish...")
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Elapsed Time:",round(elapsed_time, 2), "seconds")
        elif choice == '5':
            try:
                seconds = int(input("Enter the countdown time in seconds: "))
                while seconds > 0:
                    print("Time left:", seconds, "seconds")
                    time.sleep(1)
                    seconds -= 1
                print("Countdown finished!")
            except ValueError:
                print("Error: Please enter a valid integer for seconds.")
        elif choice == '6':
            try:
                start_time = input("Enter the start time (HH:MM): ")
                end_time = input("Enter the end time (HH:MM): ")
                start = datetime.datetime.strptime(start_time, "%H:%M")
                end = datetime.datetime.strptime(end_time, "%H:%M")
                if end < start:
                    end += datetime.timedelta(days=1)
                working_hours = end - start
                hours = working_hours.total_seconds() / 3600
                minutes = (working_hours.total_seconds() % 3600) / 60
                print(f"Working Hours: {int(hours)} hours and {int(minutes)} minutes")
            except ValueError:
                print("Error: Please enter valid times in the format HH:MM.")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

def mathematical_menu():
    while True:
        print("\nMathematical Operations:")
        print("1. Factorial Calculation")
        print("2. Compound Interest Calculation")
        print("3. Trigonometric Calculation")
        print("4. Area of Shape Calculation")
        print("5. Logarithm Calculation")
        print("6. Back to Main Menu")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            number = int(input("Enter a number to calculate its factorial: "))
            factorial(number)
        elif choice == '2':
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the annual interest rate (in %): "))
            time = float(input("Enter the time period (in years): "))
            compound_interest(principal, rate, time)
        elif choice == '3':
            trigonometric_calation()
        elif choice == '4':
            area_of_shape()
        elif choice == '5':
            number = float(input("Enter a number to calculate its logarithm: "))
            if number > 0:
                print("Natural Logarithm (ln):", round(math.log(number), 4))
                print("Base 10 Logarithm (log10):", round(math.log10(number), 4))
            else:
                print("Error: Please enter a positive number.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


def random_menu():
    while True:
        print("\nRandom Operations:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Generate Random Password")
        print("4. Generate Random OTP")
        print("5. Random Sampling")
        print("6. Back to Main Menu")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            minimum = int(input("Enter the minimum value: "))
            maximum = int(input("Enter the maximum value: "))
            random_number = random.randint(minimum, maximum)
            print("Random Number:", random_number)
        elif choice == '2':
            size = int(input("Enter the size of the list: "))
            minimum = int(input("Enter the minimum value: "))
            maximum = int(input("Enter the maximum value: "))
            random_list = []
            for i in range(size):
                number = random.randint(minimum, maximum)
                random_list.append(number)
            print("Random List:", random_list)
        elif choice == '3':
            length = int(input("Enter the length of the password: "))
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
            password = ""
            for i in range(length):
                password += random.choice(characters)
            print("Random Password:", password)
        elif choice == '4':
            otp = ""
            for i in range(6):
                otp += str(random.randint(0, 9))
            print("Random OTP:", otp)
        elif choice == '5':
            data = ["Python", "Java", "C++", "JavaScript", "Ruby", "Go", "React", "Node.js", "Django", "Flask"]
            count = int(input("Enter the number of samples to select: "))
            samples = random.sample(data, count)
            print("Random Samples:", samples)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


def uuid_menu():
    while True:
        print("\nGenerate Unique Identifiers (UUID):")
        print("1. Generate UUID1")
        print("2. Generate UUID4")
        print("3. Generate multiple UUIDs")
        print("4. Back to Main Menu")
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            unique_id = uuid.uuid1()
            print("Generated UUID1:", unique_id)
        elif choice == '2':
            unique_id = uuid.uuid4()
            print("Generated UUID4:", unique_id)
        elif choice == '3':
            count = int(input("Enter the number of UUIDs to generate: "))
            for number in range(1, count + 1):
                unique_id = uuid.uuid4()
                print(f"UUID {number}: {unique_id}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a File")
        print("2. Write to a File")
        print("3. Read from a File")
        print("4. Append to a File")
        print("5. Back to Main Menu")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            file_name = input("Enter the name of the file to create: ")
            create_file(file_name)
        elif choice == '2':
            file_name = input("Enter the name of the file to write to: ")
            content = input("Enter the content to write: ")
            write_file(file_name, content)
        elif choice == '3':
            file_name = input("Enter the name of the file to read from: ")
            read_file(file_name)
        elif choice == '4':
            file_name = input("Enter the name of the file to append to: ")
            content = input("Enter the content to append: ")
            append_file(file_name, content)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def explore_menu():
    print("\nExplore Module Attributes(dir())")
    module_name = input("Enter the module name to explore: ")
    module = {
        "math": math,
        "random": random,
        "datetime": datetime,
        "string": string,
        "uuid": uuid,
        "time": time
    }
    if module_name in module:
        module = module[module_name]
        Attributes = dir(module)
        print(f"\nAvailable Attributes in {module_name} module:")
        print(Attributes)
    else:
        print("Module not available.")
        print("Try: math, random, datetime, time, uuid, string")
    dir(module) 

def main():
    while True:
        print("\n")
        print("Welcome to Multi-Utility Toolkit")
        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        choice = input("Enter your choice:")
        if choice == "1":
            datetime_menu()
        elif choice == "2":
            mathematical_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            uuid_menu()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explore_menu()
        elif choice == "7":
            print("\n Thank you for using The Multi-Utility Toolkit!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 7.")



if __name__ == "__main__":
    main()
        