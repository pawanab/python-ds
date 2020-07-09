'''
execute some code on exit 
i.e whenever a crash happen execute some code just before program exit

module: atexit
'''
import atexit

@atexit.register
def run_before_program_exit():
    print('I will be printed very last')
    print('You can use me to cleanup anthing.')



'''
get output of print in file instead of standard output
'''
def print_in_file(data_to_save):
    with open('print_log.txt', mode='a') as f:
        print(data_to_save, file=f, flush=True)


'''
quickly calculate function running time.
'''
import time, timeit

def addAll(*args):
    sum = 0
    for i in args:
        sum += i
    print('sum = ', sum)


def fibo_no_cache(n):
    if n < 2:
        return n
    return (fibo_no_cache(n-2) + fibo_no_cache(n-1))

'''
lru cache
'''
from functools import lru_cache

@lru_cache(None)
def fibo_with_cache(n):
    if n < 2:
        return n
    return fibo_with_cache(n-2) + fibo_with_cache(n-1)



if __name__ == "__main__":
    print_in_file('aur ab yeh b karo.')

    print(timeit.timeit(lambda: print(fibo_no_cache(9)), number=1))
    print("\n")
    print(timeit.timeit(lambda: fibo_with_cache(500), number=1))
    print(fibo_with_cache(5))