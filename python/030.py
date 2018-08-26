"""
Project Euler Problem 30
========================

Surprisingly there are only three numbers that can be written as the sum
of fourth powers of their digits:

  1634 = 1^4 + 6^4 + 3^4 + 4^4
  8208 = 8^4 + 2^4 + 0^4 + 8^4
  9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
"""

from math import pow

N = 5
MAX = pow(9, N)


def calc_max_num():
    n = 1
    while MAX * n > pow(10, n - 1):
        n += 1
    return int(pow(10, n - 1) - 1)


def pow_sum(num, power=N):
    str_num = str(num)
    return int(sum(
        [pow(int(str_num[x]), power) for x in range(len(str_num))]
    ))


def main():
    max_num = calc_max_num()
    print(sum([n for n in range(2, max_num) if pow_sum(n) == n]))
    return


if __name__ == '__main__':
    main()
