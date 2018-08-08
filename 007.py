"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

from functions import is_prime

def gen_num():
    n = 1
    yield 2
    yield 3
    while True:
        yield 6 * n - 1
        yield 6 * n + 1
        n += 1


def main():
    count = 0
    for i in gen_num():
        if is_prime(i):
            count += 1
        if count == 100001:
            print(i)
            break
    return

if __name__ == '__main__':
    main()
