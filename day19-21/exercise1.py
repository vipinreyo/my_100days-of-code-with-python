'''
Learning cucle function from itertools
'''

import itertools
import sys
import time

symbols = itertools.cycle('-\|/')


def main():
    while True:
        sys.stdout.write('\r' + next(symbols))
        sys.stdout.flush()
        time.sleep(0.3)


if __name__ == '__main__':
    main()
