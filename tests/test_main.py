"""
Tests for the main module.
"""

import pytest
from src.main import add, main, multiply


def test_main():
    """Test the main function."""
    result = main()
    assert result == "Hello from MLOps Git Exercise!"
    assert isinstance(result, str)


def test_add():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(1.5, 2.5) == 4.0


def test_add_negative():
    """Test add with negative numbers."""
    assert add(-5, -3) == -8


def test_multiply():
    """Test the multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(0, 100) == 0
    assert multiply(-2, 3) == -6
    assert multiply(1.5, 2) == 3.0


def test_multiply_by_zero():
    """Test multiply by zero."""
    assert multiply(42, 0) == 0


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (10, 20, 30),
])
def test_add_parametrized(a, b, expected):
    """Test add with parametrized values."""
    assert add(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (5, 5, 25),
    (0, 100, 0),
    (-2, -3, 6),
])
def test_multiply_parametrized(a, b, expected):
    """Test multiply with parametrized values."""
    assert multiply(a, b) == expected
