def print_name(prefix):
    print(f'searching for prefix :: {prefix}')
    try:
        while True:
            name = (yield)
            if prefix in name:
                print('================== ',name, ' ==================')
    except GeneratorExit:
        print("Closing coroutine!!")



if __name__ == "__main__":
    corou = print_name('hello')
    corou.__next__()
    corou.send('pawan')
    corou.send('hello Pawan Arora')
    corou.close()