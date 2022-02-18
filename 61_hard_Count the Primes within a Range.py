"""
Count the Primes within a Range
Given two integers create a function that counts the number of primes between the two given integers.

Examples
prime_count(1, 10) ➞ 4
# range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# primes = [2, 3, 5, 7]
# answer = 4

prime_count(1, 100) ➞ 25

prime_count(1, 1000) ➞ 168
Notes
If there are no primes within the given range, return 0.
"""
import math

def prime_count(a, b):

    is_prime = lambda n: n>1 and all(n%i for i in range(2, 1+int(n**.5)))
    return sum([is_prime(n) for n in range(a, b+1)])


    # res = []
    # if a == 1:
    #     a += 1
    #
    # for num in range(a, b+1):
    #     if all(num % i != 0 for i in range(2, int(math.sqrt(num))+1)):
    #         res.append(num)
    # return len(res)
    #



    # 非常に時間がかかる
    # res = []
    #
    # if a == 1:
    #     a += 1
    #
    #     for num in range(a, b):
    #         prime = True
    #         for i in range(2, num):
    #             if num % i == 0:
    #                 prime = False
    #         if prime:
    #             res.append(num)
    #     return len(res)


print(prime_count(1, 11))
print(prime_count(1, 10000))
print(prime_count(3297, 4297))