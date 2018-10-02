"""
Project Euler Problem 44
========================

Pentagonal numbers are generated by the formula, P[n]=n(3n-1)/2. The first
ten pentagonal numbers are:

               1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P[4] + P[7] = 22 + 70 = 92 = P[8]. However, their
difference, 70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, P[j] and P[k], for which their sum
and difference is pentagonal and D = |P[k] - P[j]| is minimised; what is
the value of D?
"""

import math
from itertools import count

from functions import is_square


def pentagon():
    for n in count(2):
        yield int(n * (3 * n - 1) / 2)


def is_pentagon(x):
    """
    >>> is_pentagon(1)
    True
    >>> is_pentagon(5)
    True
    >>> is_pentagon(12)
    True
    >>> is_pentagon(22)
    True
    >>> is_pentagon(15)
    False
    """
    if x < 1:
        return False
    if is_square(1 + 24 * x):
        if int(math.sqrt(1 + 24 * x)) % 6 == 5:
            return True
    return False


def main():
    pentagon_list = [1]
    gen = pentagon()
    while True:
        pentagon_list.append(next(gen))
        max_pent = pentagon_list[-1]
        for pent in pentagon_list:
            if max_pent - pent in pentagon_list and is_pentagon(max_pent + pent):
                ans = max_pent - pent
            if ans < pentagon_list[-1] - pentagon_list[-2]:
                print(ans)
                #print(n)
                return


if __name__ == '__main__':
    main()
