"""
Project Euler Problem 33
========================

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""

import math

from functions import reduce_mul


def reduction(p, q):
    common = math.gcd(p, q)
    return p // common, q // common


def main():
    ans = []
    num = [str(y) for y in range(1, 10)]
    b_list = [x for x in range(10, 100) if x % 10 != 0]
    for b in b_list:
        for a in [x for x in range(10, b) if x % 10 != 0]:
            common = [x for x in num if (x in str(a) and x in str(b))]
            if len(common) == 1:
                c = str(a).replace(common[0], '')
                d = str(b).replace(common[0], '')
                if c == '' or d == '':
                    continue
                elif a * int(d) == b * int(c):
                    ans.append([a, b])
    numer = reduce_mul([x[0] for x in ans])
    denom = reduce_mul([x[1] for x in ans])
    print(reduction(numer, denom)[-1])
    return


if __name__ == '__main__':
    main()
