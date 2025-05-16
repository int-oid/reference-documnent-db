import random
import string

def generate_ref_number():
    letters_1 = ''.join(random.choices(string.ascii_uppercase, k=2))
    numbers_1 = ''.join(random.choices(string.digits, k=8))
    letter_2 = random.choice(string.ascii_uppercase)
    numbers_2 = ''.join(random.choices(string.digits, k=5))
    ref_number = f"{letters_1}{numbers_1}{letter_2}{numbers_2}"
    return ref_number

print(generate_ref_number())
