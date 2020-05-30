from functools import reduce

def myfun(x: list):
    '''
    var name is refenrce here change in x will result in change in actual var passed
    in python passing var in method is pass by reference default/
    BUT
    if we change the recevied refernec to something else it will create new 
    exapme in fucn myfunc1
    '''
    x[0] =10

def myfunc1(x: list):
    x = [10, 20, 30]


# keyword argument
def funKWArgs(firstname, lastname):
    print(f'firstname: {firstname}', f'lastname: {lastname}', sep='\t')    


def myArgsFun(*argv):
    '''
    it will accept any number of arguments; not keywords arguments
    we can itergate over it can use highor order fucntion such as map , filter to it.
    '''

    for arg in argv:
        print(arg, end=' ')


def myArgsFun1(first_arg, *argv):
    '''
    this is same as myArgsFun
    the only difference is first agr received in first_arg variable
    and rest all will get place in *argv
    '''
    print("\n")
    print('I am the first argument:: Name :: {}'.format(first_arg))
    print('below are the rest of the others :: >> ')
    for arg in argv:
        print(arg, end=', ')


if __name__ == "__main__":
    l = [1,2,3,4,5]
    print(l)
    myfun(l)
    print(l)
    ##
    myfunc1(l)
    print(l)

    funKWArgs(firstname='Pawan', lastname='Arora')
    funKWArgs(lastname='Arora', firstname='Pawan')


    #lambda function
    # lambda arguments: expression

    cube = lambda x: x*x*x
    print('cube',cube(3), sep=': ')

    li = [1,2,3,4,5,6,7,8,9]
    even = list(filter(lambda x: (x%2 == 0), li))
    print(even)

    square = list(map(lambda x: x*x, li))
    print(square)

    total = reduce(lambda x, y: x+y, li)
    print(total)


    myArgsFun('pawan','arora','jaipur','this is multiple','args', 'passed')
    myArgsFun1('pawan','arora','jaipur','this is multiple','args', 'passed')