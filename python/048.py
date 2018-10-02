"""
Project Euler Problem 48
========================

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

N = 10**10


def main():
    ans = 0
    for n in range(1, 1001):
        ans += n**n % N
    print(ans % N)
    return


if __name__ == '__main__':
    main()
