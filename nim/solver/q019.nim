"""
Project Euler Problem 19
========================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""

days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_mod = [x % 7 for x in days_month]


def leap_year(x):
    if x % 4 == 0:
        if x % 100 == 0 and x % 400 != 0:
            return 0
        else:
            return 1
    else:
        return 0


# sumdays%7==5のときを数える
sumdays = 0
counts = 0
for n in range(1901, 2001):
    for m in days_mod:
        if m == 28 and leap_year(n) == 1:
            sumdays += m + 1
        else:
            sumdays += m
        if sumdays % 7 == 5:
            counts += 1
print(counts)
