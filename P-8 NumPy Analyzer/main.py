import numpy as np
class DataAnalytics:
    def __init__(self, array=None):
        self.__array = np.array([]) if array is None else np.array(array)
    def __read_number(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a valid number.")
    def __read_positive_integer(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                print("Enter a number greater than zero.")
            except ValueError:
                print("Please enter a valid integer.")
    def __read_array_values(self, shape, prefix="a"):
        if len(shape) == 1:
            return [self.__read_number(f"Enter {prefix}[{i}]: ") for i in range(shape[0])]
        if len(shape) == 2:
            return [[self.__read_number(f"Enter {prefix}[{i}][{j}]: ")
                     for j in range(shape[1])] for i in range(shape[0])]
        if len(shape) == 3:
            return [[[self.__read_number(f"Enter {prefix}[{i}][{j}][{k}]: ")
                      for k in range(shape[2])] for j in range(shape[1])]
                    for i in range(shape[0])]
    @classmethod
    def from_values(cls, values):
        return cls(values)

    @staticmethod
    def is_valid_number(value):
        try:
            float(value)
            return True
        except (TypeError, ValueError):
            return False

    def __calculate_sum(self):
        return np.sum(self.__array)

    def create_array(self):
        print("\nArray Creation:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                size = self.__read_positive_integer("Enter the number of elements: ")
                self.__array = np.array(self.__read_array_values((size,)))
            elif choice == "2":
                rows = self.__read_positive_integer("Enter the number of rows: ")
                columns = self.__read_positive_integer("Enter the number of columns: ")
                self.__array = np.array(self.__read_array_values((rows, columns)))
            elif choice == "3":
                layers = self.__read_positive_integer("Enter the number of layers: ")
                rows = self.__read_positive_integer("Enter the number of rows: ")
                columns = self.__read_positive_integer("Enter the number of columns: ")
                self.__array = np.array(self.__read_array_values((layers, rows, columns)))
            else:
                print("Invalid choice.")
                return
            print("\nArray created successfully:")
            print(self.__array)
            print("Shape:", self.__array.shape)
            print("Dimensions:", self.__array.ndim)
        except (ValueError, IndexError) as error:
            print("Could not create array:", error)

    def indexing(self):
        if self.__array.size == 0:
            print("Please create an array first.")
            return
        print("\nIndexing:")
        print(self.__array)
        try:
            if self.__array.ndim == 1:
                index = int(input("Enter index: "))
                print("Element:", self.__array[index])
            elif self.__array.ndim == 2:
                row = int(input("Enter row index: "))
                column = int(input("Enter column index: "))
                print("Element:", self.__array[row, column])
            else:
                layer = int(input("Enter layer index: "))
                row = int(input("Enter row index: "))
                column = int(input("Enter column index: "))
                print("Element:", self.__array[layer, row, column])
        except (ValueError, IndexError):
            print("Invalid index.")

    def slicing(self):
        if self.__array.size == 0:
            print("Please create an array first.")
            return
        print("\nSlicing:")
        print(self.__array)
        try:
            if self.__array.ndim == 1:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                print(self.__array[start:end])
            elif self.__array.ndim == 2:
                rs = int(input("Enter row start index: "))
                re = int(input("Enter row end index: "))
                cs = int(input("Enter column start index: "))
                ce = int(input("Enter column end index: "))
                print(self.__array[rs:re, cs:ce])
            else:
                ls = int(input("Enter layer start index: "))
                le = int(input("Enter layer end index: "))
                rs = int(input("Enter row start index: "))
                re = int(input("Enter row end index: "))
                cs = int(input("Enter column start index: "))
                ce = int(input("Enter column end index: "))
                print(self.__array[ls:le, rs:re, cs:ce])
        except ValueError:
            print("Please enter valid indexes.")

    def combining_splitting(self):
        if self.__array.size == 0:
            print("Please create an array first.")
            return
        print("\nCombining and Splitting:")
        print("1. Combine Arrays")
        print("2. Split Array")
        choice = input("Enter your choice: ").strip()
        try:
            if choice == "1":
                axis = int(input(f"Enter axis (0 to {self.__array.ndim - 1}): "))
                if axis < 0 or axis >= self.__array.ndim:
                    print("Invalid axis.")
                    return
                second = np.array(self.__read_array_values(self.__array.shape, "b"))
                print("Combined Array:")
                print(np.concatenate((self.__array, second), axis=axis))
            elif choice == "2":
                axis = int(input(f"Enter axis (0 to {self.__array.ndim - 1}): "))
                if axis < 0 or axis >= self.__array.ndim:
                    print("Invalid axis.")
                    return
                parts = self.__read_positive_integer("Enter number of parts: ")
                if self.__array.shape[axis] % parts != 0:
                    print("Array cannot be split into equal parts.")
                    return
                for part in np.split(self.__array, parts, axis=axis):
                    print(part)
            else:
                print("Invalid choice.")
        except (ValueError, IndexError) as error:
            print("Operation could not be completed:", error)

    def mathematical_operations(self):
        if self.__array.size == 0:
            print("Please create an array first.")
            return
        print("\nMathematical Operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product (2D arrays)")
        print("6. Matrix Multiplication (2D arrays)")
        choice = input("Enter your choice: ").strip()
        try:
            if choice in ("1", "2", "3", "4"):
                second = np.array(self.__read_array_values(self.__array.shape, "b"))
                if choice == "1":
                    result = np.add(self.__array, second)
                    label = "Addition"
                elif choice == "2":
                    result = np.subtract(self.__array, second)
                    label = "Subtraction"
                elif choice == "3":
                    result = np.multiply(self.__array, second)
                    label = "Multiplication"
                else:
                    if np.any(second == 0):
                        print("Division by zero is not allowed.")
                        return
                    result = np.divide(self.__array, second)
                    label = "Division"
                print(f"{label} Result:")
                print(result)
            elif choice in ("5", "6"):
                if self.__array.ndim != 2:
                    print("Dot product and matrix multiplication require a 2D array.")
                    return
                rows = self.__read_positive_integer("Enter rows for second matrix: ")
                columns = self.__read_positive_integer("Enter columns for second matrix: ")
                if rows != self.__array.shape[1]:
                    print("Columns of first matrix must equal rows of second matrix.")
                    return
                second = np.array(self.__read_array_values((rows, columns), "b"))
                if choice == "5":
                    if self.__array.shape != second.shape:
                        print("For dot product, both 2D arrays must have the same shape.")
                        return
                    print("Dot Product Result:")
                    print(np.sum(self.__array * second))
                else:
                    print("Matrix Multiplication Result:")
                    print(np.matmul(self.__array, second))
            else:
                print("Invalid choice.")
        except (ValueError, IndexError) as error:
            print("Operation could not be completed:", error)

    def search_sort_filter(self):
        if self.__array.size == 0:
            print("Please create an array first.")
            return
        print("\nSearch, Sort, and Filter:")
        print("1. Search a Value")
        print("2. Sort Array")
        print("3. Filter Array")
        choice = input("Enter your choice: ").strip()
        try:
            if choice == "1":
                value = float(input("Enter value to search: "))
                positions = np.argwhere(self.__array == value)
                if positions.size:
                    print("Value found at index/indices:")
                    print(positions.flatten() if self.__array.ndim == 1 else positions)
                else:
                    print("Value not found.")
            elif choice == "2":
                print("1. Ascending Order")
                print("2. Descending Order")
                order = input("Enter your choice: ").strip()
                result = np.sort(self.__array, axis=None)
                if order == "2":
                    result = result[::-1]
                elif order != "1":
                    print("Invalid choice.")
                    return
                print("Sorted Array:")
                print(result)
            elif choice == "3":
                print("1. Greater Than")
                print("2. Less Than")
                print("3. Equal To")
                print("4. Greater Than or Equal To")
                print("5. Less Than or Equal To")
                condition = input("Enter your choice: ").strip()
                value = float(input("Enter comparison value: "))
                if condition == "1":
                    result = self.__array[self.__array > value]
                elif condition == "2":
                    result = self.__array[self.__array < value]
                elif condition == "3":
                    result = self.__array[self.__array == value]
                elif condition == "4":
                    result = self.__array[self.__array >= value]
                elif condition == "5":
                    result = self.__array[self.__array <= value]
                else:
                    print("Invalid choice.")
                    return
                print("Filtered Values:")
                print(result)
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter valid numeric input.")

    def aggregating_functions(self):
        if self.__array.size == 0:
            print("Please create an array first.")
            return
        print("\nAggregating and Statistical Functions:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum")
        print("7. Maximum")
        print("8. Percentile")
        print("9. Correlation")
        print("10. Calculate All Functions")
        choice = input("Enter your choice: ").strip()
        print("Original Array:")
        print(self.__array)
        if choice == "1":
            print("Sum:", self.__calculate_sum())
        elif choice == "2":
            print("Mean:", np.mean(self.__array))
        elif choice == "3":
            print("Median:", np.median(self.__array))
        elif choice == "4":
            print("Standard Deviation:", np.std(self.__array))
        elif choice == "5":
            print("Variance:", np.var(self.__array))
        elif choice == "6":
            print("Minimum:", np.min(self.__array))
        elif choice == "7":
            print("Maximum:", np.max(self.__array))
        elif choice == "8":
            try:
                p = float(input("Enter percentile (0-100): "))
                if not 0 <= p <= 100:
                    print("Percentile must be between 0 and 100.")
                    return
                print(f"{p}th Percentile:", np.percentile(self.__array, p))
            except ValueError:
                print("Please enter a valid percentile.")
        elif choice == "9":
            second = np.array([self.__read_number(f"Enter b[{i}]: ")
                               for i in range(self.__array.size)])
            first = self.__array.flatten()
            if np.std(first) == 0 or np.std(second) == 0:
                print("Correlation is undefined for a constant array.")
                return
            print("Correlation:", np.corrcoef(first, second)[0, 1])
        elif choice == "10":
            print("Sum:", np.sum(self.__array))
            print("Mean:", np.mean(self.__array))
            print("Median:", np.median(self.__array))
            print("Standard Deviation:", np.std(self.__array))
            print("Variance:", np.var(self.__array))
            print("Minimum:", np.min(self.__array))
            print("Maximum:", np.max(self.__array))
            print("25th Percentile:", np.percentile(self.__array, 25))
            print("50th Percentile:", np.percentile(self.__array, 50))
            print("75th Percentile:", np.percentile(self.__array, 75))
        else:
            print("Invalid choice.")

    def statistical_functions(self):
        if self.__array.size == 0:
            print("Please create an array first.")
            return
        print("\nStatistical Functions:")
        print("1. Minimum Value")
        print("2. Maximum Value")
        print("3. Percentile")
        print("4. Correlation Coefficient")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            print("Minimum Value:", np.min(self.__array))
        elif choice == "2":
            print("Maximum Value:", np.max(self.__array))
        elif choice == "3":
            try:
                p = float(input("Enter percentile (0-100): "))
                if not 0 <= p <= 100:
                    print("Percentile must be between 0 and 100.")
                    return
                print("Percentile:", np.percentile(self.__array, p))
            except ValueError:
                print("Please enter a valid percentile.")
        elif choice == "4":
            second = np.array([self.__read_number(f"Enter b[{i}]: ")
                               for i in range(self.__array.size)])
            first = self.__array.flatten()
            if np.std(first) == 0 or np.std(second) == 0:
                print("Correlation is undefined for a constant array.")
                return
            print("Correlation Coefficient:", np.corrcoef(first, second)[0, 1])
        else:
            print("Invalid choice.")

    def run(self):
        print("Welcome to the NumPy Analyzer!")
        while True:
            print("\nChoose an option:")
            print("1. Create a NumPy Array")
            print("2. Indexing")
            print("3. Slicing")
            print("4. Combining and Splitting")
            print("5. Mathematical Operations")
            print("6. Search, Sort, and Filter")
            print("7. Aggregating Functions")
            print("8. Statistical Functions")
            print("9. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.create_array()
            elif choice == "2":
                self.indexing()
            elif choice == "3":
                self.slicing()
            elif choice == "4":
                self.combining_splitting()
            elif choice == "5":
                self.mathematical_operations()
            elif choice == "6":
                self.search_sort_filter()
            elif choice == "7":
                self.aggregating_functions()
            elif choice == "8":
                self.statistical_functions()
            elif choice == "9":
                print("Thank you for using the NumPy Analyzer! Goodbye!")
                break
            else:
                print("Invalid choice. Please choose from 1 to 9.")


if __name__ == "__main__":
    analyzer = DataAnalytics()
    analyzer.run()