"""
Project Euler Problem 26
========================

A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

   1/2  =  0.5
   1/3  =  0.(3)
   1/4  =  0.25
   1/5  =  0.2
   1/6  =  0.1(6)
   1/7  =  0.(142857)
   1/8  =  0.125
   1/9  =  0.(1)
  1/10  =  0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
be seen that ^1/[7] has a 6-digit recurring cycle.

Find the value of d < 1000 for which ^1/[d] contains the longest recurring
cycle in its decimal fraction part.
"""

# (1/7)*1000000 - (1/7) = Natural
# (1/7) * 999999 = Natural

from functions import factorint

N = 1000


def cycle_len(x):
    """
    >>> cycle_len(2)
    0
    >>> cycle_len(7)
    6
    >>> cycle_len(9)
    1
    >>> cycle_len(6)
    1
    """

    factors = factorint(x)
    if 2 in factors:
        factors.pop(2)
    if 5 in factors:
        factors.pop(5)
    if not factors:
        return 0
    n = 1
    while True:
        if str(int('9' * n) / x)[-1] == '0':
            return n
        n += 1


def main():
    ans = {cycle_len(n): n for n in range(1, N + 1)}
    print(ans[max(ans.keys())])
    return


if __name__ == '__main__':
    main()
