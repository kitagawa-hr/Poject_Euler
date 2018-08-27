"""
Project Euler Problem 17
========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""

dig1 = "one,two,three,four,five,six,seven,eight,nine,ten"
dig2 = "eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen"
dig3 = "twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety"

one = [len(x) for x in dig1.split(",")]
teen = [len(x) for x in dig2.split(",")]
ty = [len(x) for x in dig3.split(",")]


def letter_count(x):
    """
    >>> letter_count([3,4,2])
    23
    >>> letter_count([1,1,5])
    20
    >>> letter_count([1,1,0])
    16

    """

    if len(x) == 1:
        if x[0] == 0:
            return 0
        else:
            return one[x[0] - 1]
    elif len(x) == 2:
        if x[0] == 0:
            del x[0]
            return letter_count(x)
        elif x[0] == 1:
            if x[1] == 0:
                return 3  # ten
            else:
                return teen[x[1] - 1]  # -teen
        else:
            a = ty[x[0] - 2]
            del x[0]
            return a + letter_count(x)  # -ty --
    elif len(x) == 3:
        a = one[x[0] - 1]
        del x[0]
        if x[0] == 0 and x[1] == 0:
            return a + 7  # -hundred
        else:
            return a + 7 + 3 + letter_count(x)  # -hundred (and -ty --)


letters = 0

for n in range(1, 1000):
    letters += letter_count([int(x) for x in list(str(n))])
letters += 11  # one thousand
print(letters)
