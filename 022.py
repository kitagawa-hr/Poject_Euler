"""
Project Euler Problem 22
========================

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def score(name):
    score = 0
    for string in name:
        if string in alphabet:
            score += alphabet.index(string) + 1
    return score


readfile = '22.txt'
f = open(readfile, 'r', encoding='utf-8')
names = f.read().split(',')

names.sort()
ans = 0
for n in range(len(names)):
    ans += score(names[n]) * (n + 1)
print(ans)
