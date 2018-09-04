"""
Project Euler Problem 34
========================

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial

import numpy as np


def fact_eq(x):
    fac = str(x)
    facsum = sum([factorial(int(n)) for n in fac])
    return x == facsum


def main():
    _range = 9 * factorial(9)
    arr = np.arange(1, _range)
    print(sum([x for x in arr if fact_eq(x)]) - 1 - 2)
    return


if __name__ == '__main__':
    main()
