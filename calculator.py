import logging


class Calculator:
    @staticmethod
    def add(a, b):
        # my_logger.debug(f"Operation: add, a: {a}, b: {b}")
        return a + b

    @staticmethod
    def subtract(a, b):
        # my_logger.debug(f"Operation: subtract, a: {a}, b: {b}")
        return a - b

    @staticmethod
    def multiply(a, b):
        # my_logger.debug(f"Operation: multiply, a: {a}, b: {b}")
        return a * b

    @staticmethod
    def divide(a, b):
        # my_logger.debug(f"Operation: divide, a: {a}, b: {b}")
        # if b == 0:
        #     # my_logger.warning("Division by 0, None returned")
        #     return None

        return a / b


# calc = Calculator()
# calc.divide(3, 0)

#
# my_logger = logging.getLogger("calc_logger")
#
# file_formatter = logging.Formatter(
#     '%(asctime)s - %(levelname)s - %(message)s')
# stream_formatter = logging.Formatter(
#     "%(asctime)s - %(levelname)s - %(message)s")
#
# file_handler = logging.FileHandler('logs/calculator.log', mode="w")
# file_handler.setFormatter(file_formatter)
#
# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(stream_formatter)
#
# file_handler.setLevel(logging.DEBUG)
# stream_handler.setLevel(logging.DEBUG)
#
# my_logger.addHandler(file_handler)
# my_logger.addHandler(stream_handler)
#
# my_logger.setLevel(logging.DEBUG)
