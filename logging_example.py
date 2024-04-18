import logging


my_logger = logging.getLogger('solver')
my_logger.setLevel(logging.WARNING)

formatter = logging.Formatter('%(levelname)s - %(message)s')

file_handler = logging.FileHandler("logs/solver.log", mode="w")
file_handler.setFormatter(formatter)

my_logger.addHandler(file_handler)

# ----
def solve_quadratic_equation(a, b, c):
    my_logger.info("The function was called")
    my_logger.debug(f"a: {a}, b: {b}, c: {c}")

    delta = b ** 2 - 4 * a * c
    if delta < 0:
        my_logger.warning(f"Delta < 0: {delta}")

    try:
        x1 = (-b - delta ** 0.5) / (2 * a)
        x2 = (-b + delta ** 0.5) / (2 * a)
        if isinstance(x1, complex) or isinstance(x2, complex):
            raise Exception("The root is a complex number")
    except Exception as e:
        my_logger.exception("Error occured while solving the equation")
        x1, x2 = None, None

    return x1, x2


a, b, c = 1, 2, 4
x1, x2 = solve_quadratic_equation(a, b, c)
print(x1, x2)
