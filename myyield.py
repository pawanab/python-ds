def square():
    i = 1
    while True:
        yield i*i
        i += 1


def fibonacci(limit):
    a, b= 0, 1

    while a < limit:
        yield a
        a, b = b, a + b


def reverse(data):
    for i in range(len(data)-1, -1, -1):
        yield data[i]


if __name__ == '__main__':
    for n in square():
        if n > 100:
            break
        print(n)

    for x in fibonacci(15):
        print(x, end=' ')
    
    print("\n")
    for i in reverse('pawan'):
        print(i, end='')
