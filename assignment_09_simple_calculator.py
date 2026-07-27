# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


print("=" * 42)
print("Welcome to the Simple Calculator")
print("=" * 42)


def addition(number1, number2):
    result = number1 + number2
    return result


def subtraction(number1, number2):
    result = number1 - number2
    return result

def multiplication(number1, number2):
    result = number1 * number2
    return result


def division(number1, number2):

    if number2 == 0:
        return None

    else:
        result = number1 / number2
        return round(result, 2)

def modulus(number1, number2):
    result = number1 % number2
    return result


def exponentiation(number1, number2):
    result = number1 ** number2
    return result    

def display_menu():

    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")

while True:

    display_menu()

    choice = input("Select an operation (1-7): ")

    if choice == "7":
        print("Goodbye!")
        break


    elif choice in ["1", "2", "3", "4", "5", "6"]:
        number1 = float(input("Enter first number : "))
        number2 = float(input("Enter second number: "))

        if choice == "1":
            result = addition(number1, number2)
            print(f"Result: {number1} + {number2} = {result}")


        elif choice == "2":
            result = subtraction(number1, number2)
            print(f"Result: {number1} - {number2} = {result}")


        elif choice == "3":
            result = multiplication(number1, number2)
            print(f"Result: {number1} * {number2} = {result}")


        elif choice == "4":
            result = division(number1, number2)
            if result == None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {number1} / {number2} = {result}")
        elif choice == "5":
            result = modulus(number1, number2)
            print(f"Result: {number1} % {number2} = {result}")
        elif choice == "6":
            result = exponentiation(number1, number2)
            print(f"Result: {number1} ** {number2} = {result}")
    else:
        print("Error invalid choice")    