"""
Project Euler Problem 39
========================

If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

                    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
"""

# a+b+c = N かつ a**2+b**2=c**2なる(a,b,c)の組み合わせ数

N = 1000


def num_combination(p):
    """
    >>> num_combination(120)
    3
    """

    count = 0
    for a in range(1, int(p / 3)):
        for b in range(a, int((p - a) / 2)):
            c = p - a - b
            if c ** 2 - a ** 2 - b ** 2 == 0:
                count += 1
    return count


def main():
    comb_dict = {num_combination(p): p for p in range(12, N + 1)}
    max_comb = max(list(comb_dict.keys()))
    ans = comb_dict[max_comb]
    print(ans)
    return


if __name__ == '__main__':
    main()
