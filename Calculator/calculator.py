from calc_art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def modulo(n1, n2):
    return n1 % n2


def exponent(n1, n2):
    return n1 ** n2


print(logo)


def calculator():
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "%": modulo,
        "**": exponent
    }
    first_no = float(input("What is your first number? "))
    for key in operations:
        print(key)
    should_continue = True
    while should_continue:
        operation = input("Pick an operation: ")
        function = operations[operation]
        second_no = float(input("What is the next number? "))
        value = function(first_no, second_no)
        print(f"{first_no} {operation} {second_no} = {value}")
        if input(f"Type 'y' to continue calculating with {value}, or type 'n' to start a new calculation : ") == 'y':
            first_no = value
        else:
            should_continue = False
            calculator()


calculator()
