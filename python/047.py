"""
Project Euler Problem 47
========================

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors
are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?
"""

from itertools import chain
from numba import jit

from functions import factorint


@jit
def has_unique_key(seq1, seq2):
    for num in seq1:
        if num not in seq2:
            return True
    return False


@jit
def is_four_consective(n):
    a, b, c, d = \
    factorint(n), factorint(n + 1), factorint(n + 2), factorint(n + 3)
    if len(a) == 4 and len(b) == 4 and len(c) == 4 and len(d) == 4:
        return True
    return False


def main():
    n = 2
    while not is_four_consective(n):
        n += 1
    print(n)
    return


if __name__ == '__main__':
    main()