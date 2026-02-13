# CALCULATOR
# BASIC FUNCTIONS
def add(x: float, y: float) -> float:
    sum = x + y
    return sum


def subtract(x: float, y: float) -> float:
    subtraction = x - y
    return subtraction


def multiply(x: float, y: float) -> float:
    product = x * y
    return product


def divide(x: float, y: float) -> float:
    division = x / y
    return division


def calculate(x: float, y: float, operator: str) -> float:
    if operator == "+":
        sum = x + y
        return sum
    elif operator == "-":
        subtraction = x - y
        return subtraction
    elif operator == "*":
        product = x * y
        return product
    elif operator == "/":
        division = x / y
        return division
    else:
        return f"{operator} is an Invalid Operation, please input a valid one"


first_number = float(input("Enter your first number: "))
second_number = float(input("Enter your second number: "))
operation = input("Enter an operation('+', '-', '*', '/'): ")
calculation = float(calculate(x=first_number, y=second_number, operator=operation))
print(f"The result of your calculation is {calculation}")