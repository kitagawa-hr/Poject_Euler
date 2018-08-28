"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def is_pitag(a, b, c):
    if a ** 2 + b ** 2 - c ** 2 == 0:
        return True
    return False


def main():
    for a in range(1, 334):
        for b in range(a, 500):
            c = 1000 - a - b
            if is_pitag(a, b, c):
                print(a * b * c)
                return


if __name__ == '__main__':
    main()
