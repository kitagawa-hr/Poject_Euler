"""
Project Euler Problem 15
========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""

from functions import reduce_mul

num = reduce_mul([x for x in range(21, 41)])
denum = reduce_mul([x for x in range(1, 21)])
print(int(num/denum))

