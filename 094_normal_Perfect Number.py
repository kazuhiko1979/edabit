"""
Perfect Number
Create a function that tests whether or not an integer is a perfect number. A perfect number is a number that can be written as the sum of its factors, excluding the number itself.

For example, 6 is a perfect number, since 1 + 2 + 3 = 6, where 1, 2, and 3 are all factors of 6. Similarly, 28 is a perfect number, since 1 + 2 + 4 + 7 + 14 = 28.

Examples
check_perfect(6) ➞ True

check_perfect(28) ➞ True

check_perfect(496) ➞ True

check_perfect(12) ➞ False

check_perfect(97) ➞ False
"""


def print_factors(x):

  return sum([i for i in range(1, x) if x % i == 0]) == x


  # factors = []
  #
  # for i in range(1, num):
  #   if num % i == 0:
  #     factors.append(i)
  # return sum(factors) == num


  # perfect_num = [i for i in range(1, x + 1) if x % i == 0]
  # return sum(perfect_num[:-1]) == x

print(print_factors(6))
print(print_factors(28))
print(print_factors(496))
print(print_factors(8128))
print(print_factors(33550336))
print(print_factors(12))
print(print_factors(97))