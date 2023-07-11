# This is a simple program to calculate the factorial of a number

def factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# Prompt the user for input
number = int(input("Enter a non-negative integer: "))

# Calculate and display the factorial
result = factorial(number)
print(f"The factorial of {number} is: {result}")

