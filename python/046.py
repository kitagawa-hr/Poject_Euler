"""
Project Euler Problem 46
========================

It was proposed by Christian Goldbach that every odd composite number can
be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""
from math import sqrt, pow
from itertools import count

from functions import is_prime


def is_gold(x):
    if is_prime(x):
        return True
    lim = int(sqrt(x - 2))
    for n in range(1, lim + 1):
        if is_prime(x - 2 * n ** 2):
            return True
    return False


def main():
    n = 33
    while is_gold(n):
        n += 2
    print(n)
    return


if __name__ == '__main__':
    main()
