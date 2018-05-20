import itertools
import os

# PREWORK
DICTIONARY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dictionary.txt')

dictionary = set()
with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    return [word.lower() for word in _get_permutations_draw(draw) if word.lower() in dictionary]


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    return [''.join(p) for r in range(1, 7) for p in itertools.permutations(draw, r=r)]


def main():
    draw = 'T, I, I, G, T, T, L'.split(', ')
    for word in get_possible_dict_words(draw):
        print(word)


if __name__ == '__main__':
    main()
