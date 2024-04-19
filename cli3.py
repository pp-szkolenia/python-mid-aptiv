import fire


# def add(x, y):
#     return x + y
#
# def subtract(x, y):
#     return x - y

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x*y

    def divide(self, x, y):
        return x/y

if __name__ == "__main__":
    fire.Fire(Calculator)
    # fire.Fire({"add": add, "subtract": subtract})
