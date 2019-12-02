from DivAndConq.counting_invertions import brute_force, recursive_aproach


def test_bf_001():
    numbers = [1, 3, 5, 2, 4, 6]
    counting_invertions = brute_force(numbers)
    assert counting_invertions == 3


def test_ra_001():
    numbers = [1, 3, 5, 2, 4, 6]
    counting_invertions = recursive_aproach(numbers)
    assert counting_invertions == 3
