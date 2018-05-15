''' Stacking decorators'''
from functools import wraps
import time


def show_args(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        print('Hi from the decorator- args')
        print(args)
        result = function(*args, **kwargs)
        print('Hi again from decorator - kwargs')
        print(kwargs)
        return result
    return wrapper


def timeit(function):
    @wraps(function)
    def wrapper(*args, **kwargs):

        # before calling the decorated function
        print('==== Starting timer ======')
        start = time.time()

        # calling the function
        function(*args, **kwargs)

        # after calling the decorated function
        print('==== Ending the timer ====')
        end = time.time()
        print(f'{function.__name__} took {int(end-start)  }s to complete')

    return wrapper


@timeit
@show_args
def generate_report(*months, **parameters):
    time.sleep(2)
    print('\n\t Hi from the generate report function\n')


def main():
    parameters = dict(split_geos=True, include_suborgs=True, txn_rate=33)
    generate_report('November', 'October', 'December', **parameters)


if __name__ == '__main__':
    main()

