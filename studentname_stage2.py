# studentname_stage2.py

# Step 1: Get user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# Initialize result as None to track if a calculation actually happened
result = None

# Step 2: Calculator Logic (from Stage 1)
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero.")
else:
    print("Invalid operator.")

# Step 3: Result Check logic
# We only run this if 'result' was successfully assigned a number
if result is not None:
    print(f"Result = {result}")
    
    if result > 0:
        print("Positive")
    elif result < 0:
        print("Negative")
    else:
        print("Zero")