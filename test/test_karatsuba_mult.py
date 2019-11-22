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

