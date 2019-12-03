from DivAndConq.counting_invertions import brute_force, recursive_approach


def test_bf_001():
    numbers = [1, 3, 5, 2, 4, 6]
    counting_invertions = brute_force(numbers)
    assert counting_invertions == 3


def test_ra_001():
    numbers = [1, 3, 5, 2, 4, 6]
    counting_invertions, numbers_ordered = recursive_approach(numbers)
    assert counting_invertions == 3 and numbers_ordered == [1, 2, 3, 4, 5, 6]


def test_ra_002():
    numbers = [5, 7, 8, 9, 10, 20, 26, 0, 1, 2, 3, 6, 21, 25]
    counting_invertions, numbers_ordered = recursive_approach(numbers)
    assert counting_invertions == 36 and numbers_ordered == [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 20, 21, 25, 26]


def test_ra_003():
    with open('DivAndConq/IntegerArray.txt') as file:
        numbers = file.read().rstrip('\n').split('\n')
    numbers = [int(x) for x in numbers]

    c, ordered = recursive_approach(numbers)
    assert c == 2407905288
