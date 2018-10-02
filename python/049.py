"""
Project Euler Problem 49
========================

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one
another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
primes, exhibiting this property, but there is one other 4-digit
increasing sequence.

What 12-digit number do you form by concatenating the three terms in this
sequence?
"""

from itertools import combinations,combinations_with_replacement, permutations

from functions import is_prime, list_to_num


def is_arithmetic(seq):
    if seq[2] + seq[0] == 2 * seq[1] and seq[0] != seq[1]:
        return True
    return False


def main():
    ans = []
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    combs = combinations_with_replacement(nums, 4)
    for comb in combs:
        primes = [
            list_to_num(x) for x in permutations(comb)
            if is_prime(list_to_num(x)) and list_to_num(x) > 1000
        ]
        if len(primes) <= 2:
            continue
        for three_primes in combinations(primes, 3):
            if is_arithmetic(sorted(three_primes)):
                ans.append(three_primes)
    true_ans = [x for x in ans if 8147 not in x]
    print(list_to_num((true_ans[0])))
    return


if __name__ == '__main__':
    main()
