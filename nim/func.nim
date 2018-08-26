import math

proc is_prime(num: int): bool =
  if num == 1:
    return false
  if num == 2 or num == 3:
    return true
  if num mod 2 == 0 or num mod 3 == 0 or num mod 5 == 0:
    return false
  var div_max = toint(sqrt(tofloat(num)))
  for n in countup(5, div_max + 1, 2):
    if num mod n == 0:
      return false
    return true
