def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_operation():
    operations = ['+', '-', '*', '/']
    while True:
        operation = input("Enter operation (+, -, *, /): ")
        if operation in operations:
            return operation
        else:
            print("Invalid operation! Please enter one of +, -, *, /.")

def calculator():
    print("Welcome to the Simple Calculator!")
    
    while True:
        num1 = get_number("Enter the first number: ")
        operation = get_operation()
        num2 = get_number("Enter the second number: ")
        
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        
        print(f"The result of {num1} {operation} {num2} = {result}")
        
        continue_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if continue_calculation.lower() != 'yes':
            break
    
    print("Thank you for using the calculator!")

if __name__ == "__main__":
    calculator()
