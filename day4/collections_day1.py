from collections import namedtuple, defaultdict, Counter, deque
import random, datetime


def main():

    # Named tuple
    # It is a convenient way to define a class without methods
    # Named tuples are a easily implementable data type. They make the code more readable
    User = namedtuple("User", "first last")
    user = User(first='Vipin', last='Reyaroth')
    print('The user is {} {}'.format(user.first, user.last))

    # Default dictionary (defaultdict)
    # It is container. It is similar as 'dict', but the value's data type is given during the initialisation.
    # It basically provides a value for a non existent key, which is very helpful to avoid KeyError situations
    # Very helpful when building a nested data structure and we have to account for a key not being there
    challenges_done = [('vipin', 10),
                       ('john', 30),
                       ('kenny', 100),
                       ('vipin', 25),
                       ('john', 26),
                       ('kenny', 95)]

    challenges = defaultdict(list)
    for name, challenge in challenges_done:
        challenges[name].append(challenge)

    print(challenges)

    # Counter
    # Counter is a container which is useful when we have a use case to count the distinct occurrences in a Collection
    # There are different ways to count distinct occurrences in a Collection
    # a) Using a dict (with a pre-check for key existence)
    # b) Using a dict with setdefault function
    # c) Using a default dict
    # d) Using a Counter
    food = ['soy', 'grape', 'orange', 'soy']
    counter = Counter(food)
    print(counter)

    # Deque
    # It's a list like container with fast appends and pops at either end
    lst = list(range(1000000))
    deq = deque(range(1000000))

    start = datetime.datetime.now()
    insert_and_delete(lst)
    end = datetime.datetime.now()
    print(end-start)

    start = datetime.datetime.now()
    insert_and_delete(deq)
    end = datetime.datetime.now()
    print(end-start)


def insert_and_delete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)


if __name__ == '__main__':
    main()
