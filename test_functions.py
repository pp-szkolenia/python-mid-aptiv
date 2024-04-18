import unittest
from unittest.mock import MagicMock, patch

from functions import kelvin_to_celsius, check_if_greater, calculate_rectangle_area


class TestFunctions(unittest.TestCase):
    def test_kelvin_to_celsius(self):
        self.assertEqual(kelvin_to_celsius(273.15), 0)

        with self.assertRaises(ValueError):
            kelvin_to_celsius(-1)

        with self.assertRaises(TypeError):
            kelvin_to_celsius("123")

    def test_check_if_greater(self):
        random_mock = MagicMock(return_value=0.5)
        with patch("functions.random.random", random_mock):
            self.assertEqual(check_if_greater(1), "Number is greater than random")
            self.assertEqual(check_if_greater(0), "Number is less than random")
            self.assertEqual(check_if_greater(0.5), "Number is equal to random")

    def test_calculate_rectangle_area(self):
        self.assertEqual(calculate_rectangle_area(2, 3), 6)

        with self.assertRaises(TypeError):
            calculate_rectangle_area("a", 3)
        with self.assertRaises(TypeError):
            calculate_rectangle_area(2, "b")

        self.assertIsNone(calculate_rectangle_area(0, 4))
