import pytest
from DivAndConq.karatsuba_mult import karatsuba_mult, fix_number_length, recursive_karatsuba_mult


def test_01_fix_number_length():
    x = '900'
    y = '1'
    assert fix_number_length(x, y) == ('0900', '0001')
    assert fix_number_length(y, x) == ('0001', '0900')


def test_02_fix_number_length():
    x = '9877'
    y = '1'
    assert fix_number_length(x, y) == ('9877', '0001')


def test_03_fix_number_length():
    x = '98771'
    y = '187652'
    assert fix_number_length(x, y) == ('00098771', '00187652')


def test_1d_karatsuba_mult():
    x = '2'
    y = '8'
    assert recursive_karatsuba_mult(x, y) == (int(x) * int(y))


def test_2d_karatsuba_mult():
    x = '92'
    y = '81'
    assert recursive_karatsuba_mult(x, y) == (int(x) * int(y))


def test_4d_karatsuba_mult():
    x = '9276'
    y = '8312'
    assert recursive_karatsuba_mult(x, y) == (int(x) * int(y))


def test_8d_karatsuba_mult():
    x = '92764576'
    y = '81431254'
    assert recursive_karatsuba_mult(x, y) == (int(x) * int(y))


def test_xd_karatsuba_mult():
    x = '3141592653589793238462643383279502884197169399375105820974944592'
    y = '2718281828459045235360287471352662497757247093699959574966967627'
    assert recursive_karatsuba_mult(x, y) == (int(x) * int(y))
