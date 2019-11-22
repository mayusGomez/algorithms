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


def karatsuba_mult(x_str: str, y_str: str):
    """
    Karatsuba multiplication


    :param x: number 01
    :param y: number 02
    :return: number 01 * number 02
    """
    number_digits = len(x_str)

    # Base case, both numbers have 1 digit
    if len(x_str) == len(y_str) == 1:
        return functools.reduce(operator.add, [int(x)]*int(y))
    else:
        None


if __name__ == '__main__':
    x = 9
    y = 32
    x, y = fix_number_length(str(x), str(y))
    result = karatsuba_mult(x, y)
    print('x[{}] * y[{}] = {}'.format(x, y, result))
