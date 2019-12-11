import logging


def partition(data: list = None, start_idx: int = None, last: int = None):
    """
    Execute the partition of quicksort around a pivot

    :param data:
    :param start_idx:
    :param last:
    :return:
    """
    i = start_idx + 1
    for j in range(i, last):
        if data[j] < data[start_idx]:
            data[j], data[i] = data[i], data[j]  # swap position with i
            i += 1

    data[start_idx], data[i-1] = data[i-1], data[start_idx]
    logging.debug(f'partition, array:{data[start_idx:last]}, pivot={i-1}, comparisons={last-start_idx-1}')

    """pivot_idx = (len(data[start_idx: last]) // 2) + start_idx
    comparisons = 0"""
    return i-1, (last-start_idx-1)


def pivot_median(data: list = None, start_idx: int = None, end_idx: int = None):
    return start_idx + 1


def quicksort(data: list = None, start_idx: int = None, last: int = None, pivot_function=None) -> None:
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
        return

    if pivot_function:
        #  by default choose the first element for pivot, else use the function received
        pivot_chosen = pivot_function(data, start_idx, last)
        data[start_idx], data[pivot_chosen] = data[pivot_chosen], data[start_idx]  # swap pivot to first position

    pivot_idx, comparisons = partition(data, start_idx, last)
    quicksort(data, start_idx, pivot_idx, pivot_function)  # left array
    quicksort(data, pivot_idx+1, last, pivot_function)  # right array


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
    l = [5, 4, 7, 1, 2, 3, 8, 9, 6, 10]
    quicksort(l, 0, len(l))
    logging.debug(f'final array:{l}')
