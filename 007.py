"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""

from functions import is_prime, gen_num

N = 10001


def main():
    count = 0
    for i in gen_num():
        if is_prime(i):
            count += 1
        if count == N:
            print(i)
            break
    return


if __name__ == '__main__':
    main()
