import random


def kelvin_to_celsius(temp_k):
    if temp_k < 0:
        raise ValueError("Negative temperature in Kelvin")

    if not isinstance(temp_k, (int, float)):
        raise TypeError("Invalid type")

    return temp_k - 273.15


def check_if_greater(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Invalid type")

    random_number = random.random()
    if x > random_number:
        return "Number is greater than random"
    elif x < random_number:
        return "Number is less than random"
    else:
        return "Number is equal to random"


def calculate_rectangle_area(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError("Invalid type of a")

    if not isinstance(b, (int, float)):
        raise TypeError("Invalid type of b")

    if a <= 0 or b <= 0:
        return None

    return a * b
