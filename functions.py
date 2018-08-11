#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project_Euler.functions
Date: 2018/08/08
Filename: functions 
@author: kitagawaharuki
"""

from collections import defaultdict
from functools import reduce
from operator import mul
import math
from timeit import timeit
from numba import jit


@jit('boolean(int64)')
def is_prime(num):
    """
    >>> is_prime(3)
    True
    >>> is_prime(7)
    True
    >>> is_prime(17)
    True
    >>> is_prime(6)
    False
    >>> is_prime(25)
    False
    >>> is_prime(111111)
    False
    """

    if num == 2 or num == 3:
        return True
    if num % 6 in [0, 2, 3, 4]:
        return False
    div_max = int(math.sqrt(num))
    for div in range(5, div_max + 1, 2):
        if num % div == 0:
            return False
    return True


def factorint(x):
    """
    >>> factorint(24)
    defaultdict(<class 'int'>, {2: 3, 3: 1})
    >>> factorint(28)
    defaultdict(<class 'int'>, {2: 2, 7: 1})
    >>> factorint(80)
    defaultdict(<class 'int'>, {2: 4, 5: 1})
    >>> factorint(77)
    defaultdict(<class 'int'>, {7: 1, 11: 1})
    """

    factors = defaultdict(int)
    while not is_prime(x):
        div_max = int(math.sqrt(x))
        for div in range(2, div_max + 1):
            if x % div == 0:
                factors[div] += 1
                x = int(x / div)
                break
    factors[x] += 1
    return factors


def divisor_num(x):
    """
    >>> divisor_num(28)
    6
    >>> divisor_num(24)
    8
    >>> divisor_num(100)
    9
    """
    factor_pow = map(lambda y: y + 1, factorint(x).values())
    div_num = reduce(mul, factor_pow)
    return div_num


def divisor_sum(x):
    """
    >>> divisor_sum(220)
    284
    >>> divisor_sum(284)
    220
    >>> divisor_sum(28)
    28
    """
    factors = factorint(x)
    primes = factors.keys()
    powers = factors.values()
    sums = list()
    for i, p in enumerate(list(primes)):
        sums.append(sum([math.pow(p, x) for x in range(list(powers)[i] + 1)]))
    return int(reduce_mul(sums)) - x


def gen_num():
    n = 1
    yield 2
    yield 3
    while True:
        yield 6 * n - 1
        yield 6 * n + 1
        n += 1


def reduce_mul(num_list):
    return reduce(mul, num_list)


if __name__ == '__main__':
    pass
