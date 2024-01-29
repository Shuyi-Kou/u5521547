def calculate_factorial(number):
    # Handle edge cases
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0:
        return 1

    # Calculate factorial using a for loop
    factorial_result = 1
    for i in range(1, number + 1):
        factorial_result *= i

    return factorial_result

# Test cases
print(calculate_factorial(5))  # Expected output: 120
print(calculate_factorial(0))  # Expected output: 1
print(calculate_factorial(3))  # Expected output: 6
print(calculate_factorial(-1))  # Expected: Error message or specific value