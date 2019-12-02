

def brute_force(numbers: list) -> int:
    """
    Brute force for counting invertions

    This aproach not work for a large n
    :param numbers: list of numbers
    :return: number of invertions
    """
    count = 0
    for i, number in enumerate(numbers[:-1]):
        for compare in numbers[i+1:]:
            if number > compare:
                count += 1
    return count


def recursive_aproach(numbers: list) -> int:
    return 0


if __name__ == '__main__':
    with open('IntegerArray.txt') as file:
        numbers = file.read().rstrip('\n').split('\n')

    n = brute_force(numbers[:100])

    print(f'Result, n:{n}')

