"""
Project Euler Problem 36
========================

The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

N = 1000000

ans = []
for n in range(1, N)[::2]:
    if str(n) == str(n)[::-1]:
        y = bin(n)[2:]
        if y == y[::-1]:
            ans.append(n)
print(sum(ans))
