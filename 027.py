"""
Project Euler Problem 27
========================

Euler published the remarkable quadratic formula:

                               n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41
is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered,
which produces 80 primes for the consecutive values n = 0 to 79. The
product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

  n^2 + an + b, where |a| < 1000 and |b| < 1000

                              where |n| is the modulus/absolute value of n
                                               e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic
expression that produces the maximum number of primes for consecutive
values of n, starting with n = 0.
"""
from itertools import product
from functions import is_prime

N = 5


def quadratic(x, a, b):
    return x ** 2 + a * x + b


def prime_len(a, b):
    """
    >>> prime_len(1,41)
    40
    >>> prime_len(-79,1601)
    80
    """
    x = 0
    while is_prime(quadratic(x, a, b)):
        x += 1
    return x


def main():
    a_range = [x for x in range(-N, N + 1) if x % 2 == 1]
    b_range = [x for x in range(2, N) if is_prime(x)]
    param = list(product(a_range, b_range))
    ans = 0
    length = 0
    for a, b in param:
        if prime_len(a, b) > length:
            length = prime_len(a, b)
            ans = a * b
    print(ans)
    return


if __name__ == '__main__':
    main()
