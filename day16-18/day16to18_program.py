import random

def main():
    NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos', 'vipin reyaroth',
            'sandra bullock', 'keanu reeves', 'bob belderbos', 'brad pitt', 'matt damon', 'brad pitt']

    # List comprehension to convert the list with names in title case
    NAMES_IN_TITLE_CASE = [name.title() for name in NAMES]
    print(NAMES_IN_TITLE_CASE)

    # List comprehension to reverse first and last names
    NAMES_IN_REVERSE = [reverse_name(name) for name in NAMES]
    print(NAMES_IN_REVERSE)

    # a generator to generate a pair of names
    pairs = gen_pairs(NAMES)

    for _ in range(0, 10):
        print(next(pairs))


# Helper function
def reverse_name(name):
    first, last = name.split()
    return f'{last} {first}'


def gen_pairs(names):
    first_names = [name.split()[0].title() for name in names]

    while True:
        first, second = None, None

        while first == second:
            first, second = random.sample(first_names, 2)

        yield f'{first} teams up with {second}'


if __name__ == '__main__':
    main()
