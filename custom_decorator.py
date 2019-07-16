def printdecorator(fn):  # function to be decorated passed as argument
    def print_wrapper(message, blahblah):  # wrap the show_me and extends its behaviour
        print('I am Decorated : ', end=' ')
        # actual show_me function (passed as 'fn' in printdecorator)
        fn(message, blahblah)
    # return print_wrapper (note not reuturned as function;)
    return print_wrapper


@printdecorator
def show_me(some_message, blahblah):
    print(some_message, blahblah, sep=" : ")


if __name__ == "__main__":
    show_me('pawan', 'blah HU')
