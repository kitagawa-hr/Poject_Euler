"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(x):
    string = str(x)
    if string == string[::-1]:
        return True
    return False


def div_3digit(x):
    for n in range(100, 1000):
        if x % n == 0 and 100 <= x / n <= 999:
            return True
    return False


def main():
    num = 999 * 999
    while not (is_palindrome(num) and div_3digit(num)):
        num -= 1
    print(num)

    return


if __name__ == '__main__':
    main()
