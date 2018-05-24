from collections import namedtuple
from random import choice
from itertools import islice


def print_breakers():
    print('===========================================')
    print('===========================================')


def get_workout(day):
    """Problem with big if, elif, else constructs"""
    print('Big if, elif and else constructs.')
    #Bad way to do
    if day == 'Monday':
        routine = 'Chest+biceps'
    elif day == 'Tuesday':
        return 'Back+triceps'
    elif day == 'Wednesday':
        routine = 'Core'
    elif day == 'Thursday':
        routine = 'Legs'
    elif day == 'Friday':
        routine = 'Shoulders'
    elif day in ('Saturday', 'Sunday'):
        routine = 'Rest'

    print('Bad way: day: {}, workout: {}'.format(day, routine))

    # good way 1, use dictionaries
    workouts = {'Monday': 'chest+biceps',
                'Tuesday': 'chest+triceps',
                'Wednesday': 'Core',
                'Thursday': 'Legs',
                'Friday': 'Shoulders',
                'Saturday': 'rest',
                'Sunday': 'rest'
                }
    print('Good way 1: Dictionaries! day: {}, workout: {}'.format(day, workouts.get(day, 'No day')))

    # good way 2, use dictionaries
    days = 'Monday Tuesday Wednesday Thursday Friday'.split()
    routines = 'chest+biceps chest+triceps Core Legs Shoulders'.split()
    workouts2 = dict(zip(days, routines))
    print('Good way 2: Dictionaries! day: {}, workout: {}'.format(day, workouts2.get(day, 'No day')))


def count_inside_loop():
    print('Counting inside a loop')
    days = 'Monday Tuesday Wednesday Thursday Friday'.split()

    # Bad way to print index of the items
    print('Bad way:')
    i = 0
    for day in days:
        i += 1
        print(f'{i}. {day}')

    print('Good way. Enumerate!')
    for i, day in enumerate(days):
        print(f'{i+1}.{day}')

    print('Good way. Enumerate with custom starting index.')
    for i, day in enumerate(days, start=1):
        print(f'{i}.{day}')


def using_context_manager():
    print('Using context manager')
    #Bad way
    try:
        f = open('text', 'w')
        f.write('Helo\n')
        raise Exception()
        f.close()
    except Exception:
        print('Exception occurred.')
        if not f.closed:
            print('File handle is not closed.')

    #Good way 1
    try:
        f = open('text', 'w')
        f.write('Helo\n')
        1/0
    except ZeroDivisionError:
        print('Exception: Division by zero.')
    finally:
        print('File handle closed.')
        f.close()

    #Best way
    with open('text', 'w') as f:
        f.write('helo\n')


def use_builtins():
    print('Using builtins')

    # Bad way: print 1 to 10 numbers
    i = 1
    while i <= 10:
        print(i, end=",")
        i += 1

    print("")
    # Good way: Use range()
    numbers = range(1, 11)
    print(list(numbers))

    # Bad way: Finding maximum
    routines = 'chest+biceps chest+triceps Core Legs Shoulders'.split()
    times = '45 50 30 55 40'.split()
    workout_times = dict(zip(routines, times))

    max_time = 0
    max_routine = ""
    for routine, time in workout_times.items():
        t = int(time)
        if t > max_time:
            max_time = t
            max_routine = routine
    print(f'Routine with max time: {max_routine}, time: {max_time}')

    # Good way
    print(max(workout_times.items(), key=lambda x: x[1]))
    print(min(workout_times.items(), key=lambda x:x[1]))


def using_tuples_and_named_tuples():
    print('using_tuples_and_named_tuples')
    # Swapping variable values. Bad way
    a = 1
    b = 2
    temp = a
    a = b
    b = temp
    print(f'{a}, {b}')

    # Using tuples, good way
    a = 1
    b = 2
    a, b = b, a
    print(f'{a}, {b}')

    # Using just tuples. Bad way
    workouts = ('Monday', 'chest+biceps', 45)
    print(f'On {workouts[0]}s, I do {workouts[1]} for {workouts[2]} minutes')

    # Using named tuples. Good way.
    Workout = namedtuple('Workout', 'day routine timing')
    workout = Workout(day='Monday', routine='Chest+biceps', timing='45')
    print(f'On {workout.day}s I do {workout.routine} for {workout.timing}')


def using_list_comprehension_and_generators():

    print('using_list_comprehension_and_generators')
    # Bad way
    days = 'Monday Tuesday Wednesday Thursday Friday'.split()
    for day in days:
        if day[0].lower() == 't':
            print(day)

    # Generators
    print([day for day in days if day[0].lower() == 't'])

    # Get a random day.
    days_gen = get_random_day(days)

    print(next(days_gen))
    print(next(days_gen))
    print(next(days_gen))
    print(next(days_gen))

    for _ in range(5):
        print(next(days_gen))

    # slicing generators using itertools islice
    slice_ = islice(days_gen, 100, 105)
    print(list(slice_))


def get_random_day(days):
    i = 0
    while True:
        i += 1
        yield i, choice(days)


def main():
    get_workout('Wednesday')
    print_breakers()
    count_inside_loop()
    print_breakers()
    using_context_manager()
    print_breakers()
    use_builtins()
    print_breakers()
    using_tuples_and_named_tuples()
    print_breakers()
    using_list_comprehension_and_generators()


if __name__ == '__main__':
    main()
