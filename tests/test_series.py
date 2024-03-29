import pytest
# from package_name.module_name import function_name
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

# pytest tests must start with "test_"


def test_fibonacci_exists():
    assert fibonacci


def test_fibonacci_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fibonacci_6():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected


def test_fibonacci_7():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected


def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_4():
    actual = lucas(4)
    expected = 7
    assert actual == expected


def test_lucas_6():
    actual = lucas(6)
    expected = 18
    assert actual == expected


def test_lucas_7():
    actual = lucas(7)
    expected = 29
    assert actual == expected


def test_sum_series_0():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series_2():
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected

