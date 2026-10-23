import math


def factorial(number):
    try:
        number = int(number)

        if number < 0:
            print("Factorial is not defined for negative numbers.")
            return
        result = math.factorial(number)
        print("Factorial:", result)
    except ValueError:
        print("Error: Please enter a valid integer.")

def compound_interest(principal, rate, time):
    try:
        principal = float(principal)
        rate = float(rate)
        time = float(time)
        amount = principal * ((1+rate/100)**time)
        print("Compound Interest: ", round(amount, 2))
    except ValueError:
        print("Error: Please enter valid numbers.")

def trigonometric_calation():
    try:
        angle = float(input("Enter the angle in degrees: "))
        radians = math.radians(angle)
        print("Sine:", round(math.sin(radians), 4))
        print("Cosine:", round(math.cos(radians), 4))
        print("Tangent:", round(math.tan(radians), 4))
    except ValueError:
        print("Error: Please enter a valid number.")

def area_of_shape():
    print("Choose a shape:")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Triangle")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        radius = float(input("Enter the radius of the circle: "))
        area = math.pi * (radius ** 2)
        print("Area of Circle:", round(area, 2))
    elif choice == '2':
        side = float(input("Enter the side length of the square: "))
        area = side ** 2
        print("Area of Square:", round(area, 2))
    elif choice == '3':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print("Area of Rectangle:", round(area, 2))
    elif choice == '4':
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print("Area of Triangle:", round(area, 2))
    else:
        print("Invalid choice. Please select a valid option.")