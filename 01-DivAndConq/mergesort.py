"""
Mergesort implementation
"""
import random


def merge(numbers_list):
    """
    Mergesort algorithm
    :param numbers_list: list of number to order
    :return: new list with numbers ordered
    """

    if len(numbers_list) <= 1:
        return numbers_list

    result = []
    # identify the middle item
    mid = len(numbers_list) // 2
    numbers_list_a = merge(numbers_list[:mid])
    numbers_list_b = merge(numbers_list[mid:])

    i = 0
    j = 0

    for k in numbers_list:
        if i < len(numbers_list_a) and j < len(numbers_list_b):
            if numbers_list_a[i] <= numbers_list_b[j]:
                result.append(numbers_list_a[i])
                i += 1
            else:
                result.append(numbers_list_b[j])
                j += 1
        else:
            if i >= len(numbers_list_a):
                result += numbers_list_b[j:]
            else:
                result += numbers_list_a[i:]
            break

    return result


if __name__ == '__main__':
    numbers_list = [random.randint(0, 100) for x in range(21)]
    print(f'intial: {numbers_list}')
    numbers_list = merge(numbers_list)
    print(f'result: {numbers_list}')
