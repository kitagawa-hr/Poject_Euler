"""
Project Euler Problem 31
========================

In England the currency is made up of pound, -L-, and pence, p, and there
are eight coins in general circulation:

  1p, 2p, 5p, 10p, 20p, 50p, -L-1 (100p) and -L-2 (200p).

It is possible to make -L-2 in the following way:

  1 * -L-1 + 1 * 50p + 2 * 20p + 1 * 5p + 1 * 2p + 3 * 1p

How many different ways can -L-2 be made using any number of coins?
"""


def ways_to_change(target, coins):
    if target == 0 or len(coins) == 1:
        return 1
    else:
        coins = sorted(coins)
        largest = coins[-1]
        uses = target // largest
        total = 0
        for i in range(uses + 1):
            total += ways_to_change(target - largest * i, coins[:-1])
        return total


def main():
    print(ways_to_change(200, [1, 2, 5, 10, 20, 50, 100, 200]))


if __name__ == "__main__":
    main()
