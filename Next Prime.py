"""
Given an integer, create a function that returns the next prime. If the number is prime, return the number itself.

Examples
next_prime(12) ➞ 13
next_prime(24) ➞ 29
next_prime(11) ➞ 11
# 11 is a prime, so we return the number itself.
"""


def next_prime(num):

    if all(num % i for i in range(2, num)):
        return num

    next_prime = num + 1
    prime = True

    while True:
        for i in range(2, next_prime):
            if next_prime % i ==0:
                prime = False
                break
        if prime:
            return next_prime
        else:
            next_prime = next_prime + 1
            if next_prime % 2 == 0:
                next_prime = next_prime + 1
            prime = True


print(next_prime(12))
print(next_prime(24))
print(next_prime(11))

