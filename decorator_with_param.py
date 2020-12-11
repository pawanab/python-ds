def receive_the_args(dec1, dec2, dec3):
    print("i was passed from wapper {0} {1} {2}".format(dec1, dec2, dec3))
    def wrapper_with_args(fun):
        def new_fun(arg1, arg2, arg3):
            print(f'fun has arguments {fun.__name__} {arg1} {arg2} {arg3} ')
            print(f'am extra that passed with wrapper {dec1} {dec2} {dec3}')

            fun(arg1, arg2, arg3)
        
        return new_fun
    return wrapper_with_args


@receive_the_args('p','a','w')
def check_args(a1, a2, a3):
    print(a1+a2+a3)


def check_scope(a):
    result = a**2
    return result


# check_args(1,2,3)
if __name__ == '__main__':
    print(check_scope.__code__)
