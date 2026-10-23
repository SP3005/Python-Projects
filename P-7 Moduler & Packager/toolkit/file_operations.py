# Custom file operations module

def create_file(filename):
    try:
        with open(filename, 'x') as file:
            file.write("")
        print("File created successfull.")
    except FileExistsError:
        print("Error: File already exists.")
    except Exception as error:
        print(f"Error: {error}")

def write_file(filename, data):
    try:
        with open(filename, "w") as file:
            file.write(data)
        print("Data written to file successfully.")
    except Exception as error:
        print(f"Error: {error}")

def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
        print("\nFile content:")
        print(content)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as error:
        print(f"Error: {error}")

def append_file(filename, data):
    try:
        with open(filename, "a") as file:
            file.write(data)
        print("Data appended to file successfully.")
    except Exception as error:
        print(f"Error: {error}")