import math

proc bit_length*[T: SomeInteger](n: T): T =
  ## Calculates how many bits are necessary to represent the number
  result = 1
  var y: T = n shr 1
  var zero: T = 0 #Needed because unsigned and signed 0 are different ...
  while y > zero:
    y = y shr 1
    inc(result)

proc isqrt*[T: SomeInteger](n: T):  T =
  ##integer square root, return the biggest squarable number under n
  ##Computation via Newton method
  var x = n
  const two: T = 2 #necessary to cover uint and int
  var y = (two shl ((n.bit_length()+1) shr 1)) - 1
  while y < x:
      x = y
      y = (x + n div x) shr 1
  return x

proc isPrime*(num: int or int64): bool =
  case num
  of 1:
    return false
  of 2, 3, 5:
    return true
  else:
    discard
  if num mod 2 == 0 or num mod 3 == 0 or num mod 5 == 0:
    return false
  var div_max = isqrt(num)
  if div_max <= 5:
    return true
  for n in countup(5, div_max + 1, 2):
    if num mod n == 0:
      return false
    return true