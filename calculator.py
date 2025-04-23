def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
    return x / y

def calculator():
    print("Simple Python Calculator")
    print("Operations: +, -, *, /")

    while True:
        operation = input("Enter operation (+, -, *, /) or 'q' to quit: ")
        if operation == 'q':
            print("Goodbye!")
            break

        if operation in ('+', '-', '*', '/'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Please enter valid numbers.")
                continue

            if operation == '+':
                print("Result:", add(num1, num2))
            elif operation == '-':
                print("Result:", subtract(num1, num2))
            elif operation == '*':
                print("Result:", multiply(num1, num2))
            elif operation == '/':
                print("Result:", divide(num1, num2))
        else:
            print("Invalid operation. Try again.")

calculator()
