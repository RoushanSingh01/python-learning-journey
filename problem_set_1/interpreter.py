# Prompt user for an arithmetic expression
expression = input("Expression: ")

# Split the input into x, y, and z based on single spaces
x, y, z = expression.split(" ")

# Convert x and z from strings to floating-point numbers for calculation
# (even though they are input as integers, converting to float allows for math)
num1 = float(x)
num2 = float(z)

# Perform the calculation based on the operator y
if y == "+":
    result = num1 + num2
elif y == "-":
    result = num1 - num2
elif y == "*":
    result = num1 * num2
elif y == "/":
    # The problem assumes z (num2) will not be 0
    result = num1 / num2

# Output the result formatted to one decimal place
print(f"{result:.1f}")
