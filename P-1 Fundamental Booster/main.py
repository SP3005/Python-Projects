print("Welcome to the Innteractive Personal Data Collector!")

name = input("Please enter your name = ")
age = int(input("Please enter your age = "))
height = float(input("Please enter your height in meters = "))
favorite_namber = int(input("Please enter your favorite number = "))

print()
print("Thank you! Here is the information we collected:")
print()

print(f"Name: {name}(Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age}(Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height}(Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favorite Number: {favorite_namber}(Type: {type(favorite_namber)}, Memory Address: {id(favorite_namber)})\n")

current_year = 2026
birth_year = current_year - age

print(f"Your birth year is approximately = {birth_year}"
      f"(based on your age of {age})")

print()
print("Thank you for using the Personal Data Collector. Goodbye!")
