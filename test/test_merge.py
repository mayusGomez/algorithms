from DivAndConq.mergesort import merge


def test_1_mergesort():
    initial = [3]
    ordered = [3]
    sorted = merge(initial)
    assert sorted == ordered


def test_2_mergesort():
    initial = [63, 26]
    ordered = [26, 63]
    sorted = merge(initial)
    assert sorted == ordered


def test_15_mergesort():
    initial = [7, 57, 93, 11, 87, 7, 39, 22, 47, 89, 63, 26, 26, 98, 80]
    ordered = [7, 7, 11, 22, 26, 26, 39, 47, 57, 63, 80, 87, 89, 93, 98]
    sorted = merge(initial)
    assert sorted == ordered


def test_50_mergesort():
    initial = [47, 95, 65, 69, 62, 63, 37, 38, 52, 52, 10, 26, 2, 95, 29, 16, 66, 16, 24, 70, 59, 43, 2, 98, 18, 71, 0,
               2, 80, 98, 44, 17, 56, 69, 74, 34, 18, 6, 45, 25, 17, 51, 17, 4, 73, 27, 38, 54, 46, 46]
    ordered = [0, 2, 2, 2, 4, 6, 10, 16, 16, 17, 17, 17, 18, 18, 24, 25, 26, 27, 29, 34, 37, 38, 38, 43, 44, 45, 46, 46,
               47, 51, 52, 52, 54, 56, 59, 62, 63, 65, 66, 69, 69, 70, 71, 73, 74, 80, 95, 95, 98, 98]
    sorted = merge(initial)
    assert sorted == ordered
