"""
Project Euler Problem 40
========================

An irrational decimal fraction is created by concatenating the positive
integers:

                  0.123456789101112131415161718192021...
                               ^

It can be seen that the 12th digit of the fractional part is 1.

If d[n] represents the n-th digit of the fractional part, find the value
of the following expression.

    d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]
"""

import itertools

from functions import reduce_mul


def d(x):
    key = list(itertools.accumulate([9, 180, 2700, 36000, 450000, 5400000]))
    if x <= key[0]:
        return x

    for n in range(1, 5):
        if x <= key[n]:
            r = (x - key[n - 1]) % (n + 1)
            q = (x - key[n - 1] - r) / (n + 1)
            if r == 0:
                strr = str(int(10 ** n + q - 1))
                return strr[-1]
            else:
                strr = str(int(10 ** n + q))
                return strr[r - 1]
    return


ans = []
for n in range(1, 6):
    ans.append(int(d(10 ** n)))
print(reduce_mul(ans))
