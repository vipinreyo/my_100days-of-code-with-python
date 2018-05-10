'''
Learning cartesian product function from itertools
'''
from itertools import product

def main():
    for i in product('anantha', repeat=1):
        print(i)

    for i in product('anantha', repeat=2):
        print(i)

    for i in product('anantha', repeat=3):
        print(i)
        

if __name__ == '__main__':
    main()
