import sys


def add(x, y):
    return x + y


if __name__ == "__main__":
    x = int(sys.argv[1])
    y = int(sys.argv[2])

    print(add(x, y))
