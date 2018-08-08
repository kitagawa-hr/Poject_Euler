"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from functions import factorint


NUM = 600851475143


def main():
    div = factorint(NUM).keys()
    print(max(div))
    return


if __name__ == '__main__':
    main()
