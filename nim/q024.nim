"""
Project Euler Problem 24
========================

A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

                    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
4, 5, 6, 7, 8 and 9?
"""

from itertools import permutations

N = 1000000

def gen_perm(num_list):
    perm_list = permutations(num_list)
    return list(perm_list)


def main():
    perm = gen_perm([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    ans = ''.join(list(map(str,perm[N-1])))
    print(int(ans))
    return


if __name__ == '__main__':
    main()
