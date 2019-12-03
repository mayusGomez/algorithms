

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


def count_split_inver(numbers_l: list, numbers_r: list) -> (int, list):
    """
    Count split inversion

    :param numbers_l: ordered list a
    :param numbers_r: ordered list b
    :return: count of inversions, ordered list (a + b)
    """
    result = []
    count = 0
    i = 0
    j = 0
    while i < len(numbers_l) and j < len(numbers_r):
        if numbers_l[i] <= numbers_r[j]:
            result.append(numbers_l[i])
            i += 1
            count += j
        else:
            result.append(numbers_r[j])
            j += 1

    if i >= len(numbers_l):
        result += numbers_r[j:]
    else:
        result += numbers_l[i:]
        count += len(numbers_l[i:]) * j

    return count, result


def recursive_approach(numbers: list) -> (int, list):
    """
    recursive approach of counting inversions

    This functions split in two sub-list, and for each sub-list et the count and the ordered list, and finally invoque
    the count_split_inver to count inversions in the union of both ordered sub-list.
    :param numbers: list of numbers
    :return: tuple with: counting invertions, ordered list
    """

    if len(numbers) <= 1:
        return 0, numbers

    mid = len(numbers) // 2
    count_a, left_numbers = recursive_approach(numbers[:mid])
    count_b, right_numbers = recursive_approach(numbers[mid:])
    count, ordered = count_split_inver(left_numbers, right_numbers)
    count += count_a + count_b
    return count, ordered


if __name__ == '__main__':
    with open('IntegerArray.txt') as file:
        numbers = file.read().rstrip('\n').split('\n')
    numbers = [int(x) for x in numbers]

    c, ordered = recursive_approach(numbers)
    print(f'Result, inversions:{c} [:15]={ordered[:15]}, [-15:]:{ordered[-15:]}')
