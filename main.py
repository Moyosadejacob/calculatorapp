# Build a Simple Calculator App for the following:
# Addition +
# Subtraction -
# Division /
# Multiplication *

""" 
Alternative 1
from addition import add_numbers
from subtraction import minus_number
from multiplication import multiply_number
from division import divide_number """


# Alternative 2
from addition.add_numbers import calculate_sum_of_numbers
from subtraction.minus_number import calculate_difference_of_numbers
from multiplication.multiply_number import multiplication_of_numbers
from division.divide_number import divides_of_numbers


def calculator(a, b, operation):

    if operation == "+":
        result = calculate_sum_of_numbers(a, b)
    elif operation == "-":
        result = calculate_difference_of_numbers(a, b)
    elif operation == "*":
        result = multiplication_of_numbers(a, b)
    elif operation == "/":
        result = divides_of_numbers(a, b)
    else:
        result = "No operation"
    return



print("Does calculation operations")
divide_result = calculator(a=7, b=-5, operation="/")
print(f"Division result: {divide_result}.")
mul_result = calculator(a=7, b=-5, operation="*")
print(f"Multiply result: {mul_result}.")
add_result = calculator(a=7, b=-5, operation="+")
print(f"Add result: {add_result}.")
subtract_result = calculator(a=7, b=-5, operation="-")
print(f"Subtract result: {subtract_result}.")