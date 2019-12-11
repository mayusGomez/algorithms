import logging


def partition(data: list = None, start_idx: int = None, last: int = None):
    """
    Execute the partition of quicksort around a pivot

    :param data: array of numbers
    :param start_idx: index of first element of sub-array
    :param last: last element of sub-array
    :return pivot_idx: pivot of array partitioned
    :return comparisons: number of comparisons executed
    """
    i = start_idx + 1
    for j in range(i, last):
        if data[j] < data[start_idx]:
            data[j], data[i] = data[i], data[j]  # swap position with i
            i += 1

    data[start_idx], data[i-1] = data[i-1], data[start_idx]
    logging.debug(f'partition, array:{data[start_idx:last]}, pivot={i-1}, comparisons={last-start_idx-1}')

    pivot_idx = i-1
    comparisons = (last-start_idx-1)
    return pivot_idx, comparisons


def pivot_median(data: list = None, start_idx: int = None, end_idx: int = None):
    return start_idx + 1


def quicksort(data: list = None, start_idx: int = None, last: int = None, pivot_function=None) -> int:
    """
    Quicksort

    Implementation inplace of quicksort algorithm
    :param data: iterable with number unsorted
    :param start_idx: index of first element of sub-array
    :param last: last element of sub-array
    :param pivot_function:
    :return:
    """
    logging.debug(f'Quicksort, array:{data[start_idx:last]}')

    if start_idx + 1 >= last:
        return 0

    if pivot_function:
        #  by default choose the first element for pivot, else use the function received
        pivot_chosen = pivot_function(data, start_idx, last)
        data[start_idx], data[pivot_chosen] = data[pivot_chosen], data[start_idx]  # swap pivot to first position

    pivot_idx, comparisons = partition(data, start_idx, last)
    comparisons_left = quicksort(data, start_idx, pivot_idx, pivot_function)  # left array
    comparisons_right = quicksort(data, pivot_idx+1, last, pivot_function)  # right array
    return comparisons + comparisons_left + comparisons_right


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
    with open('quicksort_01.txt') as file:
        numbers = file.read().rstrip('\n').split('\n')
    numbers = [int(x) for x in numbers]
    total_comparisons = quicksort(numbers, 0, len(numbers))
    logging.debug(f'total comparisons:{total_comparisons}')
    logging.debug(f'first number:{numbers[0]}')
    logging.debug(f'last number:{numbers[-1]}')
    logging.debug(f'3457 number:{numbers[3456]}')
    logging.debug(f'5678 number:{numbers[5677]}')
    logging.debug(f'8934 number:{numbers[8933]}')
