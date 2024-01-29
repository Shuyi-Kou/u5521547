def is_prime(number):
    if number < 2:
        return False
    elif (number%2 != 0 and number%3 != 0 and number%5 != 0 and number%7 !=0) or (number == 2 or number == 3 or number == 5 or number == 7):
        return True
    else:
        return False
print(is_prime(11))  # Expected output: True
print(is_prime(4))   # Expected output: False
print(is_prime(2))   # Expected output: True
print(is_prime(1))   # Expected output: False