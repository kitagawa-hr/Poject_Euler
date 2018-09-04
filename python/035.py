"""
Project Euler Problem 35
========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from itertools import product

from functions import is_prime, list_to_num

N = 1000000


def cycle(x):
    """
    >>> 345
    [453, 534]
    >>> 12345
    [23451, 34512, 45123, 51234]
    """
    s = str(x)
    return [int(s[y:] + s[:y]) for y in range(len(s))]


num = [1, 3, 7, 9]
ans = [2, 3, 5, 7]
for digit in range(2, 7):
    numlis = list(product(num, repeat=digit))
    primes = [list_to_num(n) for n in numlis if
              is_prime(list_to_num(n))]
    for x in primes:
        if all([is_prime(z) for z in cycle(x)]):
            ans.append(x)
print(len(ans))
