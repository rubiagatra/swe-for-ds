import pytest
from math_functions import add, divide, multiply  # Import fungsi yang akan diuji


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 3) == pytest.approx(
        2.333333
    )  # Gunakan pytest.approx untuk floating point
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)


def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-2, 3) == -6
    assert multiply(0, 10) == 0
