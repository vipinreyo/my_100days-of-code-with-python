from functools import wraps
import time


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
def generate_report():
    time.sleep(2)
    print('\n\t Hi from the generate report function\n')


def main():
    generate_report()


if __name__ == '__main__':
    main()
