print("\nWelcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    option = int(input("Enter your choice: "))
    if option == 1:
        while True:
            print("\n------ PATTERN MENU ------")
            print("1. Right Triangle")
            print("2. Inverted Right Triangle")
            print("3. Pyramid")
            print("4. Inverted Pyramid")
            print("5. Diamond Pattern")
            print("6. Hollow Square")
            print("7. Butterfly Pattern")
            print("0. Back to Main Menu")
            choice = input("\nEnter your choice: ")
            match choice:
                case "1":
                    rows = int(input("Enter number of rows: "))
                    for i in range(1, rows + 1):
                        for j in range(i):
                            print("*", end=" ")
                        print()
                case "2":
                    rows = int(input("Enter number of rows: "))
                    for i in range(rows, 0, -1):
                        for j in range(i):
                            print("*", end=" ")
                        print()
                case "3":
                    rows = int(input("Enter number of rows: "))
                    for i in range(1, rows + 1):
                        spaces = rows - i
                        stars = 2 * i - 1
                        print(" " * spaces + "*" * stars)
                case "4":
                    rows = int(input("Enter number of rows: "))
                    for i in range(rows, 0, -1):
                        spaces = rows - i
                        stars = 2 * i - 1
                        print(" " * spaces + "*" * stars)
                case "5":
                    rows = int(input("Enter number of rows: "))
                    for i in range(1, rows + 1):
                        spaces = rows - i
                        stars = 2 * i - 1
                        print(" " * spaces + "*" * stars)
                    for i in range(rows - 1, 0, -1):
                        spaces = rows - i
                        stars = 2 * i - 1
                        print(" " * spaces + "*" * stars)
                case "6":
                    rows = int(input("Enter size of square: "))
                    for i in range(rows):
                        for j in range(rows):
                            if (i == 0 or i == rows - 1 or j == 0 or j == rows - 1):
                                print("*", end=" ")
                            else:
                                print(" ", end=" ")
                        print()
                case "7":
                    rows = int(input("Enter number of rows: "))
                    for i in range(1, rows + 1):
                        print("*" * i, end="")
                        print(" " * (2 * (rows - i)), end="")
                        print("*" * i)
                    for i in range(rows - 1, 0, -1):
                        print("*" * i, end="")
                        print(" " * (2 * (rows - i)), end="")
                        print("*" * i)
                case "0":
                    print("\nReturning to Main Menu...")
                    break
                case _:
                    print("\nInvalid choice! Please try again.")
    elif option == 2:
        start = int(input("\nEnter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        if start > end:
            print("\nInvalid range! Start number should be smaller than end number.")
        else:
            total = 0
            print("\n------ NUMBER ANALYSIS ------")
            for number in range(start, end + 1):
                total = total + number
                if number % 2 == 0:
                    print(number, "is Even")
                else:
                    print(number, "is Odd")
            print("\nSum of numbers from",start,"to",end,"=",total)
    elif option == 3:
        print("\nThank you for using the program!")
        break
    else:
        print("\nInvalid choice! Please select between 1 and 3.")
