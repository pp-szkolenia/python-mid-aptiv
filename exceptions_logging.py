import logging


logger = logging.getLogger("my_logger")


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception("Tried to divide by 0")
    else:
        return result


print(divide(2, 0))
