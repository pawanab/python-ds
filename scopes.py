# global scope variable num
num = 1
'''
    scoping is defined by LEGB rule in python
    Local,
    Enclosing,
    Global,
    Built-in
'''


def local_scpose_update_fail():
    '''
        try to update the value of global scope variable num
    '''
    num += 6


def local_scpose_only_access():
    print(f'value of num from global scope is {num}')
    print("\n")


def local_scpose_update_pass():
    global num #nonlocal can also be user instaed of localre
    num += 6

    print(f'New value of global var num is {num}')
    print("\n")


'''
    lambda function `even`
'''   
even = lambda x: not bool(x % 2)

if __name__ == '__main__':
    n = range(0,10)
    x = [n for n in range(0,10) if even(n)]
    print(x)


    local_scpose_only_access()
    local_scpose_update_pass()
    local_scpose_update_fail()