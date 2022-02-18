"""
The Kempner Function
The Kempner Function, applied to a composite number, permits to find the smallest integer greater than zero whose factorial is exactly divided by the number.

kempner(6) ➞ 3

1! = 1 % 6 > 0
2! = 2 % 6 > 0
3! = 6 % 6 === 0

kempner(10) ➞ 5

1! = 1 % 10 > 0
2! = 2 % 10 > 0
3! = 6 % 10 > 0
4! = 24 % 10 > 0
5! = 120 % 10 === 0
A Kempner Function applied to a prime will always return the prime itself.

kempner(2) ➞ 2
kempner(5) ➞ 5
Given an integer n, implement a Kempner Function.

Examples
kempner(6) ➞ 3

kempner(10) ➞ 5

kempner(2) ➞ 2
Notes
Try solving this recursively, with an approach oriented to higher-order functions.
"""
from math import factorial as f

def kempner(n, i=1):

    return kempner(n, i+1) if f(i) % n else i

    # factorial = 1
    # index = 1
    # while True:
    #     factorial = factorial * index
    #     if factorial % n == 0:
    #         return index
    #     else:
    #         index += 1



    # composite_num = 1
    # count = 1
    # calc_devided = lambda a, b: a % b
    #
    # while calc_devided(composite_num, n) > 0:
    #     count += 1
    #     composite_num *= count
    # return count



print(kempner(6))
print(kempner(10))
print(kempner(2))
print(kempner(5))
