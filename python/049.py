"""
Project Euler Problem 49
========================

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one
another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

from itertools import combinations, permutations

from functions import is_prime


def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    combs = combinations(nums, 4)
    for comb in combs:
        primes = [x for x in permutations(comb) if is_prime(x)]
        if len(primes) <= 2:
            continue
    return


if __name__ == '__main__':
    main()
