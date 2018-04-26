
def main():
    #list
    # mutable
    empty_list = [] # empty list

    lst = list("Vipin")
    print(lst)

    numbers = [6, 8, 3, 6, 7, 3]
    numbers.sort()
    print(numbers)

    l = ['a', 'b', 'c', 'd', 'e', 'f']
    print(l)

    l.pop()
    print(l)

    l.append('g')
    print(l)

    del (l[0])
    print(l)

    l.insert(0, 'i')

    print(l)
    print(l[1])

    #tuple
    #immutable
    empty_tuple = ()

    tup = ('a', 'b', 'c', 'd', 'e', 'f')
    print(tup[0])

    # dictionary
    # unordered data structure
    empty_dict = {}

    names_ages = {"vipin": 36, "reyo": 39, "velluva": 42}
    print(names_ages)

    people = {}
    people['vipin'] = 36
    people['reyo'] = 39
    people['velluva'] = 42
    print(people)

    print(people.keys())
    print(people.values())
    print(people.items())

    for key in people.keys():
        print(key)

    for age in people.values():
        print(age)

    for key, value in people.items():
        print('{}: {}'.format(key, value))


if __name__ == '__main__':
    main()



