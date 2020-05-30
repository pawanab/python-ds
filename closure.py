print('------ closure in python ---------')
import logging

logging.basicConfig(filename='closure_logs.log', level=logging.INFO)

def logger(fun):
    def log_func(*args):
        logging.info(
            f'Running fun {fun.__name__} with args : {args}'
        )
        
        result = fun(*args)
        print('{}{} : {}'.format(fun.__name__, args, result) )
    return log_func


def add(a, b):
    return a + b

def sub(a, b):
    return a - b 


if __name__ == "__main__":
    
    logger_add = logger(add)
    logger_sub = logger(sub)

    logger_add(1, 2)
    logger_sub(5, 3)