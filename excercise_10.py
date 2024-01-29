def fibonacci_sequence(max_value):
    if max_value < 0:
        return "Error"
    elif max_value == 0:
        return [0]
    fib_sequence = [0, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= max_value:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence
print(fibonacci_sequence(10))  # Expected output: [0, 1, 1, 2, 3, 5, 8]
print(fibonacci_sequence(1))  # Expected output: [0, 1, 1]
print(fibonacci_sequence(0))  # Expected output: [0]
print(fibonacci_sequence(-5))  # Expected: Error message or empty list