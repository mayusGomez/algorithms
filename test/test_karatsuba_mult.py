import pytest
from DivAndConq.karatsuba_mult import karatsuba_mult, fix_number_length


def test_01_karatsuba_mult():
    x = '900'
    y = '1'
    assert fix_number_length(x, y) == ('0900', '0001')
    assert fix_number_length(y, x) == ('0001', '0900')


def test_02_karatsuba_mult():
    x = '9877'
    y = '1'
    assert fix_number_length(x, y) == ('9877', '0001')


def test_03_karatsuba_mult():
    x = '98771'
    y = '187652'
    assert fix_number_length(x, y) == ('00098771', '00187652')


def test_1d_karatsuba_mult():
    number_01 = '2'
    number_02 = '8'
    assert karatsuba_mult(number_01, number_02) == 16


def test_2d_karatsuba_mult():
    number_01 = '92'
    number_02 = '81'
    assert karatsuba_mult(number_01, number_02) == 7452


def test_4d_karatsuba_mult():
    number_01 = '9276'
    number_02 = '8312'
    assert karatsuba_mult(number_01, number_02) == 77102112


def test_8d_karatsuba_mult():
    number_01 = '92764576'
    number_02 = '81431254'
    assert karatsuba_mult(number_01, number_02) == 7553935750458300
