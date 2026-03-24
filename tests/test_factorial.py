import pytest
from mymath.factorial import factorial


def test_3():
    assert factorial(3) == 6

def test_2():
    assert factorial(2) == 2

def test_0():
    assert factorial(0) == 1

def test_negative():
    with pytest.raises(ValueError):
        factorial(-1)
