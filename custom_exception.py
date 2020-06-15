import sys

class MyCustomError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def client_code(a, b):
    if b <= 0:
        tb = sys.exc_info()[2]
        raise MyCustomError('Demonator can not be 0 or less.').with_traceback(tb)

    return a/b


if __name__ == "__main__":
    a1 = client_code(10, 5)
    print(f'result of 10 / 5 is :: {a1}')
    try:
        a2 = client_code(10, -1)
        print(f'result of 10 / -1 is :: {a2}')
    except MyCustomError as e:
        print(e)