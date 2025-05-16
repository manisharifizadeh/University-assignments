# Get input
a = input("First number: ")
b = input("Second number: ")
op = input("Operator (+ - * //): ")

# Convert to integers
a = int(a)
b = int(b)

# Perform operation
if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "//":
    if b == 0:
        print("Error! Cannot divide by zero.")
    else:
        print("Result:", a // b)
else:
    print("Invalid operator!")
