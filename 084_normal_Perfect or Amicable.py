"""
Perfect or Amicable?
Given a positive number x, if all the positive divisors of x (excluding x) add up to x, then x is said to be a perfect number.

For example, the set of positive divisors of 6 excluding 6 itself is (1, 2, 3). The sum of this set is 6. Therefore, 6 is a perfect number.

Given a positive number x, if all the positive divisors of x add up to a second number y, and all the positive divisors of y add up to x, then x and y are said to be a pair of amicable numbers.

Create a function that takes a number and returns "Perfect" if the number is perfect, "Amicable" if the number is part of an amicable pair, or "Neither".

Examples
num_type(6) ➞ "Perfect"

num_type(2924) ➞ "Amicable"

num_type(5010) ➞ "Neither"
"""
def num_type(n):

    s = sum([i for i in range(1, n) if n % i == 0])
    if s == n:
        return 'Perfect'
    s1 = sum([i for i in range(1, s) if s % i == 0])
    if s1 == n:
        return 'Amicable'
    return 'Neither'



# def factors(num):
#     factors = []
#     for i in range(1, num):
#         if num % i == 0:
#             factors.append(i)
#     return factors
#
# def num_type(n):
#     sum_factors = sum(factors(n))
#     if sum_factors == n:
#         return 'Perfect'
#     elif sum(factors(sum_factors)) == n:
#         return "Amicable"
#     else:
#         return "Neither"


# import math
#
# def num_type(num):
#
#     "Find an addup proper divisors of num"
#     result = 0
#     i = 2
#     while i <= math.sqrt(num):
#         if num % i == 0:
#             if i == (num / i):
#                 result = result + i
#             else:
#                 result = result + (i + num / i)
#         i = i + 1
#
#     x = result+1
#
#     result_y = 0
#     j = 2
#
#     while j <= math.sqrt(x):
#         if x % j == 0:
#             if j == (x / i):
#                 result_y = result_y + j
#             else:
#                 result_y = result_y + (j + x / j)
#         j = j + 1
#
#     y = result_y + 1
#
#     # print(num, x, y)
#
#     if num == x:
#         return "Perfect"
#     elif num == y:
#         return "Amicable"
#     else:
#         return "Neither"


print(num_type(6))
print(num_type(2924))
print(num_type(5010))

