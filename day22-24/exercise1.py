from functools import wraps


def show_args(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print('Hi from the decorator- args')
        print(args)
        result = function(*args, **kwargs)
        print('Hi again from decorator - kwargs')
        print(kwargs)
        return result
    return wrapper

@show_args
def get_profile(name, active=True, *sports, **awards):
    print('\n\tHi from get profile function\n')


def main():
    get_profile('Vipin', False, 'cricket', 'soccer', pythonista= 'special honour', topcoder='2017 free code camp')


if __name__ == '__main__':
    main()
