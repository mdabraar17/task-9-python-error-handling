# error_handling.py
# Demonstrates exception handling and logging in Python

import logging

# -------- Logging Configuration --------
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide_numbers(a, b):
    """Divides two numbers and handles errors"""
    try:
        result = a / b
        return result

    except ZeroDivisionError:
        logging.error("Division by zero attempted")
        return "Error: Cannot divide by zero"

    except TypeError:
        logging.error("Invalid data type used for division")
        return "Error: Invalid input type"

    else:
        print("Division successful")

    finally:
        print("Execution completed")


# -------- Simulating runtime errors --------
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    output = divide_numbers(num1, num2)
    print("Result:", output)

except ValueError:
    logging.error("User entered non-numeric value")
    print("Error: Please enter only numbers")

finally:
    print("Program ended safely")
