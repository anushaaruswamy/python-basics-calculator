# studentname_stage1.py

# Taking user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# Logic to handle arithmetic operations
if operator == '+':
    result = num1 + num2
    print(f"Result = {result}")
elif operator == '-':
    result = num1 - num2
    print(f"Result = {result}")
elif operator == '*':
    result = num1 * num2
    print(f"Result = {result}")
elif operator == '/':
    # Handling division by zero
    if num2 != 0:
        result = num1 / num2
        print(f"Result = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator.")