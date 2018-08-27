"""
Project Euler Problem 28
========================

Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

                              21 22 23 24 25
                              20  7  8  9 10
                              19  6  1  2 11
                              18  5  4  3 12
                              17 16 15 14 13

It can be verified that the sum of both diagonals is 101.

What is the sum of both diagonals in a 1001 by 1001 spiral formed in the
same way?
"""

'''
n(n>=2)周目の最初の数は(2,10,26,...)
a[n+1]=a[n]+8n
四隅の和はS[n]=4a[n]+20n-4
S[500]を求める
'''


def spiral(n):
    if n == 1:
        return 2
    else:
        return spiral(n - 1) + 8 * (n - 1)


def main():
    print(1 + sum([(4 * spiral(n) + 20 * n - 4) for n in range(1, 501)]))
    return


if __name__ == '__main__':
    main()
