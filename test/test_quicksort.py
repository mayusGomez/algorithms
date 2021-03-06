from DivAndConq.quicksort import quicksort, pivot_last, pivot_median_of_3


def test_001():
    l = [5, 4, 7, 1, 2, 3, 8, 9, 6, 10]
    total_comparisons = quicksort(l, 0, len(l))
    assert total_comparisons == 19 and l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_002():
    with open('DivAndConq/quicksort_01.txt') as file:
        numbers = file.read().rstrip('\n').split('\n')
    numbers = [int(x) for x in numbers]
    total_comparisons = quicksort(numbers, 0, len(numbers))
    assert total_comparisons == 162085
    for n in range(len(numbers)):
        assert n+1 == numbers[n]


def test_003():
    with open('DivAndConq/quicksort_01.txt') as file:
        numbers = file.read().rstrip('\n').split('\n')
    numbers = [int(x) for x in numbers]
    total_comparisons = quicksort(numbers, 0, len(numbers), pivot_last)
    assert total_comparisons == 164123
    for n in range(len(numbers)):
        assert n+1 == numbers[n]


def test_004():
    with open('DivAndConq/quicksort_01.txt') as file:
        numbers = file.read().rstrip('\n').split('\n')
    numbers = [int(x) for x in numbers]
    total_comparisons = quicksort(numbers, 0, len(numbers), pivot_median_of_3)
    assert total_comparisons == 138382
    for n in range(len(numbers)):
        assert n+1 == numbers[n]
