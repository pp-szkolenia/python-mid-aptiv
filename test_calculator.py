import pytest
from calculator import Calculator

calc = Calculator()


def test_add():
    assert calc.add(1, 2) == 3
    assert calc.add(3, 5) == 8
    assert isinstance(calc.add(1, 2), int)


def test_subtract():
    assert calc.subtract(4, 2) == 2


def test_multiply():
    assert calc.multiply(4, 1) == 4


def test_divide():
    assert calc.divide(4, 2) == 2
    with pytest.raises(ZeroDivisionError):
        calc.divide(4, 0)








# import unittest
# from calculator import Calculator
#
# calc = Calculator()
#
#
# class TestCalculator(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(calc.add(1, 2), 3)
#         self.assertEqual(calc.add(-1, -2), -3)
#
#     def test_subtract(self):
#         self.assertEqual(calc.subtract(1, 2), -1)
#         self.assertEqual(calc.subtract(2, 2), 0)
#         self.assertNotIn(0, [1, 2, 3])
#
#     def test_multiply(self):
#         self.assertEqual(calc.multiply(1, 2), 2)
#
#     def test_divide(self):
#         self.assertEqual(calc.divide(2, 2), 1)
#         with self.assertRaises(ZeroDivisionError):
#             calc.divide(3, 0)
