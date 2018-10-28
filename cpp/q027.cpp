#include <iostream>
#include <vector>
#include "euler.hpp"

/*
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
*/

namespace
{
const int N = 1000;
}

int quadratic(int x, int a, int b)
{
    return pow(x, 2) + a * x + b;
}

int prime_len(int a, int b)
{
    int x = 0;
    while (PrimeUtils::isPrime(quadratic(x, a, b)))
    {
        x += 1;
    }
    return x;
}

int main()
{
    int ans = 0, length = 0, tmp = 0;
    for (int i = -N + 1; abs(i) < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            tmp = prime_len(i, j);
            if (tmp > length)
            {
                length = tmp;
                ans = i*j;
            }
        }
    }
    cout << ans << endl;
    return 0;
}
