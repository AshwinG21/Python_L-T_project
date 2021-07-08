import pytest
def calculate(x,y):
    return ((1023 * x )/ y)


def test_method():
    assert calculate(1,20) == 51.15
    assert calculate(2,20) == 102.3
    assert calculate(0.88,20) == 45.012
    assert calculate(-0.88, 20) == -45.012