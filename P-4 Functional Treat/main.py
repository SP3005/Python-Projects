def input_data():
    """Take input for both 1D and 2D array."""
    print("\n+-------------------------------+")
    print("|          Input Data           |")
    print("+-------------------------------+")
    
    print("\n~~~~~~~~~~ 1D ARRAY ~~~~~~~~~~")
    size = int(input("Enter number of 1D elements: "))
    array_1d = []
    for i in range(size):
        value = int(input(f"Enter element {i + 1}: "))
        array_1d.append(value)
    print("\n1D Array:",array_1d)
    
    print("\n~~~~~~~~~~ 2D ARRAY ~~~~~~~~~~")
    rows = int(input("Enter number of row: "))
    columns = int(input("Enter number of columns: "))
    array_2d = []
    for i in range(rows):
        row = []
        for j in range(columns):
            value = int(input(f"Enter value[{i + 1}][{j + 1}]: "))
            row.append(value)
        array_2d.append(row)
    print("\n2D Array:")
    for row in array_2d:
        print(row)

    print("\nBoth arrays created successfully!")
    return array_1d, array_2d

def display_data(array_1d, array_2d):
    print("\n+-------------------------------+")
    print("|         Display Data          |")
    print("+-------------------------------+")
    print("\n1D Array:")
    print(array_1d)
    print("\n2D Array:")
    for row in array_2d:
        print(row)


def display_data_summary(array_1d, array_2d):
        """Display summary of both 1D and 2D arrays."""
        total_1d = sum(array_1d)
        count_1d = len(array_1d)
        minimum_1d = min(array_1d)
        maximum_1d = max(array_1d)
        average_1d = total_1d / count_1d
        print("\n+-------------------------------+")
        print("|     1D Array data summary     |")
        print("|      (Build-in Function)      |")
        print("+-------------------------------+")
        print("Array Type     :","1D Array")
        print("Total Elements :", count_1d)
        print("Minimum Value  :", minimum_1d)
        print("Maximum Value  :", maximum_1d)
        print("Total Sum      :", total_1d)
        print("Average        :", average_1d)
        total_2d = 0
        count_2d = 0
        for row in array_2d:
            total_2d += sum(row)
            count_2d += len(row)
        minimum_2d = min(min(row) for row in array_2d)
        maximum_2d = max(max(row) for row in array_2d)
        average_2d = total_2d / count_2d
        print("\n+-------------------------------+")
        print("|     2D Array data summary     |")
        print("|      (Build-in Function)      |")
        print("+-------------------------------+")
        print("Array Type     :","2D Array")
        print("Total Elements :", count_2d)
        print("Minimum Value  :", minimum_2d)
        print("Maximum Value  :", maximum_2d)
        print("Total Sum      :", total_2d)
        print("Average        :", average_2d)

def factorial(n):
    """ Calculate factorial using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def factorial_menu():
    """Take number from user and calculate factorial"""
    print("\n+-------------------------------+")
    print("|      Calculate Factorial      |")
    print("|          (Recursion)          |")
    print("+-------------------------------+")
    num = int(input("\nEnter a Number : "))
    if num <= 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = factorial(num)
        print("Factorial of", num, "is:", result)

def filter_data(array_1d, array_2d):
    """Filter both arrays using lambda function."""
    print("\n+-------------------------------+")
    print("|    Filter data by threshold   |")
    print("|       (Lambda Function)       |")
    print("+-------------------------------+")
    threshold = int(input("Enter threshold: "))
    result_1d = list(filter(lambda x: x > threshold, array_1d))
    result_2d = []
    for row in array_2d:
        filtered_row = list(filter(lambda x: x > threshold, row))
        result_2d.append(filtered_row)
    print("\nOriginal 1D Array: ",array_1d)
    print("Threshold: ",threshold)
    print("Filtered 1D Array: ", result_1d)
    print("\nOriginal 2D Array: ")
    for row in array_2d:
        print(row)
    print("Threshold: ",threshold)
    print("Filtered 2D Array: ")
    for row in result_2d:
        print(row)
def sort_data(array_1d, array_2d):
    """Sort both 1D and 2D arrays in increasing and decreasing order."""
    while True:
        print("\n+-------------------------------+")
        print("|           Sort Data           |")
        print("|   (Increasing / Decreasing)   |")
        print("+-------------------------------+")
        print("1. Ascending")
        print("2. Descending")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("\n~~~~~~~~~~ 1D ARRAY ~~~~~~~~~~")
            increasing_1d = sorted(array_1d)
            print("Original   : ",array_1d)
            print("Asscending : ", increasing_1d)
            numbers = []
            for row in array_2d:
                for value in row:
                    numbers.append(value)
            increasing_2d = sorted(numbers)
            increasing_array_2d = []
            index = 0
            for i in range(len(array_2d)):
                row = []
                for j in range(len(array_2d[i])):
                    row.append(increasing_2d[index])
                    index +=1
                increasing_array_2d.append(row)
            print("\n~~~~~~~~~~ 2D ARRAY ~~~~~~~~~~")
            print("Original :")
            for row in array_2d:
                print(row)
            print("Asscending :")
            for row in increasing_array_2d:
                    print(row)
        elif choice == 2:
            print("\n~~~~~~~~~~ 1D ARRAY ~~~~~~~~~~")
            decreasing_1d = sorted(array_1d)
            print("Original   : ",array_1d)
            print("Descending : ", decreasing_1d)
            numbers = []
            for row in array_2d:
                for value in row:
                    numbers.append(value)
            decreasing_2d = sorted(numbers)
            decreasing_array_2d = []
            index = 0
            for i in range(len(array_2d)):
                row = []
                for j in range(len(array_2d[i])):
                    row.append(decreasing_2d[index])
                    index +=1
                decreasing_array_2d.append(row)
            print("\n~~~~~~~~~~ 2D ARRAY ~~~~~~~~~~")
            print("Original :")
            for row in array_2d:
                print(row)
            print("Asscending :")
            for row in decreasing_array_2d:
                    print(row)
        elif choice == 3:
            print("\nExiting Sort Data...")
            break
        else:
            print("\nInvalid choice!")
            print("Please select 1, 2, 3.")

def dataset_statistics(array_1d,array_2d):
    """Calculate and return dataset statistics."""

    total_1d = sum(array_1d)
    count_1d = len(array_1d)
    minimum_1d = min(array_1d)
    maximum_1d = max(array_1d)
    average_1d = total_1d / count_1d
    even_1d = 0
    odd_1d = 0
    positive_1d = 0
    negative_1d = 0
    zero_1d = 0
    for value in array_1d:
        if value %2==0:
            even_1d += 1
        else:
            odd_1d += 1
        if value > 0:
            positive_1d += 1
        elif value < 0:
            negative_1d += 1
        else:
            zero_1d += 1
    total_2d = 0
    count_2d = 0
    even_2d = 0
    odd_2d = 0
    positive_2d = 0
    negative_2d = 0
    zero_2d = 0
    for row in array_2d:
        total_2d += sum(row)
        count_2d += len(row)
        for value in row:
            if value %2==0:
                even_2d += 1
            else:
                odd_2d += 1
            if value > 0:
                positive_2d += 1
            elif value < 0:
                negative_2d += 1
            else:
                zero_2d += 1
    minimum_2d = min(min(row) for row in array_2d)
    maximum_2d = max(max(row) for row in array_2d)
    average_2d = total_2d / count_2d
    statistics_1d = (count_1d, minimum_1d, maximum_1d, total_1d, average_1d, even_1d, odd_1d, positive_1d, negative_1d, zero_1d)
    statistics_2d = (count_2d, minimum_2d, maximum_2d, total_2d, average_2d, even_2d, odd_2d, positive_2d, negative_2d, zero_2d)
    return statistics_1d, statistics_2d

def display_statistics(array_1d, array_2d):
    statistics_1d,statistics_2d = dataset_statistics(array_1d, array_2d)
    print("\n+-------------------------------+")
    print("|   Display Dataset Statistics  |")
    print("|    (Return Multiple Values)   |")
    print("+-------------------------------+")
    print("\n~~~~~~~~~~ 1D ARRAY ~~~~~~~~~~")
    print("Array Type      :","1D Array")
    print("Total Elements  :", statistics_1d[0])
    print("Minimum Value   :", statistics_1d[1])
    print("Maximum Value   :", statistics_1d[2])
    print("Total Sum       :", statistics_1d[3])
    print("Average         :", statistics_1d[4])
    print("Even Values     :", statistics_1d[5])
    print("Odd Values      :", statistics_1d[6])
    print("Positive Values :", statistics_1d[7])
    print("Negative Values :", statistics_1d[8])
    print("Zero Values     :", statistics_1d[9])
    print("\n~~~~~~~~~~ 2D ARRAY ~~~~~~~~~~")
    print("Array Type      :","2D Array")
    print("Total Elements  :", statistics_2d[0])
    print("Minimum Value   :", statistics_2d[1])
    print("Maximum Value   :", statistics_2d[2])
    print("Total Sum       :", statistics_2d[3])
    print("Average         :", statistics_2d[4])
    print("Even Values     :", statistics_2d[5])
    print("Odd Values      :", statistics_2d[6])
    print("Positive Values :", statistics_2d[7])
    print("Negative Values :", statistics_2d[8])
    print("Zero Values     :", statistics_2d[9])


def show_doc():
    """Display documentation of all functions."""
    print("\n+-------------------------------+")
    print("|     FUNCTION DOCUMENTATION    |")
    print("+-------------------------------+")
    print("\n1. input_data.__doc__")
    print(input_data.__doc__)
    print("\n2. display_data.__doc__")
    print(display_data.__doc__)
    print("\n3. display_data_summary.__doc__")
    print(display_data_summary.__doc__)
    print("\n4. factorial.__doc__")
    print(factorial.__doc__)
    print("\n5. factorial_menu.__doc__")
    print(factorial_menu.__doc__)
    print("\n6. filter_data.__doc__")
    print(filter_data.__doc__)
    print("\n7. sort_data.__doc__")
    print(sort_data.__doc__)
    print("\n8. dataset_statistics.__doc__")
    print(dataset_statistics.__doc__)
    print("\n9. show_doc.__doc__")
    print(show_doc.__doc__)

array_1d = None
array_2d = None

while True:
    print("\n")
    print("\n+-----------------------------------------+")
    print("|   DATA ANALYZER & TRANSFORMER PROGRAM   |")
    print("+-----------------------------------------+")
    print("| 1. Input Data                           |")
    print("| 2. Display Both Arrays                  |")
    print("| 3. Data Summary                         |")
    print("| 4. Factorial                            |")
    print("| 5. Filter Data                          |")
    print("| 6. Sort Data                            |")
    print("| 7. Dataset Statistics                   |")
    print("| 8. Show __doc__                         |")
    print("| 9. Exit                                 |")
    print("+-----------------------------------------+")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        array_1d, array_2d = input_data()
        
    elif choice == 2:
        if array_1d is None or array_2d is None:
            print("\nPlease enter both arrays first.")
        else:
            display_data(array_1d, array_2d)

    elif choice == 3:
        if array_1d is None or array_2d is None:
            print("\nPlease enter both arrays first.")
        else:
            display_data_summary(array_1d, array_2d)
            
    elif choice == 4:
        factorial_menu()
        
    elif choice == 5:
        if array_1d is None or array_2d is None:
            print("\nPlease enter both arrays first.")
        else:
            filter_data(array_1d, array_2d)

    elif choice == 6:
        if array_1d is None or array_2d is None:
            print("\nPlease enter both arrays first.")
        else:
            sort_data(array_1d, array_2d)

    elif choice == 7:
        if array_1d is None or array_2d is None:
            print("\nPlease enter both arrays first.")
        else:
            display_statistics(array_1d, array_2d)

    elif choice == 8:
        show_doc()

    elif choice == 9:
        print("\n+-----------------------------------------+")
        print("|    Thank You For Using Data Analyzer    |")
        print("+-----------------------------------------+")
        print("Program Exit Successfully.")
        break

    else:
        print("\nInvalid Choice!")
        print("Please select a choice from 1 to 9.")
