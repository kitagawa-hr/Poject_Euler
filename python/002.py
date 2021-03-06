"""
Project Euler Problem 2
=======================

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

                  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not
exceed four million.
"""

import functools


@functools.lru_cache(maxsize=None)
def fibo(n):
    if n == 1 or n == 2:
        return n
    return fibo(n - 1) + fibo(n - 2)


def main():
    MAX = 4000000
    n = 1
    fibo_list = []
    while fibo(n) <= MAX:
        fibo_list.append(fibo(n))
        n += 1
    ans = sum(filter(lambda x: x % 2 == 0, fibo_list))
    print(ans)
    return


if __name__ == '__main__':
    main()
