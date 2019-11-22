

def karatsuba_mult(number_01, number_02):
    number_01_digits = len(str(number_01))
    number_02_digits = len(str(number_02))
    if number_01_digits % 2 != 0:
        raise("Your number is not power of 2")
    if number_01_digits != number_02_digits:
        raise("Both numbers must have the same number of digits")


