from itertools import combinations, permutations

friends = 'vipin neeraj amit'.split()

def main():
    # Combinations
    print('Combinations: ')
    for c in list(combinations(friends, 2)):
        print(c)

    # Permutations
    print('Permutations')
    for p in list(permutations(friends, 2)):
        print(p)
        

if __name__ == '__main__':
    main()
