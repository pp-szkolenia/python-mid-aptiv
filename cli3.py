import fire


class SimpleCalculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x*y

    def divide(self, x, y):
        return x/y


class AdvancedCalculator:
    def sqrt(self, x):
        return x**0.5

    def exp(self, x):
        return 2.71 ** x


class Pipeline:
    def __init__(self):
        self.simple = SimpleCalculator()
        self.advanced = AdvancedCalculator()

    def info(self):
        return "Simple and advanced calculator"


if __name__ == "__main__":
    fire.Fire(Pipeline)
    # fire.Fire({"add": add, "subtract": subtract})
