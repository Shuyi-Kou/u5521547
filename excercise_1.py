def morse_translator(text):
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }

    text = text.upper()
    morse_code_list = []
    for char in text:
        if char.isalpha():
            morse_code_list.append(morse_code_dict[char])
        elif char == " ":
            morse_code_list.append("/")
    morse_code_string = " ".join(morse_code_list)
    return morse_code_string

print(morse_translator("HELLO WORLD"))