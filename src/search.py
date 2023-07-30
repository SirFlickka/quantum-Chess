# search.py
import numpy as np
import sympy as sp

def quadrant_number(n):
    """
    Classify a number into one of four quadrants:
    - even0,2,4
    - even6,8
    - odd5
    - odd1,3,7,9
    """
    if n % 2 == 0:
        if n % 10 in [0, 2, 4]:
            return 'even0,2,4'
        else:
            return 'even6,8'
    else:
        if n % 10 == 5:
            return 'odd5'
        else:
            return 'odd1,3,7,9'

def search_quadrant(quadrant, numbers):
    """
    Find all numbers in the list that belong to the specified quadrant
    """
    return [n for n in numbers if quadrant_number(n) == quadrant]

def request_and_search_quadrant(numbers):
    """
    Prompt the user for a quadrant and search for numbers in that quadrant
    """
    valid_quadrants = ['even0,2,4', 'even6,8', 'odd5', 'odd1,3,7,9']

    while True:
        quadrant = input("Enter a quadrant ('even0,2,4', 'even6,8', 'odd5', 'odd1,3,7,9'): ")

        if quadrant in valid_quadrants:
            found_numbers = search_quadrant(quadrant, numbers)
            break
        else:
            print("Invalid quadrant. Please enter one of the following: 'even0,2,4', 'even6,8', 'odd5', 'odd1,3,7,9'")

    return found_numbers

def transform_numbers(numbers):
    """
    Apply transformations (logarithm, exponential) to a list of numbers using sympy for more precision
    """
    # Use sympy to apply the natural logarithm and get symbolic results
    log_numbers = [sp.log(n) for n in numbers]

    # Convert the symbolic results to decimals with a precision of 50 digits
    log_numbers_decimal = [float(n.evalf(50)) for n in log_numbers]

    # Apply the exponential function as before
    exp_numbers = np.exp(numbers)

    # Combine the original numbers, more precise log numbers, and exp numbers into a single list
    combined_numbers = np.concatenate((numbers, log_numbers_decimal, exp_numbers))
    return combined_numbers

# Example usage:
numbers = np.array(range(1, 20))
transformed_numbers = transform_numbers(numbers)
found_numbers = request_and_search_quadrant(transformed_numbers)
print(f"Numbers in the requested quadrant: {found_numbers}")
