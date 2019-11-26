import math
import functools
import operator


def fix_number_length(x_fix: str, y_fix: str):
    """
    Fix the length of two number

    For the Karatsuba multiplication both numbers must be the same digits and the length of both numbers must be power
    of 2. For example, if the number is '987' then the length of this number is 3 and 3 is not power of 2, '987' must be
    transform to '0987' because 4 is power of 2. The number '89872' must be transform to '00089872' and so on.

    :param x_fix: number 01
    :param y_fix: number 02
    :return: tuple of fixed numbers
    """
    # Find the max length of both numbers
    max_length = len(x_fix) if len(x_fix) >= len(y_fix) else len(y_fix)
    power_2_number = 0

    # Find the power of two length
    log_operation = math.log(max_length, 2)
    if log_operation % 1 != 0:
        power_2_number = (log_operation // 1) + 1
    else:
        power_2_number = log_operation

    number_digits = 2**power_2_number

    # Fix x
    if len(x_fix) < number_digits:
        zero_str = '0' * int(number_digits - len(x_fix))
        x_fix = zero_str + x_fix

    # Fix y
    if len(y_fix) < number_digits:
        zero_str = '0' * int(number_digits - len(y_fix))
        y_fix = zero_str + y_fix

    return x_fix, y_fix


def recursive_karatsuba_mult(x_str: str, y_str: str) -> int:
    """
    Karatsuba multiplication implementation

    Both numbers must be power of two, the algorithm of karatsuba is:
    1. Numbers to multiply: 8976 * 3421
    2. Divide the problem: a=89, b=76, c=34, d=21
    3.1. Compute: a*c
    3.2. Compute: b*d
    3.3. Compute: (a+b)*(c+d)
    3.4. Compute: (3.3) - (3.2) - (3.1)
    3.5. Compute: (3.1)*(10**len(8976)) + (3.2) + ((3.4)*(10**(len(8976)/2)))

    Base case:
    - Some number is zero
    - some number is < 10

    :param x: number 01 : str
    :param y: number 02 : str
    :return: number 01 * number 02
    """
    number_digits = len(x_str)
    number_digits_mid = int(number_digits / 2)

    # Base case, 1 digit or zero
    if int(x_str) == 0 or int(y_str) == 0:
        return 0
    elif int(x_str) < 10:
        return functools.reduce(operator.add, [int(y_str)] * int(x_str))
    elif int(y_str) < 10:
        return functools.reduce(operator.add, [int(x_str)]*int(y_str))
    else:
        a = x_str[:number_digits_mid]
        b = x_str[number_digits_mid:]
        c = y_str[:number_digits_mid]
        d = y_str[number_digits_mid:]

        compute_01 = recursive_karatsuba_mult(a, c)
        compute_02 = recursive_karatsuba_mult(b, d)

        compute_03_1 = int(a)+int(b)
        compute_03_2 = int(c)+int(d)
        compute_03 = karatsuba_mult(compute_03_1, compute_03_2)

        compute_04 = compute_03 - compute_02 - compute_01

        # Multiply by 10.... adding zeros
        compute_05_1_power_str = '0' * number_digits
        compute_05_1 = int(str(compute_01) + compute_05_1_power_str)

        # Multiply by 10.... adding zeros
        compute_05_2_power_str = '0' * (number_digits//2)
        compute_05_2 = int(str(compute_04) + compute_05_2_power_str)

        compute_05 = compute_05_1 + compute_02 + compute_05_2

        return compute_05


def karatsuba_mult(x: int, y: int) -> int:
    """
    Karatsuba multiplication of two numbers

    First fix the numbers length (power of 2) and then call the recursive method
    :param x: number 1
    :param y: number 2
    :return: recursive_karatsuba_mult(number 1 , number 2)
    """
    x_str, y_str = fix_number_length(str(x), str(y))
    return recursive_karatsuba_mult(x_str, y_str)


if __name__ == '__main__':
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
    result = karatsuba_mult(x, y)
    print('x[{}] * y[{}] = {}'.format(x, y, result))
