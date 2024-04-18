from calculator import Calculator, my_logger


calc = Calculator()


my_logger.info("Script started")

print(calc.add(1, 2))
print(calc.subtract(1, 2))
print(calc.multiply(1, 2))
print(calc.divide(1, 0))

my_logger.info("Script ended")