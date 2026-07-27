# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

print("=" * 42)
print("Welcome to the Array Statistics Calculator")
print("=" * 42)

values = []
array_size = int(input("How many numbers? "))
if array_size <= 0:
    print("Error invalid input ")
for i in range(array_size):
    current_value = int(input(f"Enter number {i+1}: "))
    values.append(current_value)


def sum_of_array (values):
    total = 0
    for i in range(len(values)):
        total += values[i]
    return total    

def average_of_array (values):
    avg = sum_of_array(values) / len(values)
    return avg

def maximum_of_array(values):
    maximum = values[0]
    for i in range(len(values)):
        if values[i] > maximum:
            maximum = values[i]

    return maximum

def minimum_of_array(values):
    minimum = values[0]
    for i in range(len(values)):
        if values[i] < minimum:
            minimum = values[i]

    return minimum

print("Results:")
print(f"Sum:   {(sum_of_array(values))}")
print(f"Average: {(average_of_array(values))}")
print(f"Maximum: {(maximum_of_array(values))}")
print(f"Minimum: {(minimum_of_array(values))}")