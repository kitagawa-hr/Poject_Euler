"""
Project Euler Problem 14
========================

The following iterative sequence is defined for the set of positive
integers:

n->n/2 (n is even)
n->3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence:
                  13->40->20->10->5->16->8->4->2->1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
N = 1000000


def collatz(x):
    if x % 2 == 0:
        return x / 2
    return 3 * x + 1


def search(x, cache={1: 1}):
    if x in cache:
        return cache[x]
    cache[x] = search(collatz(x)) + 1
    return cache[x]


def main():
    _max= 1
    ans = dict()
    for n in range(2, N):
        length = search(n)
        if length > _max:
            _max = length
            ans[_max] = n
    t_max = max(ans.keys())
    print(ans[t_max])
    return


if __name__ == '__main__':
    main()
