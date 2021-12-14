"""
Reversing a Binary String
Write a function that takes an integer n, reverses the binary representation of that integer, and returns the new integer from the reversed binary.

Examples
reversed_binary_integer(10) ➞ 5
# 10 = 1010 -> 0101 = 5

reversed_binary_integer(12) ➞ 3
# 12 = 1100 -> 0011 = 3

reversed_binary_integer(25) ➞ 19
# 25 = 11001 -> 10011 = 19

reversed_binary_integer(45) ➞ 45
# 45 = 101101 -> 101101 = 45
Notes
All values of n will be positive.
"""

def reversed_binary_integer(n):

  return int(str(bin(n)[2:])[::-1],2)

print(reversed_binary_integer(82))


