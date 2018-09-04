"""
Project Euler Problem 37
========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from itertools import product

from functions import is_prime, list_to_num


def is_truncable(x):
    """
    >>> is_truncable(3797)
    True

    """
    s = str(x)
    if all([is_prime(int(s[i:])) for i in range(len(s))]):
        if all([is_prime(int(s[:i])) for i in range(1, len(s) + 1)]):
            return True
    return False


def main():
    num = [1, 3, 7, 9]
    ans = []
    for n in range(8, 100):
        if is_truncable(n):
            ans.append(n)

    for digit in range(3, 7):
        numlis = list(product(num, repeat=digit))
        for x in numlis:
            y = list_to_num(x)
            if is_truncable(y):
                ans.append(y)
        if len(ans) >= 11:
            print(sum(ans[:11]))
            return


if __name__ == '__main__':
    main()
