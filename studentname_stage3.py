# studentname_stage3.py

# 1. Collect User Inputs
name = input("Enter student name: ")
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

# 2. Perform Calculations
total = mark1 + mark2 + mark3
percentage = (total / 300) * 100

# 3. Apply Grade Logic
if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

# 4. Final Output Display
print("\n--- Student Report ---")
print(name)
print(f"Total: {total}/300")
print(f"Percentage: {percentage:.1f}%")
print(f"Grade: {grade}")