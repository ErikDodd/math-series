import pytest
# from package_name.module_name import function_name
from math_series.series import fibonacci

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

