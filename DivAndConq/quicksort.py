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


def pivot_median_of_3(data: list = None, start_idx: int = None, last: int = None) -> int:
    """
    Compute the number of comparisons using the "median-of-three" pivot rule. [The primary motivation
    behind this rule is to do a little bit of extra work to get much better performance on input arrays that are nearly
    sorted or reverse sorted.] In more detail, you should choose the pivot as follows. Consider the first, middle, and
    final elements of the given array. (If the array has odd length it should be clear what the "middle" element is;
    for an array with even length 2k2k, use the k^{th}kth element as the "middle" element. So for the array 4 5 6 7,
    the "middle" element is the second one ---- 5 and not 6!) Identify which of these three elements is the median
    (i.e., the one whose value is in between the other two), and use this as your pivot. As discussed in the first and
    second parts of this programming assignment, be sure to implement Partition exactly as described in the video lectures
    (including exchanging the pivot element with the first element just before the main Partition subroutine).

    :param data:
    :param start_idx:
    :param last:
    :return:
    """
    length = last - start_idx
    middle_idx = start_idx + (length // 2)
    if length % 2 == 0:
        middle_idx -= 1

    if data[start_idx] > data[middle_idx]:
        if data[start_idx] < data[last-1]:
            return start_idx
        elif data[middle_idx] > data[last-1]:
            return middle_idx
        else:
            return last - 1
    else:
        if data[start_idx] > data[last-1]:
            return start_idx
        elif data[middle_idx] < data[last-1]:
            return middle_idx
        else:
            return last - 1


def pivot_last(data: list = None, start_idx: int = None, last: int = None):
    """
    Choose the last element for pivot
    :param data:
    :param start_idx:
    :param last:
    :return: pivot index
    """
    return last - 1


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
    """with open('quicksort_01.txt') as file:
        numbers = file.read().rstrip('\n').split('\n')
    numbers = [int(x) for x in numbers]
    logging.debug(f'total comparisons:{total_comparisons}')
    logging.debug(f'first number:{numbers[0]}')
    logging.debug(f'last number:{numbers[-1]}')
    logging.debug(f'3457 number:{numbers[3456]}')
    logging.debug(f'5678 number:{numbers[5677]}')
    logging.debug(f'8934 number:{numbers[8933]}')
    """
    numbers = [5, 4, 7, 1, 2, 10, 8, 9, 6, 3]
    total_comparisons = quicksort(numbers, 0, len(numbers))
    logging.debug(f'first element= total comparisons:{total_comparisons}, array:{numbers}')
    logging.debug('---------------------------------------------------------')

    numbers = [5, 4, 7, 1, 2, 10, 8, 9, 6, 3]
    total_comparisons = quicksort(numbers, 0, len(numbers), pivot_last)
    logging.debug(f'last element = total comparisons:{total_comparisons}, array:{numbers}')
    logging.debug('---------------------------------------------------------')

    numbers = [5, 4, 7, 1, 2, 10, 8, 9, 6, 3]
    total_comparisons = quicksort(numbers, 0, len(numbers), pivot_median_of_3)
    logging.debug(f'median of 3 = total comparisons:{total_comparisons}, array:{numbers}')

