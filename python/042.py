"""
Project Euler Problem 42
========================

The n-th term of the sequence of triangle numbers is given by, t[n] =
1/2n(n+1); so the first ten triangle numbers are:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t[10]. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""

import math

readfile = '../resources/42.txt'
f = open(readfile, 'r', encoding='utf-8')
words = f.read().split(',')
f.close()

alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def calc_score(x):
    score = 0
    for n in x:
        if n in alpha:
            score += alpha.index(n) + 1
    return score


def main():
    scores = [calc_score(n) for n in words]
    end = math.floor(2 * math.sqrt(max(scores)))
    tn = [n * (n + 1) / 2 for n in range(1, end + 1)]
    ans = sum([scores.count(n) for n in tn])
    print(ans)


if __name__ == '__main__':
    main()
