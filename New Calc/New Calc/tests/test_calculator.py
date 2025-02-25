
import sys
import os
import pytest

# Add the parent directory to the sys.path to ensure the calculator module can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculator import Calculator

def test_addition():
    calc = Calculator()
    assert calc.addition(3, 7) == 10
    assert calc.addition(-3, 7) == 4
    assert calc.addition(-3, -7) == -10

def test_subtraction():
    calc = Calculator()
    assert calc.subtraction(5, 2) == 3
    assert calc.subtraction(-5, -2) == -3
    assert calc.subtraction(0, 0) == 0
    assert calc.subtraction(2, 5) == -3

def test_multiplication():
    calc = Calculator()
    assert calc.multiplication(3, 7) == 21
    assert calc.multiplication(-3, 7) == -21
    assert calc.multiplication(-3, -7) == 21

def test_division():
    calc = Calculator()
    assert calc.division(10, 2) == 5
    assert calc.division(-10, 2) == -5


    assert calc.division(-10, -2) == 5
    with pytest.raises(ValueError):
        calc.division(10, 0)


