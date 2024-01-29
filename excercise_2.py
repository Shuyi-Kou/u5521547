def case_counter(text):
    n = 0
    s = 0
    for char in text:
        if char.isupper():
            n += 1
        elif char. islower():
            s += 1
        else:
            continue
    print(f"uppercase letters: {n},lowercase letters:{s}")
case_counter("1234!")
