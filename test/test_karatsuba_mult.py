import pytest
from DivAndConq.karatsuba_mult import karatsuba_mult


def test_2d_karatsuba_mult():
    number_01 = 92
    number_02 = 81
    assert karatsuba_mult(number_01, number_02) == 7452


def test_4d_karatsuba_mult():
    number_01 = 9276
    number_02 = 8312
    assert karatsuba_mult(number_01, number_02) == 77102112


def test_8d_karatsuba_mult():
    number_01 = 92764576
    number_02 = 81431254
    assert karatsuba_mult(number_01, number_02) ==   7.553935750458300


def test_err01_karatsuba_mult():
    number_01 = 9276457
    number_02 = 8143125
    with pytest.raises(Exception):
        karatsuba_mult(number_01, number_02)


def test_err02_karatsuba_mult():
    number_01 = 92764578
    number_02 = 8143
    with pytest.raises(Exception):
        karatsuba_mult(number_01, number_02)

