discard """
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import system, macros, algorithm, tables, sets, lists, queues, intsets, critbits, sequtils, strutils, math, future
import utils.functions

proc factor(x: int or int64): seq[int] =
  while not isPrime(x):
    var 
        lim = isqrt(x)
        facLis: seq[int] = @[]
    for n in 2..lim:
      if x mod n == 0:
        facLis.add()
    return facLis

let NUM: int64 = 600851475143
var ans = factor(NUM)
echo(max(ans))