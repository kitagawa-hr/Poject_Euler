"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from functions import gen_num, is_prime

N = 2000000


def main():
    prime_list = [x for x in gen_num(lim=N) if is_prime(x)]
    print(sum(prime_list))
    return


if __name__ == '__main__':
    main()
