import time 
from myyield import fibonacci
from starpattern import pypattern


def welcome(func):
    def say_hello():
        print('Hello... ', end=' ')
        func()
    return say_hello


def smart_divide(func):
    def divide(a, b):
        if b == 0:
            # print("Whoops! cannot divide")
            return "Whoops! cannot divide"
        return func(a, b)
    return divide


def beautiful_print(func):
    def change_print(*args):
        print('*********************************', end="\t")
        func(*args)
    return change_print



def total_execution_time(func):
    def execute(*args, **kwargs):
        begin = time.time()
        
        func(*args, **kwargs)

        end = time.time()
        print(f'actual time taken to execute the function == {func.__name__} == is :=: {end-begin}')
    return execute


def memorize_factorial(func):
    memory = {}
    def memorize(num):
        if num not in memory:
            memory[num] = func(num)
        return memory[num]
    return memorize


@memorize_factorial
def facto(n):
    if n == 1:
        return 1
    return n * facto(n-1)

@beautiful_print
def show_me(*msg):
    print(*msg)



@smart_divide
def actual_divide(a, b):
    return a/b


@welcome
def agent():
    print('Pawan')


@total_execution_time
def nfibonacci(n):
    for x in fibonacci(n):
        print(x)

@total_execution_time
def star_chapo(n):
    pypattern(n)



if __name__ == "__main__":
    """ agent_hello = welcome(agent)
    agent_hello() """

    agent()
    print(actual_divide(10, 5))
    print(actual_divide(10, 0))

    show_me('Pawan', 'Arora','multiple', 'args')

    nfibonacci(15)
    star_chapo(15)
    print(facto(4))