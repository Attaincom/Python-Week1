# Basic Calculator Program

# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user for a mathematical operation
operation = input("Enter the operation (+, -, *, /): ")

# Perform the calculation and display the result
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    # Handle division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")
