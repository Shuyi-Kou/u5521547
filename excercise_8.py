def compound_interest_calculator(P, r, n, t):
    # Check for invalid inputs
    if P <= 0 or r < 0 or n <= 0 or t < 0:
        return "Invalid input. Please provide valid values for Principal amount, Annual interest rate, Number of times interest is compounded per year, and Number of years for investment."

    # Calculate compound interest
    A = P * (1 + r/n)**(n*t)
    return f"Amount after {t} years: {A:.2f}"

# Test cases
print(compound_interest_calculator(1000, 0.05, 12, 5))  # Expected: Amount after 5 years
print(compound_interest_calculator(500, 0.07, 4, 10))  # Expected: Amount after 10 years