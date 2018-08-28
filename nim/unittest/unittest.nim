import unittest
import ../utils/functions

test "test isPrime":
  check(isPrime(1) == false)
  check(isPrime(4) == false)
  check(isPrime(44) == false)
  check(isPrime(111) == false)
  check(isPrime(1000) == false)
  check(isPrime(1000000) == false)
  check(isPrime(2) == true)
  check(isPrime(3) == true)
  check(isPrime(5) == true)
  check(isPrime(7) == true)
  check(isPrime(19) == true)
  check(isPrime(126107 ) == true)
  check(isPrime(9999991) == true)
